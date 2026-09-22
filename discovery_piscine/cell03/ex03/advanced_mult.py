import sys

# ตรวจสอบว่ามีการพิมพ์ argument ต่อท้ายตอนรันคำสั่งหรือไม่
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    # while loop ตัวที่ 1: ควบคุมแม่สูตรคูณตั้งแต่แม่ 0 ถึง 10
    while i <= 10:
        print(f"Table de {i}:", end="")
        
        j = 0
        # while loop ตัวที่ 2: ควบคุมตัวคูณตั้งแต่คูณ 0 ถึง 10
        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
            
        print() # ขึ้นบรรทัดใหม่เมื่อแสดงผลสูตรคูณแต่ละแม่เสร็จ
        i += 1