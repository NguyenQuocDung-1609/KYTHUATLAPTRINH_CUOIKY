lst=[]
while True:
    nhapso= input('Enter a number:')
    if nhapso=='done':
        break
    try:
        so= float(nhapso)
        lst.append(nhapso)
    except:
        print('ERROR')
lonnhat= max(lst)
nhonhat= min(lst)
print('Maximum:',lonnhat)
print('Minimun:',nhonhat)