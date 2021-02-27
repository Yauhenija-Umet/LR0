name1 = 'Марина'
height1 = 1.70
weight1 = 61

name2 = 'Саня'
height2 = 1.70
weight2 = 70

name3 = 'Лена'
height3 = 1.70
weight3 = 75

def calculate_bmi(height, weight):
    return weight / height**2

def show_person_bmi(name, height, weight):
    bmi = calculate_bmi(height, weight)
    print('%s: индекс массы тела = %.2f' % (name, bmi))

def get_advice_on_bmi(bmi):
    if bmi <= 25:
        return 'может скушать пончик'
    else: 
        return 'пора садиться на диету'

def show_advice_on_bmi(name, height, weight):
    bmi = calculate_bmi(height, weight)
    advice = get_advice_on_bmi(bmi)
    print(f"{name} {advice}")

show_person_bmi(name1, height1, weight1)
show_advice_on_bmi(name1, height1, weight1)

show_person_bmi(name2, height2, weight2)
show_advice_on_bmi(name2, height2, weight2)

show_person_bmi(name3, height3, weight3)
show_advice_on_bmi(name3, height3, weight3)

