
with open('hamlet.txt') as file:
    hamlet= ''
    for line in file:
        hamlet= hamlet + line

wordlist=hamlet.strip().split(' ')
totallength= 0
for i in wordlist :
   totallength =totallength+len(i)
averagelength=totallength/ len(wordlist)

combined_string= "The average length of the words in Hamlet is "+str(averagelength)
print(combined_string)

