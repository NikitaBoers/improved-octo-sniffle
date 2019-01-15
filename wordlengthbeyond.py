
with open('beyond_good_and_evil.txt') as file:
    beyond= ''
    for line in file:
        beyond= beyond + line

with open('jenseits_von_gut_und_boese.txt', encoding = 'utf8') as file:
    jenseits= ''
    for line in file:
        jenseits= jenseits + line

wordlist1=jenseits.strip().split(' ')
totallength1= 0
for i in wordlist1 :
   totallength1 =totallength1+len(i)
averagelength1=totallength1/ len(wordlist1)

combined_string1= "The average length of the words in Jenseits von Gut und Böse is "+str(averagelength1)
print(combined_string1)

wordlist2=beyond.strip().split(' ')
totallength2= 0
for i in wordlist2 :
   totallength2 =totallength2+len(i)
averagelength2=totallength2/ len(wordlist2)

combined_string2= "The average length of the words in Beyond Good and Evil is "+str(averagelength2)
print(combined_string2)

if averagelength1 >  averagelength2:
    print("Jenseits von Gut und Böse has words that are on avergae longer than Beyond Good and Evil")
elif averagelength1 == averagelength2:
    print('Jenseits von Gut und Böse and Beyond Good and Evil have words that, on average, are of equal length')
else :
    print("Beyond Good and Evil has words that are on avergae longer than Jenseits von Gut und Böse")
