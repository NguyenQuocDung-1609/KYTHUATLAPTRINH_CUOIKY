def computepay(hours, rate):
    if hours > 40:
        luong_bt = 40 * rate
        luong_tong = luong_bt + (hours - 40) * rate * 1.5
    else:
        luong_tong = hours * rate
    return luong_tong

# Nhập dữ liệu
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Gọi hàm và in kết quả
pay = computepay(hours, rate)
print("Pay:", pay)