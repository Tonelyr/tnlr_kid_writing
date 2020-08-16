print("Welcome to the KiD wRiTiNg Generator !")
print("11 characters max (for the moment)")


useript = input("Word to change: ")
str(useript)

length = (len(useript))


if length <= 1:
    print("There is nothing to transform")
elif length == 2:
    print(useript[:1] + useript[1].upper())
elif length == 3:
    print(useript[:1].lower() + useript[1].upper() + useript[2:].lower()) 
elif length == 4:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper())
elif length == 5:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper() + useript[4].lower())
elif length == 6:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper() + useript[4].lower() + useript[5].upper())
elif length == 7:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper() + useript[4].lower() + useript[5].upper() + useript[6].lower())
elif length == 8:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper() + useript[4].lower() + useript[5].upper() + useript[6].lower() + useript[7].upper())
elif length == 9:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper() + useript[4].lower() + useript[5].upper() + useript[6].lower() + useript[7].upper() + useript[8].lower())
elif length == 10:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper() + useript[4].lower() + useript[5].upper() + useript[6].lower() + useript[7].upper() + useript[8].lower() + useript[9].upper())
elif length == 11:
    print(useript[:1].lower() + useript[1].upper() + useript[2].lower() + useript[3].upper() + useript[4].lower() + useript[5].upper() + useript[6].lower() + useript[7].upper() + useript[8].lower() + useript[9].upper() + useript[10].lower())
else:
    print("Text too long ;-;")