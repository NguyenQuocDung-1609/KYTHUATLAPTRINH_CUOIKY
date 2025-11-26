max = None
min = None
while True:
    value = input("Enter a number: ")
    if value == "done":
        break
    try:
        number = float(value)
    except:
        print("Invalid input")
        continue
    if max is None or number > max:
        max = number
    if min is None or number < min:
        min = number
print("Maximum:", max)
print("Minimum:", min)
