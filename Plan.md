# แผนพัฒนาเนื้อหา 259201 — Computer Programming for Engineers

> เป้าหมาย: ยกระดับจาก "สอนครบ syntax" → **"ทักษะเขียนโปรแกรมที่ใช้งานได้จริงสำหรับวิศวกร"**
> อ้างอิงแนวทางการสอนจาก [`Idea.md`](Idea.md) (State/Sequence/Selection/Iteration + Trace + Predict + Debug)
> สถานะปัจจุบัน: Module 1–12 (เนื้อหาหลัก) + Extra ครบทุก module

---

## หลักการที่ต้องยึด (ทุกงานในแผนนี้)

- ยึด convention ใน [`CLAUDE.md`](CLAUDE.md) — `live-revealjs`, `custom.scss`, `.exercise`/`.exercise-think`, panel-tabset Live Code/เฉลย
- **ห้ามเกินขอบเขตที่สอน** — ตรวจ token/แนวคิดเทียบ slide หลักก่อนเสมอ (เช่น `None`, `len()` early, bitwise ต้องเช็ค)
- แต่ละ Extra เผยเฉลยด้วย `. . .` + callout (MC/Predict/Trace/Bug) หรือ panel-tabset (เติมคำ)
- อัปเดต [`index.qmd`](index.qmd) และลิงก์ข้ามโมดูลทุกครั้งที่เพิ่มไฟล์

---

## Part A — เสริม Trace/Predict/Debug ในจุดที่ยาก 🔴 (ทำก่อน)

เหตุผล: นักศึกษาไม่ติด syntax แต่ **"ตามค่าตัวแปรไม่ทัน"** — เพิ่มโจทย์ในจุดที่ mental model พังบ่อยสุด

| Module | จุดยาก | เพิ่ม (ประเภท × จำนวน) |
|---|---|---|
| **M9 Scope** ⭐ | local/global, parameter เป็น local, ชื่อซ้ำคนละตัว | Trace table 2–3 ข้อ (ไล่ global vs local พร้อมกัน) |
| **M7 Nested loop** ⭐ | ลูปซ้อน `(i,j)`, นับรอบรวม, `break` อยู่ลูปไหน | Trace ตาราง `(i,j)` ทีละรอบ 2 ข้อ + Predict 1 |
| **M10 List comp** ⭐ | comp + `if`, nested 2D comp | "แปลง loop ↔ comprehension" 2–3 ข้อ |
| **M12 NumPy** ⭐⭐ | broadcasting rules, `axis 0 vs 1`, View vs Copy | Predict shape เข้ากันได้ไหม 2 ข้อ + axis 1 ข้อ |
| **M5** | `if-elif-else` ทำสาขาเดียว, nested if | Trace เส้นทางเงื่อนไข 1–2 ข้อ |
| **M8** | เข้าถึง nested `a[i][j]`, dict iteration | Predict การเข้าถึงหลายชั้น 1–2 ข้อ |

**ผลลัพธ์:** Extra ของ M5, M7, M8, M9, M10, M12 หนาแน่นขึ้นในจุดวิกฤต

---

## Part B — สอดแทรกโจทย์เชิง Engineering 🟡

เหตุผล: วิชานี้คือ *for Engineers* แต่ Extra ปัจจุบันใช้บริบททั่วไป (คะแนน/ผลไม้) เป็นหลัก
แนวทาง: เพิ่มหมวด **"Engineering Application"** ~3–4 ข้อต่อ module **โดยไม่เพิ่ม syntax ใหม่**

| แนวคิด Python | โจทย์วิศวกรรมที่ใช้ได้ |
|---|---|
| ตัวแปร/สูตร (M3) | แปลงหน่วย, กฎของโอห์ม `V=IR`, BMI, ความเค้น `σ=F/A` |
| เงื่อนไข (M5) | safety factor, ช่วง PM2.5 → ระดับเตือน |
| loop (M6–8) | ค่าเฉลี่ยข้อมูลเซนเซอร์, พลังงานสะสม, ตารางการวัด |
| function (M9) | โมดูลคำนวณ (โมเมนต์/กระแส) เรียกซ้ำ |
| list comp (M10) | sampling สัญญาณ, normalize ข้อมูลวัด |
| matplotlib (M11) | กราฟข้อมูลทดลอง (มีบางส่วนแล้ว) |
| NumPy (M12) | เมทริกซ์วงจร/โครงสร้าง, สถิติการวัดหลายรอบ |

**หมายเหตุ:** ตรวจว่าหน่วย/สูตรถูกต้องเชิงฟิสิกส์ และผลลัพธ์ตัวเลขในเฉลยคำนวณจริง

---

## Part C — Module ใหม่ที่ขาด (13–17) 🆕

เทียบตาราง CT→Python ใน `Idea.md` — ยังขาด **Abstraction→Class** และ **Evaluation→Testing/Debugging**
และทักษะพื้นฐานที่ทำให้ "รับข้อมูลจริงไม่ได้ / โปรแกรมพังง่าย"

| ลำดับ | Module | ขอบเขต | สถานะความจำเป็น |
|:--:|---|---|:--:|
| **13** | **String Processing** | `.upper/.lower/.strip/.find/.replace/.split`, string slice, การ parse ข้อความ/รหัสชิ้นงาน | 🔴 ควรมี |
| **14** | **File I/O & CSV** | `open/read/write/with`, อ่านไฟล์ข้อมูลการวัด, เขียนผลลัพธ์, CSV เบื้องต้น | 🔴 ควรมี |
| **15** | **Exception Handling & Debugging** | `try/except/finally`, input ที่ทนทาน, ผูกกับ "Debug ตั้งแต่วันแรก" | 🔴 ควรมี |
| **16** | **Classes / OOP** | `class/__init__/method/attribute`, จำลอง object เชิงวิศวกรรม (เติมเสา Abstraction) | 🟡 น่ามี |
| **17** | **Data Analysis with Pandas** | `DataFrame`, อ่าน CSV, filter/group, ต่อยอด M11–12 | 🟡 น่ามี |
| — | (optional) Recursion · Algorithms (search/sort + Big-O) · Testing | เสริมความลึก | ⚪ ไม่จำเป็นสำหรับคอร์สแรก |

**ความเห็นสรุป:** 12 module ครอบคลุมแกนหลักของ intro course พอแล้ว — แต่ถ้าเป้าคือ *ทักษะใช้งานจริง*
อย่างน้อยควรเพิ่ม **M13 (String) + M14 (File I/O) + M15 (Exception)** เพราะเป็นช่องว่างที่ทำให้ตอนนี้
นักศึกษายัง "อ่านข้อมูลจากไฟล์จริงไม่ได้" และ "เขียนโปรแกรมที่ไม่พังตอนเจอ input แปลก ๆ ไม่เป็น"

### โครงมาตรฐานของ module ใหม่แต่ละตัว (ตาม convention เดิม)
- Front matter + topics-slide + section dividers + summary + xkcd พักสมอง
- เนื้อหา + Live Code (`{pyodide}`) แทรกโจทย์ `.exercise` เป็นระยะ
- SVG diagram วาดเอง (ไม่ raster) ตาม 3 pipelines
- ไฟล์ Extra คู่กัน (MC + Predict + Trace + Bug + เติมคำ)
- ต้องมี source: เขียนใหม่ หรือแปลงจาก `.ipynb` (ถ้าจะทำ ให้เพิ่ม notebook ต้นฉบับด้วย)

---

## ลำดับการทำ (Phasing)

1. **Phase 1 (เร็ว, คุณค่าสูง):** Part A — เสริม Trace/Predict/Debug ใน M9, M7, M10, M12
2. **Phase 2:** Part B — โจทย์ Engineering ใน Extra ที่มีอยู่ (นำร่อง M3, M5, M9, M12)
3. **Phase 3:** Part C — ร่าง **Module 13 (String)** เป็นต้นแบบ 1 module ก่อน แล้วรีวิว ก่อนทำ M14–15
4. **Phase 4:** M16 (OOP), M17 (Pandas) — ถ้าตัดสินใจขยายขอบเขตคอร์ส

## Definition of Done (ทุก Phase)
- [ ] ทุกไฟล์ `quarto render` ผ่าน ไม่มี error/warn
- [ ] ตรวจ token/แนวคิด — ไม่มีอะไรเกินที่สอน (ยกเว้นที่ตั้งใจแนะนำเป็น module ใหม่)
- [ ] ผลลัพธ์ในเฉลยคำนวณจริง ตรงกับโค้ด
- [ ] อัปเดต `index.qmd` + ลิงก์ข้ามโมดูล + cross-references
- [ ] เลขข้อในแต่ละ deck ต่อเนื่อง ไม่ชนกัน

---

## คำถามที่ต้องตัดสินใจก่อนเริ่ม Part C
- คอร์สนี้กำหนดจบที่ 12 module (ตามหลักสูตร/เวลาสอน) หรือขยายได้?
- Module ใหม่จะ **ออกสอบ** ไหม (มีผลต่อความละเอียดของ Extra)
- OOP (M16) อยู่ในขอบเขตของวิชาปีนี้หรือเป็นวิชาต่อยอด?
