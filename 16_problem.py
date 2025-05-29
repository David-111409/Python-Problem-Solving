def calculate_years(human_years):
    
    return [
        human_years, 
            15 * (human_years >= 1) + 9 * (human_years >= 2) + 4 * (human_years - 2) * (human_years > 2),
            15 * (human_years >= 1) + 9 * (human_years >= 2) + 5 * (human_years - 2) * (human_years > 2)
            ]
    
    


print(calculate_years(1), [1,15,15])
print(calculate_years(2), [2,24,24])
print(calculate_years(10), [10,56,64])
print(calculate_years(20)== [20,96,114])
print(calculate_years(65)== [65,276,339])
print(calculate_years(43)== [43,188,229])
print(calculate_years(100), [100,416,514])

'''
Human, Cat and Dog Years 🧑🏻🐱🐶
Mubashir has a cat and a dog. He purchased both of them at the same time human_years ago.

Create a function which takes an argument of human_years and returns [human_years, cat_years, dog_years] list.

Human Years
Human Years >= 1
Human Years are whole numbers only.
Cat Years
15 cat years for first year.
+9 cat years for second year.
+4 cat years for each year after that.
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
Examples
calculate_years(1) ➞ [1, 15, 15]

calculate_years(2) ➞ [2, 24, 24]

calculate_years(10) ➞ [10, 56, 64]
'''
