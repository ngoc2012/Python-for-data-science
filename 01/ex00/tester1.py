from give_bmi import give_bmi, apply_limit


weight = [165.3, 38.4]
height = [2.71]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, 0]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, -1]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, "smt"]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, None]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, 1.15]
weight = [165.3]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3, 0]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3, -1]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3, None]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3,"smt"]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
try:
    print(apply_limit(bmi, []))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, [None]))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, None))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, -1))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, 0))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, "hello"))
except Exception as e:
    print(e)
