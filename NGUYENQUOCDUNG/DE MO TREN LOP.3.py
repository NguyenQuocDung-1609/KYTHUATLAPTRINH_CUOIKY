# Yêu cầu người dùng nhập mật khẩu
password = input("Nhập mật khẩu (ít nhất 8 ký tự): ")
# Kiểm tra độ dài mật khẩu
while len(password) < 8:
    print("Mật khẩu phải có ít nhất 8 ký tự!")
    password = input("Nhập lại mật khẩu: ")
# Kiểm tra xem mật khẩu có chứa chữ, số và ký tự đặc biệt không
co_chu = False
co_so = False
co_ky_tu_dac_biet = False
for ch in password:
    if ch.isalpha():           # là chữ
        co_chu = True
    elif ch.isdigit():         # là số
        co_so = True
    else:                      # không phải chữ, không phải số → ký tự đặc biệt
        co_ky_tu_dac_biet = True
# Đánh giá độ mạnh của mật khẩu
if co_chu and co_so and co_ky_tu_dac_biet:
    print("Mật khẩu mạnh!")
else:
    print("Mật khẩu yếu!")
