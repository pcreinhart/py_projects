#F-strings provide a way to embed expressions inside 
# string literals, using a minimal syntax. 
# It should be noted that an f-string is really 
# an expression evaluated at run time, not a constant value. 
# In Python source code, an f-string is a literal string, prefixed 
# with 'f', which contains expressions inside braces.

types_of_vegetables = 456
types_of_berries= 24
print (types_of_berries - types_of_vegetables)
print (f"Berries minus vegetables equals {types_of_berries - types_of_vegetables} sorta kinda maybe ")
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"thos who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"Isaid:{x}")
print(f"I also said:'{y}''")
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w="This is the let side of...."
e="a string with a right side"
print (w+e)


