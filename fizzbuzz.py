for i in range(1,15+1):
    if i % 3 == 0 or i % 5 ==0:
        print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0))
    else :
        print(i)
