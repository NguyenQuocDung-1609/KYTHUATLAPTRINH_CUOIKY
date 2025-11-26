# Nhập tên file
fname = input("Enter file name: ")

# Mở file
fhand = open(fname)

# Biến đếm số dòng bắt đầu bằng "From"
count = 0

# Đọc từng dòng trong file
for line in fhand:
    # Loại bỏ khoảng trắng ở đầu/cuối dòng
    line = line.strip()

    # Bỏ qua dòng không bắt đầu bằng "From "
    if not line.startswith("From "):
        continue

    # Tách dòng thành các từ
    words = line.split()

    # In từ thứ hai (địa chỉ email)
    print(words[1])

    # Tăng biến đếm
    count = count + 1

# In ra tổng số dòng "From"
print("There were", count, "lines in the file with From as the first word")
