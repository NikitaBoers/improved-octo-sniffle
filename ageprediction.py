
birthyear = int(input('Enter birthyear: '))
yearinput = int(input('Enter year: '))

if birthyear< yearinput:
    age = yearinput - birthyear 
    combined_string= 'in'+str(yearinput)+'you will be'+str(age)+'years old'
    print (combined_string)
elif birthyear > yearinput:
    print ('you were not born yet :(')
else :
    print('this is the year you were born')



