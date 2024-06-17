import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
Question Number 1:
Created a new array using np.array, performed sum, average, min and max upon the array using the .sum , .max , .min, .mean method provided by numpy.

a = np.array([1,2,3,4,5])
print(f"Their Sum is: {np.sum(a)}, Their Average is {np.mean(a)} and their max and min values are {np.max(a)}, {np.min(a)} respectively.")
'''

'''
Question No 2: 
used list comprehension, .split function and type casting to take any number of user inputs, sorted it with the sorted function and index'ed it in the f-string.

sorted_user_inputs = sorted([int(x) for x in input("Enter any number of numbers you'd like seperated by commas (,): ").split(',')]) 
print(f"Elements between 2-5: {sorted_user_inputs[2:6]}, between 5-8: {sorted_user_inputs[5:9]}, between 2-9: {sorted_user_inputs[2:9]}")  

'''

'''
Question No 3:
Generated a random array using np.random.randint, sorted it using np.sort, and reshaped it using .reshape method

print(f"Reshaped matrix:\n{np.sort(np.random.randint(2, 100, size=12)).reshape(3,4)}") 
'''

'''
Question Number 4:
Used List Comprehension to Input the matrices, Used lambda functions to validate the matrice's size for addition/substraction, multiplication and used python's new match case statement to conditionally either multiply or add and substract or both.
try:
    matrix_a = np.array([[int(x) for x in input(f"Enter values separated by commas for row {i+1}: ").split(',')]\
        for i in range(int(input("Enter the number of rows you want the matrix_1 to have: ")))])
    matrix_b = np.array([[int(x) for x in input(f"Enter values separated by commas for row {i+1}: ").split(',')]\
        for i in range(int(input("Enter the number of rows you want the matrix_2 to have: ")))])
    validate_add_sub, validate_mul = lambda m1, m2: m1.shape == m2.shape, lambda m1,m2: m1.shape[1] == m2.shape[0]
    match (validate_add_sub(matrix_a, matrix_b), validate_mul(matrix_a, matrix_b)):
        case (True, False):  # Addition and subtraction only
            print("--- Matrice's Dimensions Only Support Addition And Substraction --- ")
            print(f"Adding:\n{matrix_a}\nand\n{matrix_b}\ngives:\n{matrix_a + matrix_b}")
            print(f"Subtracting:\n{matrix_a}\nand\n{matrix_b}\ngives:\n{matrix_a - matrix_b}")
        case (False, True):  # Multiplication only
            print("--- Matrice's Dimensions Only Support Multiplication --- ")
            print(f"Multiplying:\n{matrix_a}\nand\n{matrix_b}\ngives:\n{np.dot(matrix_a, matrix_b)}")
        case (True, True):   # Both addition/subtraction and multiplication
            print("--- Matrice's Dimensions Support All Addition, Substraction And Multiplication --- ")
            print(f"Adding:\n{matrix_a}\nand\n{matrix_b}\ngives:\n{matrix_a + matrix_b}")
            print(f"Subtracting:\n{matrix_a}\nand\n{matrix_b}\ngives:\n{matrix_a - matrix_b}")
            print(f"Multiplying:\n{matrix_a}\nand\n{matrix_b}\ngives:\n{np.dot(matrix_a, matrix_b)}")
        case (_, _):
            print("Matrices cannot be added/subtracted or multiplied due to incompatible dimensions.")
except:
    print("Invalid Matrix Dimensions Please Enter Again: ")
'''

'''
Question 5:
Read csv From Pandas, Plotted Figure Using MatlibPlot

data = pd.read_csv('weight_height.csv')

# Scatter Plot For Weight x Height
plt.figure(figsize=(10, 6))
plt.scatter(data['Weight'], data['Height'], c='blue', label='Weight vs Height')
plt.xlabel('Weight (Kgs)')
plt.ylabel('Height (meters)')
plt.title('Scatter Plot: Weight vs Height')
plt.grid(True)
# plt.show() # didn't work on mine as interactive mode for displaying plot's isnt enabled.
plt.savefig('Question 6/weight_vs_height')

# Scatter Plot For Age x Weight
plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['Weight'], c='blue', label='Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight (Kgs)')
plt.title('Scatter Plot: Age vs Weight')
plt.grid(True)
# plt.show() # didn't work on mine as interactive mode for displaying plot's isnt enabled.
plt.savefig('Question 6/age_vs_weight')


# Scatter Plot For Height x Age
plt.figure(figsize=(10, 6))
plt.scatter(data['Height'], data['Age'], c='blue', label='Height vs Age')
plt.xlabel('Height (meters)')
plt.ylabel('Age')
plt.title('Scatter Plot: Height vs Age')
plt.grid(True)
# plt.show() # didn't work on mine as interactive mode for displaying plot's isnt enabled.
plt.savefig('Question 6/height_vs_age')

# Scatter Plot For Gender x Height
plt.figure(figsize=(10, 6))
plt.scatter(data['Gender'], data['Height'], c='blue', label='Gender vs Height')
plt.xlabel('Gender')
plt.ylabel('Height (meters)')
plt.title('Scatter Plot: Gender vs Height')
plt.grid(True)
# plt.show() # didn't work on mine as interactive mode for displaying plot's isnt enabled.
plt.savefig('Question 6/gender_vs_height')

# Scatter Plot For Gender x Weight
plt.figure(figsize=(10, 6))
plt.scatter(data['Gender'], data['Weight'], c='blue', label='Gender vs Weight')
plt.xlabel('Gender')
plt.ylabel('Weight (Kgs)')
plt.title('Scatter Plot: Gender vs Weight')
plt.grid(True)
# plt.show() # didn't work on mine as interactive mode for displaying plot's isnt enabled.
plt.savefig('Question 6/gender_vs_weight')
'''

'''
Question 6:

df = pd.read_csv('weight_height.csv')
df['BMI'] = (df['Weight'] / df['Height']).round(2)

def determine_risk(bmi):
    if bmi < 18.5:
        return 'Nutrient deficient'
    elif 18.5 <= bmi <= 24.9:
        return 'Lower risk'
    elif 25 <= bmi <= 29.9:
        return 'Heart disease risk'
    elif 30 <= bmi <= 34.9:
        return 'Higher risk of diabetes, Heart disease risk'
    else:
        return 'Serious health condition risk'

df['Risk'] = df['BMI'].apply(determine_risk)

print(df)
'''
