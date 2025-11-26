count = 0
total = 0
while True:
    value = input("Enter a number: ")
    if value == "done":
        break
    try:
        number = float(value)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + number
print(total, count, total / count)
    