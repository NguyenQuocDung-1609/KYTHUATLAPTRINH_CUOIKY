# Exercise 4
width = 17
height = 12.0

expressions = [
    ("width // 2", width // 2),
    ("width / 2.0", width / 2.0),
    ("height / 3", height / 3),
    ("1 + 2 * 5", 1 + 2 * 5)
]

for expr, value in expressions:
    print(expr, "=", value, ", type:", type(value))
