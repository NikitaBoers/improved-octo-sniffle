
with open('hamlet.txt') as file:
    whole_text= ''
    for line in file:
        whole_text= whole_text + line

print(whole_text)
