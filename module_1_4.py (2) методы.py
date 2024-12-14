my_string = input("Ваше имя: ")
print(len(my_string))
print(my_string.upper())
print(my_string.upper().lower())
my_string = my_string.replace(" ", "")
print(my_string)
if my_string:
    print(my_string[0])
if my_string:
    print(my_string[-1])
