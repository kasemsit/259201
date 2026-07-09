#!/usr/bin/env python3
"""สร้าง QR code สำหรับลิงก์โหวต แล้วบันทึกลง slides/images/qr-poll-<pollId>.png

ใช้งาน (รันหลัง deploy แล้วรู้ URL จริง):
    python make-qr.py https://YOUR-DECK.web.app/slides/poll/vote.html intro goal

- อาร์กิวเมนต์ตัวแรก = base URL ของ vote.html ที่ deploy แล้ว
- อาร์กิวเมนต์ที่เหลือ = pollId (ต้องตรงกับ key ใน poll-config.js)
"""
import os
import sys

import qrcode

base = sys.argv[1] if len(sys.argv) > 1 else "https://YOUR-DECK.web.app/slides/poll/vote.html"
polls = sys.argv[2:] or ["intro"]
outdir = os.path.join(os.path.dirname(__file__), "..", "images")

for p in polls:
    url = f"{base}?poll={p}"
    qr = qrcode.QRCode(border=2, box_size=10)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#2c3e50", back_color="white")
    path = os.path.join(outdir, f"qr-poll-{p}.png")
    img.save(path)
    print("saved", os.path.normpath(path), "→", url)
