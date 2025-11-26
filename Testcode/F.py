# Dòng dữ liệu đầu vào
my_string = "Hello World! Python for Everybody."

# 1. Chuyển thành chữ thường
lower_string = my_string.lower()
print(f"1. Chữ thường: {lower_string}")

# 2. Kiểm tra kết thúc bằng '!'
ends_with_exclamation = my_string.endswith('!')
print(f"2. Kết thúc bằng '!'? {ends_with_exclamation}")

# 3. Thay thế 'o' bằng '@'
replaced_string = my_string.replace('o', '@')
print(f"3. Thay thế 'o' bằng '@': {replaced_string}")