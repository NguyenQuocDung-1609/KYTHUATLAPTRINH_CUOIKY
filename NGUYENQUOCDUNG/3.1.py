Hours = float(input("Enter Hours: "))
Rate = float(input("Enter Rate: "))

if Hours > 40:
    Luong_BT = 40 * Rate
    Luong_tong = Luong_BT + (Hours - 40)*Rate*1.5
else:
    Luong_tong = Hours * Rate

print("Pay:", Luong_tong)
