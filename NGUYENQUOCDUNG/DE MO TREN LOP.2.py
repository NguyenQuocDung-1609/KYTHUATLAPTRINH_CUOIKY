str = 'Mã OTP của bạn là: 1357'
# Duyệt từng ký tự để tìm vị trí bắt đầu của số
for i in range(len(str)):
    if str[i].isdigit():      # nếu ký tự là chữ số đầu tiên
        chuoi_so = str[i:]    # cắt chuỗi từ đó trở đi
        break
giatri = float(chuoi_so)
print(giatri)
