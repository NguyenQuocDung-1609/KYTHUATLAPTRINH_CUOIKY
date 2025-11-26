# shout.py
fname = input("Enter a file name: ")

# Mở file
fhand = open(fname)

# Đọc và in từng dòng ở dạng in hoa
for line in fhand:
    line = line.rstrip()
    print(line.upper())
