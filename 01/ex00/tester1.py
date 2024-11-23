from give_bmi import give_bmi, apply_limit


weight = [165.3, 38.4]
height = [2.71]
bmi = give_bmi(height, weight)
height = [2.71, 0]
bmi = give_bmi(height, weight)
height = [2.71, -1]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
