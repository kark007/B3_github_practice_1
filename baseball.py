#打者判定システム

print('打席数と安打数を入力してください')
a,b = map(int,input().split())
batting_average = float(b/a)

if batting_average >= 0.3:
    print(f'打率{batting_average} 一流打者')
    
elif batting_average >= 0.28:
    print(f'打率{batting_average} 強打者')
    
elif batting_average >= 0.25:
    print(f'打率{batting_average} 一軍スタメン')
    
elif batting_average >= 0.2:
    print(f'打率{batting_average} 一軍控え')

else:
    print(f'打率{batting_average} 二軍で頑張ろう!')