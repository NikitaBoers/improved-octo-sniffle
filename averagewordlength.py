sentence=input('Write a sentence of at least 10 words: ')
wordlist= sentence.strip().split(' ')
for i in wordlist:
    print(i)

totallength= 0
for i in wordlist :
   totallength =totallength+len(i)
averagelength=totallength/ len(wordlist)

combined_string= "The average length of the words in this sentence is "+str(averagelength)
print(combined_string)

