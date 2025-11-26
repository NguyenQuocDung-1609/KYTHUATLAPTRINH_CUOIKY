fname = input("Enter the file name: ")
try:
    with open(fname, 'r', encoding='utf-8') as fh:
        total = 0.0
        count = 0
        for line in fh:
            line = line.rstrip()
            if line.startswith("X-DSPAM-Confidence:"):
                # Phân tách sau dấu ':' và chuyển thành float
                try:
                    num_str = line.split(":", 1)[1].strip()
                    num = float(num_str)
                except (IndexError, ValueError):
                    # Nếu không parse được, bỏ qua dòng đó
                    continue
                total += num
                count += 1
        if count > 0:
            print("Average spam confidence:{:.12f}".format( total / count))
        else:
            print("No 'X-DSPAM-Confidence' lines found.")
except FileNotFoundError:
    print("File not found:", fname)