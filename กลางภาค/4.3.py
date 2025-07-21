min_value = None

while True:
    try:
        num = float(input("ป้อนจำนวนจริงบวก: "))
        if num <= 0:
            break
        if min_value is None or num < min_value:
            min_value = num
    except ValueError:
        break

if min_value is not None:
    print(f"ค่าน้อยที่สุดคือ: {min_value}")
else:
    print("ไม่มีจำนวนจริงบวกที่รับเข้ามา")
