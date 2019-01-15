



filename = 'hamlet.txt'
with open(filename) as file:
    worddictionary = {}
    for line in file:
        split= line.strip().split()
        length=len(split)
        for i in range (length):
            lower=split[i].lower()
            if lower in worddictionary:
                worddictionary[lower] += 1
            else :
                worddictionary[lower] = 1
            
sorted_by_value = sorted(worddictionary.items(), key=lambda kv: kv[1])


max_value = max(worddictionary.values())
maxValKey = max(worddictionary, key=worddictionary.get)
listall = list(worddictionary.values())
listmax= listall[:]

print(sorted_by_value)
print(max_value)
print(maxValKey)
print(listmax)
'''
#from collections import Counter to count stuff
#worddictionary=Counter()
#for word in words:
 #   word= word.lower(    )
  #  worddictionary[word]+=1

worddictionary=Counter(words)

'''
