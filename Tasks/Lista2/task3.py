# Lesson2, Task3

num = 1
nextNum = num / 2

while nextNum > 0:
	num = nextNum
	nextNum = num / 2
	
print ("Machine precision in Python equals to {:e}.".format(num))