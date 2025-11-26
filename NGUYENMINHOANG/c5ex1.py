total = 0
count = 0

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try:
        number = float(inp)
        total = total + number   # cộng dồn vào tổng
        count = count + 1        # tăng số lượng lên 1
    except:
        print("Invalid input")

if count > 0:
    average = total / count
    print(total, count, average)