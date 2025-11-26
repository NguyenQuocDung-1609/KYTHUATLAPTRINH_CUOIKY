# Dòng dữ liệu đầu vào
str_data = 'X-DSPAM-Confidence: 0.8475'

# 1. Tìm vị trí của ký tự ':' (dấu hai chấm)
# Ký tự ':' thường là điểm phân tách giữa nhãn và giá trị.
colon_pos = str_data.find(':') 
# Ví dụ: colon_pos sẽ là 18

# 2. Sử dụng string slicing để trích xuất phần chuỗi chứa số
# Ta bắt đầu cắt chuỗi từ vị trí ngay sau dấu hai chấm (colon_pos + 1)
# và đi đến cuối chuỗi.
# Lưu ý: Sách khuyên nên sử dụng lstrip() hoặc strip() sau khi cắt
# để loại bỏ khoảng trắng dư thừa, đảm bảo việc chuyển đổi số chính xác.
number_string = str_data[colon_pos + 1:].strip()
# 3. Chuyển đổi chuỗi số đã trích xuất thành số thực (float)
confidence_value = float(number_string)
# 4. In kết quả
print(f"Chuỗi đã trích xuất: '{number_string}'")
print(f"Giá trị số thực: {confidence_value}")
print(f"Kiểu dữ liệu: {type(confidence_value)}")