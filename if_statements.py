# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))


if age == 100:
    print('You are old!')
elif age >= 18:
    print('you are an adult!')
elif age < 0:
    print('Not even born!')
else:
    print('You are a child!')