from give_bmi import give_bmi, apply_limit

# Test without errors
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# Test with errors
# height_error = [2.71, 1.15]
# weight_error_1 = [165.3, 38.4, 12]
# weight_error_2 = [165.3, "38.4"]
# bmi_error_1 = give_bmi(height_error, weight_error_1)
# bmi_error_2 = give_bmi(height_error, weight_error_2)
