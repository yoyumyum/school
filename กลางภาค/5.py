numbers = []
for _ in range(5):
    n = int(input())
    numbers.append(n)

total = sum(numbers)
average = total / 5

print(f"ผลรวม: {total}")
print(f"ค่าเฉลี่ย: {average}")
