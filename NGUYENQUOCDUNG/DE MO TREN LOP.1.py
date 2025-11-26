a = 'Mã OTP của bạn là: 1357'  # chuỗi ban đầu
for i in range(len(a)):           # duyệt từng ký tự trong chuỗi
    if a[i].isdigit():            # nếu ký tự là số
        b = a[i:]                 # cắt chuỗi từ vị trí đó trở đi
        break                     # dừng lại vì đã tìm được số
c = float(b)                      # đổi chuỗi số sang kiểu float
print(c)                          # in kết quả ra
