// =============================================================
//  ตั้งค่าระบบโหวต (Firebase Realtime Database — ฟรี Spark plan)
// =============================================================
//
//  1) สร้างโปรเจกต์ที่ https://console.firebase.google.com  (ฟรี)
//  2) เมนู Build → Realtime Database → Create database → เลือก "Start in test mode"
//  3) เมนู Project settings (⚙️) → Your apps → Web app (</>) → คัดลอกค่า config มาวางด้านล่าง
//  4) ตั้ง Rules ของ Realtime Database ให้อ่าน/เขียนโพลได้ (ดู poll/README.md)
//
//  ---- วางค่า Firebase config ของคุณตรงนี้ ----
window.FIREBASE_CONFIG = {
  apiKey:      "PASTE_YOUR_API_KEY",
  authDomain:  "PASTE_PROJECT_ID.firebaseapp.com",
  databaseURL: "https://PASTE_PROJECT_ID-default-rtdb.firebaseio.com",
  projectId:   "PASTE_PROJECT_ID",
  appId:       "PASTE_APP_ID"
};

// =============================================================
//  คำถามโหวต — เพิ่ม/แก้ได้ตามต้องการ
//  key ของแต่ละอัน = pollId ที่ใช้ในลิงก์  (เช่น ?poll=intro)
// =============================================================
window.POLLS = {
  intro: {
    question: "คุณเคยเขียนโปรแกรมมาก่อนหรือไม่?",
    options: ["ไม่เคยเลย", "เคยนิดหน่อย", "เคยพอสมควร", "เขียนได้คล่อง"]
  },
  goal: {
    question: "อยากเขียนโปรแกรมไปทำอะไรมากที่สุด?",
    options: ["เกม", "เว็บ / แอป", "AI / ข้อมูล", "หุ่นยนต์ / IoT"]
  }
};
