
fname = input("Enter a file name: ")
try:
    with open(fname) as f:
        for line in f:
            print(line.rstrip().upper())
except FileNotFoundError:
    print("File not found:", fname)