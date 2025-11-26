# Python for Everybody - Chapter 7 Exercises

# ---------------------------
# Exercise 1: Print file content in uppercase
# ---------------------------

def exercise1():
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        return

    for line in fhand:
        line = line.rstrip()
        print(line.upper())


# ---------------------------
# Exercise 2: Compute average spam confidence
# ---------------------------

def exercise2():
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        return

    count = 0
    total = 0.0

    for line in fhand:
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        value = float(line[line.find(':') + 1:])
        total += value
        count += 1

    if count > 0:
        print('Average spam confidence:', total / count)
    else:
        print('No spam confidence lines found.')


# ---------------------------
# Exercise 3: Easter Egg
# ---------------------------

def exercise3():
    fname = input('Enter the file name: ')

    if fname.lower() == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        return

    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        return

    count = 0
    for line in fhand:
        if line.startswith('Subject:'):
            count += 1
    print('There were', count, 'subject lines in', fname)


# ---------------------------
# Main menu to select exercise
# ---------------------------

def main():
    print("Python for Everybody - Chapter 7 Exercises")
    print("1. Print file content in uppercase")
    print("2. Compute average spam confidence")
    print("3. Easter Egg message")
    choice = input("Choose an exercise (1-3): ")

    if choice == '1':
        exercise1()
    elif choice == '2':
        exercise2()
    elif choice == '3':
        exercise3()
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
