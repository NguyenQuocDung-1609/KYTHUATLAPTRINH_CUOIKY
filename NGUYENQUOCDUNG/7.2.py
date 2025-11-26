# Exercise 2 - spam confidence average

fname = input("Enter a file name: ")
fhand = open(fname)

count = 0
total = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(':')
        number = float(line[pos+1:].strip())
        count = count + 1
        total = total + number

average = total / count
print("Average spam confidence:", average)
