str_data = 'X-DSPAM-Confidence: 0.8475'
colon_pos = str_data.find(':') 
number_string = str_data[colon_pos + 1:].strip()
confidence_value = float(number_string)
print(f"Chuỗi đã trích xuất: '{number_string}'")
print(f"Giá trị số thực: {confidence_value}")
print(f"Kiểu dữ liệu: {type(confidence_value)}")