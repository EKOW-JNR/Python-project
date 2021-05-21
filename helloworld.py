# print("hello world")
# a function to return a value
def get_initial(name):
    initial= name[0:1].upper()
    return initial


first_name= input('Enter your first name: ')
first_name_initial= get_initial(first_name)
last_name = input('enter your last name: ')
last_name_initial= get_initial(last_name)
print('your name is '+first_name+' '+last_name)
print('your initials are: '+first_name_initial+last_name_initial)



first_name.append( "jo")