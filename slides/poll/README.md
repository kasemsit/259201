# ระบบโหวตในสไลด์ (Firebase Realtime Database — ฟรี)

โหวตสด ๆ ในคลาส: นักศึกษาสแกน QR → เลือกคำตอบบนมือถือ → กราฟผลโหวตในสไลด์ **อัปเดตทันที**
ทุกอย่างฟรี (Firebase **Spark plan**) และเป็นของเราเอง ไม่มีลิมิตคำถาม

## ไฟล์ในโฟลเดอร์นี้

| ไฟล์ | หน้าที่ |
|---|---|
| `poll-config.js` | ใส่ Firebase config + กำหนดคำถาม/ตัวเลือก (แก้ไฟล์นี้ไฟล์เดียว) |
| `vote.html` | หน้าที่นักศึกษาเปิดบนมือถือเพื่อโหวต |
| `results.html` | กราฟผลโหวต (ฝังเป็น `<iframe>` ในสไลด์) |
| `make-qr.py` | สร้าง QR code ของลิงก์โหวต → `../images/qr-poll-<id>.png` |

## ตั้งค่าครั้งเดียว

1. **สร้างโปรเจกต์ Firebase** (ฟรี) ที่ <https://console.firebase.google.com>
2. **เปิด Realtime Database**: เมนู *Build → Realtime Database → Create database → Start in test mode*
3. **คัดลอก config**: *Project settings (⚙️) → Your apps → Web `</>`* แล้วนำค่าไปวางใน `poll-config.js` (`window.FIREBASE_CONFIG`)
4. **ตั้ง Rules** ของ Realtime Database ให้โหวตได้ (เปิดเฉพาะ node `polls`):

   ```json
   {
     "rules": {
       "polls": { ".read": true, ".write": true },
       "$other": { ".read": false, ".write": false }
     }
   }
   ```

   > ⚠️ นี่เปิดให้ใครก็ได้ที่มีลิงก์ อ่าน/เขียน `polls` ได้ — เหมาะกับการใช้ในคลาส ความเสี่ยงต่ำ

5. **Deploy** ให้มือถือนักศึกษาเข้าถึง `vote.html` ได้ (ต้องเป็น URL สาธารณะ) — เลือกวิธีใดก็ได้:
   - **Firebase Hosting** (แนะนำ เพราะอยู่โปรเจกต์เดียวกัน): `firebase init hosting` ชี้ public เป็น `_output` แล้ว `firebase deploy`
   - หรือ **GitHub Pages / Netlify** ชี้ไปที่โฟลเดอร์ `_output`
6. **สร้าง QR** ด้วย URL จริงหลัง deploy:

   ```bash
   cd slides/poll
   ../../.venv/bin/python make-qr.py https://YOUR-APP.web.app/slides/poll/vote.html intro goal
   ```

   แล้ว render สไลด์ใหม่

## เพิ่มคำถามใหม่

1. เพิ่ม key ใน `poll-config.js` เช่น
   ```js
   window.POLLS.goal = { question: "…", options: ["…","…"] };
   ```
2. ใส่สไลด์ (ดูตัวอย่างที่ `slides/module01.qmd` — id `#m1-poll`):
   ```markdown
   ![](images/qr-poll-goal.png){width="220px"}

   ```{=html}
   <iframe src="poll/results.html?poll=goal" style="width:100%;height:350px;border:0"></iframe>
   ```
   ```
3. สร้าง QR ของ pollId ใหม่ด้วย `make-qr.py … goal`

## สอนหลายรอบ — ผลไม่ปนกัน (session)

ผลโหวตถูกแยกตาม **session** โดยเก็บที่ `polls/<pollId>/<session>/votes`

- **ไม่ระบุ session** → ใช้ **วันที่วันนี้** อัตโนมัติ (เช่น `2025-06-24`)
  → สอนคนละวัน ผลจะ **แยกกันเอง** ไม่ต้องทำอะไรเพิ่ม ✅
- **สอน 2 sections ในวันเดียวกัน** → ใส่ `&session=...` ให้ต่างกัน ทั้งใน iframe และ QR:
  ```markdown
  <iframe src="poll/results.html?poll=intro&session=secA"></iframe>
  ```
  ```bash
  python make-qr.py https://YOUR-APP.web.app/slides/poll/vote.html "intro&session=secA"
  ```
  > สำคัญ: หน้า **vote** กับ **results** ต้องใช้ `session` เดียวกันถึงจะนับรวมกัน

## ระหว่างสอน

- เปิดสไลด์หน้าโหวต → กราฟผลโหวตขึ้นเรียลไทม์ (มุมล่างบอก session ที่กำลังใช้)
- กด **"ล้างผล"** มุมขวาล่าง เพื่อล้างเฉพาะ session นั้น (เช่น อยากเริ่มนับใหม่ในคาบเดียวกัน)
- นักศึกษาโหวตซ้ำใน session เดิมไม่ได้ (จำด้วย `localStorage`) — แต่คาบใหม่ (วันใหม่) โหวตได้อีก
