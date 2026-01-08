#this program teaches basic python commands
print("this is my first python lesson")
print("you acheive this with command 'print' and entering text in parenthesis and double inverted commas")
name=input("What is your name?")

#while True loop (just while loop is also a thing, couldint figure out where it would fit in this program)
while True: 
    age=(input("What is your age?"))
    try:
        age=int(age)
        break
    except:
        print('That is not a valid number')

'''print("Name:", name,'\n',"Age:",age,'\n',name, " you are ", age, " years old!",sep='')'''

print ("Name:", name)
print("Age:", age)
print("Hello", name, "you are", age, "years old")

#Conditional statement
if age>=19:
    print('You are officially an adult')
elif 12<age<20:
    print('you are in your TEENS')
else:
    print('hello kids!')

if age<20:
    Is_Happy= True
    if Is_Happy:
        print('You are happy')
else:
    print('You pretend to be happy')

print('other people your age are:')

#for loop
name_list=['shabada', 'dabada']
for x in name_list:
    print(x)

#function
def h(name):
    print('Hey there,' , name)
h('shabada')
h('dabada')
h(name)

# math in python
a=10
b=5
add= a+b
subtraction= a-b
multiply= a*b
division= a/b
power= a**b
print(add)
print(subtraction)
print(multiply)
print(division)
print(power)

