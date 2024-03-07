import math
 
def equationroots(a,b,c):
	dis = b*b -4 *a *c 
	sqrt_value = math.sqrt(abs(dis))

	if dis > 0:
		print("Real and differnt root")
		print((-b + sqrt_value)/(2 * a))
		print((-b - sqrt_value)/(2 * a))
	elif dis == 0:
		print("real and same roots")
		print(-b / (2 * a))
	else :
		print("Complex roots")
		print(-b /(2 * a), +i,sqrt_value)
		print(-b /(2 * a), -i,sqrt_value)
	

a = 1 
b = 10
c = -24
if a == 0:
	print("Input correct quadration equation")
else:
	equationroots (a,b,c)
