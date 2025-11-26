str = 'X-DSPAM-Confidence:0.8475'
vi_tri = str.find(':')
chuoi_so = str[vi_tri + 1 :]
giatri = float(chuoi_so)
print(giatri)
