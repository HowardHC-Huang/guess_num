###猜數字遊戲###
#產生一個隨機整數1~100
#使用者重複輸入數字去猜
#猜對: 印出"終於猜對了!"
#猜錯: 印出比答案大/小
#延伸1: 印出猜了幾次
#延伸2: 使用者決定隨機數範圍

import random
rand_min = int(input('請決定隨機數的最小值:'))	#延伸2
rand_max = int(input('請決定隨機數的最大值:'))

answer = random.randint(rand_min, rand_max)
reply = int(input('請猜一個0~100的整數\n'))
count = 0		#延伸1:記錄次數要寫在循環外面
while True:
	#count = 0    [重要!!!]記錄次數如果寫在循環裡面,會每次都歸零,吃龜苓膏...
	count = count + 1
	if reply == answer:
		print('終於猜對了!')
		break
	elif reply > answer:
		print('猜太大了,  請再猜一次, 這是你猜的第', count, '次')
		reply = int(input())
	elif reply < answer:
		print('猜太小了,  請再猜一次, 這是你猜的第', count, '次')
		reply = int(input())