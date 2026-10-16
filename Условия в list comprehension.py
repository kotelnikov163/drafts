fruit_yields = [164.8, 105.0, 124.3, 113.8] 
corrected_fruit_yields = [yield_value + 1.2 if yield_value < 120 else yield_value for yield_value in fruit_yields]
#                         |- - - -           Тернарный оператор          - - - -|
print(corrected_fruit_yields)