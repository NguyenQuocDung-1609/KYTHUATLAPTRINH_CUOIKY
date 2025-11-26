try:
    Hours = float(input("Enter Hours: "))
    Rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if Hours > 40:
    Luong_BT = 40 * Rate
    Luong_them = Hours - 40
    Luong_tong = Luong_BT + Luong_them * 1.5 * Rate
else:
    Luong_tong = Hours * Rate

print("Pay:", Luong_tong)


