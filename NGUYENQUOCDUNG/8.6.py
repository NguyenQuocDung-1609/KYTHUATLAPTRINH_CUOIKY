# Tạo 1 list rỗng để lưu các số người dùng nhập vào
numbers = []
while True:
    # Yêu cầu người dùng nhập số
    num = input("Enter a number: ")
    # Nếu người dùng nhập 'done' thì dừng vòng lặp
    if num == "Done":
        break
    # Chuyển chuỗi nhập vào thành số (dạng float để tính được số thập phân)
    value = float(num)
    # Thêm số đó vào danh sách
    numbers.append(value)
# Dùng hàm max() và min() để tìm giá trị lớn nhất và nhỏ nhất
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
