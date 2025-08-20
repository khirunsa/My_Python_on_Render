from flask import Flask, jsonify
import time

app = Flask(__name__)

def run_script():
    # ====== วางโค้ด Python ของคุณตรงนี้ ======
    # ตัวอย่าง: แสดงเวลาปัจจุบัน
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    return f"สคริปต์ทำงานแล้ว: {now}"

@app.get("/")
def home():
    return "พร้อมใช้งานแล้ว! เปิด /run เพื่อสั่งรันสคริปต์"

@app.get("/run")
def run():
    result = run_script()
    return jsonify({"result": result})
