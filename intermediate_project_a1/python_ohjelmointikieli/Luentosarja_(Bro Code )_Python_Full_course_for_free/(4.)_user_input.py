"""
New in this Lecture
input() Function. 

variable_a = input() <- Saves given input in to the variable_a 
The data type of input() is string by default


"""

monomial = input("Please insert monomial of polynomial, for example 3x^2: ")

numerals_of_monomial = [int(monomial[0]), int(monomial[3])]

co_efficiant = numerals_of_monomial[0] * numerals_of_monomial[1]
exponent = numerals_of_monomial[1] - 1

derivative = str(co_efficiant) + "x" + "^" + str(exponent)

print(f"Derivative of {monomial} is {derivative}")


