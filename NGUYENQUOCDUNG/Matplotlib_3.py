import matplotlib.pyplot as plt

# Dữ liệu mẫu
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [12, 18, 15, 22, 28, 25]  # Doanh thu bất kỳ

plt.figure(figsize=(10, 6))

# Biểu đồ cột
plt.bar(months, revenue, color='skyblue', label='Doanh thu (Bar)')

# Tính vị trí giữa cột
mid_revenue = [r/2 for r in revenue]

# Vẽ dấu chấm ở giữa cột
plt.scatter(months, mid_revenue, color='red', s=60, label='Điểm giữa cột')

# Vẽ đường nối các điểm giữa cột
plt.plot(months, mid_revenue, color='red', linewidth=2)

# Nhãn và tiêu đề
plt.xlabel("Tháng")
plt.ylabel("Doanh thu (triệu VND)")
plt.title("Biểu đồ doanh thu 6 tháng đầu năm")

plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
