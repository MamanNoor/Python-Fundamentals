temperature = 28
is_raining = False
is_weekend = True

print("condition 1:", temperature > 25 and is_weekend)
print("condition 2:", temperature < 20 or is_raining)
print("condition 3:", not is_raining)
print("condition 4:", temperature > 30 or is_weekend)
print("condition 5:", temperature > 25 and not is_raining)