# 5단 구구단

dan = 5
for i in range(1, 10):
    #print(str(dan) + 'x' + str(i) + '=' + str(dan *i))
    #print(dan,'x',i,'=',dan*i)
    #print(f'{dan}*{i}={dan*i}') #f'': format의 약자, 문자 서식을 줄때 사용하면 좋음.
    mul = f'{dan}*{i}={dan*i}'
    print(mul)