try:
    # Cố gắng nhận và chuyển đổi đầu vào sang số thực
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    
    # Phần tính toán lương (giả định đã đúng)
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        pay = hours * rate
        
    print("Pay:", pay)

# Bắt lỗi khi việc chuyển đổi sang float thất bại (input không phải số)
except ValueError:
    print("Error, please enter numeric input")
    # Chương trình tự động thoát sau khi khối except kết thúc