
ten_tap_tin = input("Nhập tên tệp: ")
danh_sach_tu = []
try:
    with open(ten_tap_tin) as tap_tin:
        for dong in tap_tin:
            cac_tu = dong.split()
            for tu in cac_tu:
                if tu not in danh_sach_tu:
                    danh_sach_tu.append(tu)
    danh_sach_tu.sort()
    print(danh_sach_tu)
except FileNotFoundError:
    print("Không tìm thấy tệp:", ten_tap_tin)