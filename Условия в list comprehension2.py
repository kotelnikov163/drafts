fruit_yields = [164.8, 105.0, 124.3, 113.8] 
# Присвоить новому элементу значение yield_value, ЕСЛИ yield_value > 120. 
new_yields = [yield_value for yield_value in fruit_yields if yield_value > 120]

print(new_yields)