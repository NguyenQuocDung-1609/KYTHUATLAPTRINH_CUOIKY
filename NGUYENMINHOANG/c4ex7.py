def computergrade (score):
    if score < 0.0 or score > 1.0:
        print(' Error')
    else:
        if score>= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('c')
        elif score >= 0.6:
            print('D')
        else:
            return 'F'
diem = float (input(' enter score:'))
score = float (diem)
print(' Enter score:', score)
lop=computergrade(score )
print ( lop)