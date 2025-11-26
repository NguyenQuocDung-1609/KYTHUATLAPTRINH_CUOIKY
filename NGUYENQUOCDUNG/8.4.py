# Nhập tên file
fname = input("Enter file name: ")

# Mở file để đọc
fhand = open(fname)

# Tạo 1 list rỗng để lưu các từ
words = []

# Đọc từng dòng trong file
for line in fhand:
    # Tách dòng thành danh sách các từ
    pieces = line.split()
    
    # Duyệt từng từ trong dòng
    for word in pieces:
        # Nếu từ chưa có trong list thì thêm vào
        if word not in words:
            words.append(word)

# Sắp xếp danh sách theo thứ tự bảng chữ cái
words.sort()

# In ra kết quả
print(words)
