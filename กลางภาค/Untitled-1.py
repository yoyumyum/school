hour = int(input("กรุณาใส่จำนวนชั่วโมง: "))
minute = int(input("กรุณาใส่จำนวนนาที: "))

# เช็คว่ามีค่าติดลบไหม
if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    # คำนวณเวลาจอดรวมเป็นชั่วโมง (เศษนาทีถือเป็นชั่วโมงเต็ม)
    total_hours = hour
    if minute > 0:
        total_hours += 1

    # ชั่วโมงแรกจอดฟรี
    if total_hours <= 1:
        price = 0
    else:
        price = (total_hours - 1) * 30

    print("ค่าจอดรถ: {} บาท".format(price))
