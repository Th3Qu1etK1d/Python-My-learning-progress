# while loop = statement that will execute it's block of code
#                     as long it's condition remains true

#name = None

#while not name:
    #name = input("Enter your name: ")

#print('Hello '+name)

#______________________________________________________________

# for loop = a statement that will execute it's block of code 
# a limited amount of times 
#                               while loop = unlimited                            
#                               for loop = limited

#for i in range(10):
    #print(i+1)

#for i in range(50,100+1,2):
    #print(i)

#for i in 'Hugo Pelletier':
    #print(i)

#import time 

#for minute in range(10,0,-1):
    #print(minute)
    #time.sleep(10)
#print('happy new year')

#____________________________________________________________________________

# nested loops = The "inner loop" will finish all of it's iterations before 
#                finishing one iterration of the "outer loop"

#rows = int(input('how many rows?: '))
#columns = int(input('how many colums?: '))
#symbol = input('enter a symbol to use: ')

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()

#____________________________________________________________________________

# loop control statement = change a loops execution from it's normal sequence

# break = used to terminate the loop
# continue = skips t othe next iteration of the loop
# pass = nothing, placeholder

#while True:
    #name = input("Enter your name:")
    #if name != "":
        #break

#phone_number = "984-143-4324"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

#for i in range(1,21):

    #if i == 13:
        #pass
    #else:
        #print(i)
     