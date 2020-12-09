print("Welcome to the KiD wRiTiNg Generator !") 

userinput = input("Word to change: ")

new_input = ""

capital_letter = False

for i in userinput:
    if not capital_letter:
        new_input += i.upper()
        capital_letter = True
    else:
        new_input += i
        capital_letter = False  
print(new_input)
