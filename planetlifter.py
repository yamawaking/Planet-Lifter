import numpy as np

def weight_adjustment(ex, raw_weight, add_weight):
    if ex == "weight training":
        adjust_weight = raw_weight
    elif ex == "dips":
        adjust_weight = raw_weight * 0.8 + add_weight
    elif ex == "push up":
        adjust_weight = raw_weight * 2/3 + add_weight
    return adjust_weight

def calculate_intensity(ex, raw_weight, count, add_weight):
    adj_weight = weight_adjustment(ex, raw_weight, add_weight)
    intensity = adj_weight * count
    return intensity

ex1 = "weight training"
raw_weight1 = 50
count1 = 10
add_weight1 = 0

ex2 = "push up"
raw_weight2 = 70
count2 = 30
add_weight2 = 0

ex3 = "dips"
raw_weight3 = 70
count3 = 5
add_weight3 = 30

intensity1 = calculate_intensity(ex1, raw_weight1, count1, add_weight1)
intensity2 = calculate_intensity(ex2, raw_weight2, count2, add_weight2)
intensity3 = calculate_intensity(ex3, raw_weight3, count3, add_weight3)

list_intensity = [intensity1, intensity2, intensity3]
session_intensity = sum(list_intensity)

print(f"the intensity of this session is {session_intensity}")
