###猜數字遊戲###
#產生一個隨機整數1~100
#使用者重複輸入數字去猜
#猜對: 印出"終於猜對了!"
#猜錯: 印出比答案大/小

import random

answer = random.randint(1, 100)

reply = int(input('請猜一個0~100的整數\n'))
while True:
	if reply == answer:
		print('終於猜對了!')
		break
	elif reply > answer:
		reply = int(input('猜太大了, 請再猜一次\n'))
	elif reply < answer:
		reply = int(input('猜太小了, 請再猜一次\n'))