# Yêu cầu: Viết lại chương trình tính lương, trả 1.5 lần tỉ lệ giờ cho số giờ làm trên 40.

try:
    # Bước 1: Nhận đầu vào từ người dùng và chuyển sang số thực
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    
    # Khởi tạo biến pay
    pay = 0.0
    
    # Bước 2: Kiểm tra nếu số giờ làm lớn hơn 40
    if hours > 40:
        # Giờ làm thêm (overtime) = Tổng giờ - 40
        overtime_hours = hours - 40
        
        # Lương cơ bản cho 40 giờ
        regular_pay = 40 * rate
        
        # Lương làm thêm: Giờ làm thêm * (1.5 * Tỉ lệ giờ)
        overtime_pay = overtime_hours * (1.5 * rate)
        
        # Tổng lương
        pay = regular_pay + overtime_pay
        
    else:
        # Nếu tổng giờ làm <= 40, tính lương cơ bản
        pay = hours * rate
        
    # Bước 3: In ra kết quả
    print("Pay:", pay)
    
# Xử lý ngoại lệ: Bắt lỗi nếu người dùng nhập ký tự không phải số
except ValueError:
    print("Error, please enter numeric input for hours and rate.")

# Ví dụ chạy với dữ liệu trong đề bài (Hours: 45, Rate: 10):
# Regular Pay: 40 * 10 = 400
# Overtime Hours: 45 - 40 = 5
# Overtime Rate: 1.5 * 10 = 15
# Overtime Pay: 5 * 15 = 75
# Total Pay: 400 + 75 = 475.0 (Đúng với kết quả mẫu)