chuoi = 'X-DSPAM-Confidence:0.8475'
vi_tri_dau_2cham = chuoi.find(':')
chuoi_so = chuoi[vi_tri_dau_2cham+1:]
so_thuc = float(chuoi_so)
print(so_thuc)
