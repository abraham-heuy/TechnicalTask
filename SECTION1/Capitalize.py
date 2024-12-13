#Algorithm to capitalize the first letter of a string.
#Create a function that handles the capitalization.
 
def capitalize_first_letter(input_string):
    capitalized_string = ' '.join(word.capitalize() for word in input_string.split())
    return capitalized_string

#print some of the examples: 
print(capitalize_first_letter("hi"))#pass some input as input_string
print(capitalize_first_letter("i love programming"))