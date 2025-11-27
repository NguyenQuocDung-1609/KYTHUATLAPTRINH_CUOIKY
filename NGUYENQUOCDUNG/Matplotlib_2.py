import numpy as np
import matplotlib.pyplot as plt

# Tạo miền giá trị x từ -10 tới 10
x = np.linspace(-10, 10, 400)

# Với hàm căn x, chỉ lấy x >= 0
x_sqrt = np.linspace(0, 10, 200)
y3 = np.sqrt(x_sqrt)

# Vẽ đồ thị
plt.plot(x, x**2, label='y = x^2')
plt.plot(x, x**3, label='y = x^3')
plt.plot(x_sqrt, y3, label='y = √x')

# Nhãn và tiêu đề
plt.xlabel("Giá trị x")
plt.ylabel("Giá trị y")
plt.title("Đồ thị các hàm số y = x^2, y = x^3 và y = √x")

# Hiển thị chú thích
plt.legend()

# Hiển thị lưới
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
