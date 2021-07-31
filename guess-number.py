import random

start = input ('請決定隨機數字範圍開始值：')
end = input ('請決定隨機數字範圍結束值：')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1
    n = input('請猜'+str(start)+'～'+str(end)+'之間的數字： ')
    n = int(n)
    if n == r:
        print('終於猜對了！')
        break
    elif n > r:
    	print('比答案大喔！再猜')
    else:
    	print('比答案小喔！再猜')
print('你總共猜了', count, '次！')
