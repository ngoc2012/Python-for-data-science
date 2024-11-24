from give_bmi import give_bmi, apply_limit


weight = [165.3, 38.4]
height = [2.71]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, 0]
bmi = give_bmi(height, weight)
height = [2.71, -1]
bmi = give_bmi(height, weight)
height = [2.71, "smt"]
bmi = give_bmi(height, weight)
height = [2.71, None]
bmi = give_bmi(height, weight)
height = [2.71, 1.15]
weight = [165.3]
bmi = give_bmi(height, weight)
weight = [165.3, 0]
bmi = give_bmi(height, weight)
weight = [165.3, -1]
bmi = give_bmi(height, weight)
weight = [165.3, None]
bmi = give_bmi(height, weight)
weight = [165.3,"smt"]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
