file_name = input("Enter the file name: ").strip()
if file_name == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            count = 0
            for line in f:
                if line.startswith("Subject:"):
                    count += 1
            print(f"There were {count} subject lines in {file_name}")
    except FileNotFoundError:
        print(f"File cannot be opened: {file_name}")