numbers = []

while (num := int(input("Nhập một số nguyên (nhập -1 để kết thúc) : "))) != -1:
    numbers.append(num)

print("Số lớn nhất : ", max(numbers) if numbers else "Dãy số trống!")
print("Số nhỏ nhất : ", min(numbers) if numbers else "Dãy số trống!")

