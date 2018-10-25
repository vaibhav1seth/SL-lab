from functools import reduce
import operator
words=dict()
with open('myfile.txt','rb') as file:
    for word in (word for line in file for word in line.split()):
        if word in words:
            words[word]+=1
        else:
            words[word]=1

words=dict(sorted(words.items(),key=lambda x:x[1],reverse=True))

# top 10 words with most number of occurrences in descending order
print('Top 10 words with most occurences',list(words.keys())[:10])

#one-line reduce function to get the average length
print('Average Length',reduce(lambda x,y:x+y,words.values())/(len(words.values())))

#one-line list comprehension to display squares of all odd numbers
print('Squares of ODD numbers',[x*x for x in range(1,100,2)])
