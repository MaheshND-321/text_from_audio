text = 'Ramanujan spoke about black holes nearly 100 years or more than hundred years ago there was no concept of black mathematics for black holes when there was no concept of Black Hole science always progress is like this but the concept then the theory and then the mathematics but he made the mathematics first before before their eyes when they are and still more in our mathematics notebooks and netbooks mathematics sim ki foreigner my baby please mathematics'
count=0
maxcount = 0
l=[]
words = words=text.split()
for i in range(len(words)):
    for j in range(len(words)):
        if(words[i]==words[j]):        #finding count of each word
            count+=1
        else:
            count=count
        if(count==maxcount):          #comparing with maximum count
            l.append(words[i])
        elif(count>maxcount):         #if count greater than maxcount
            l.clear()
            l.append(words[i])
            maxcount=count
        else:
            l=l
        count=0
print(l)                              #printing contents of l