import random

r = random.randint(1,100)

while True:
    n = int(input('請猜 1~100 之間的數字： '))
    if n == r:
        print('終於猜對了！')
        break
    elif n > r:
    	print('比答案大喔！再猜')
    else:
    	print('比答案小喔！再猜')
