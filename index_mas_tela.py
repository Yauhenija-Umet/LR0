name1 = 'Марина'
h1 = 1.70
w1 = 61

name2 = 'Саня'
h2 = 1.70
w2 = 70

name3 = 'Лена'
h3 = 1.70
w3 = 75

def bmi_calculator(name, h,w):
	bmi = w/(h**2)
	print(name + ": Индекс массы тела = " + str(bmi))
	if bmi<=25:
		return name + " может скушать пончик"
	else:
		return name + " пора садиться на диету"

bmi1 = bmi_calculator(name1, h1, w1)
bmi2 = bmi_calculator(name2, h2, w2)
bmi3 = bmi_calculator(name3, h3, w3)

print(bmi1)
print(bmi2)
print(bmi3)
