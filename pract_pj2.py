

def func_check_weight(*,age: int,height: int):
    if age <= 30:
        norm_weight_range = height - 110
    elif age >=30 and age <= 50:
        norm_weight_range = height - 100
    elif age  >= 50:
        norm_weight_range = height - 90
    return 'грубая норма веса в %i и при росте %i равна %i' % (age,height,norm_weight_range)

try:

    while True:
        age_input = int(input('input age >'))
        height_input = int(input('input height >'))

        if age_input > 18 and height_input > 155:
            print(func_check_weight(age=age_input,height=height_input))
        else:
            print('invalid data user input(min 18 age and height min 155) you input - age:%i height:%i' % (age_input,height_input))
except KeyboardInterrupt:
    pass
