import operator

vowel = ['a','e','i','o','u','A','E','I','O','U']

class input_str:
    def __init__(self, sentence):
        self.sentence = sentence
        
    def count_vowel(self):
        mylist = self.sentence.split()
        count = 0
        for words in mylist:
            for letter in words:
                if letter in vowel:
                    count+=1
        return count
    
    def reverse_str(self):
        mylist = (self.sentence).split()
        list1 = reversed(mylist)
        return list1
        
str1 = input_str(input('Enter the first sentence: '))
str2 = input_str(input('Enter the second sentence: '))
str3 = input_str(input('Enter the third sentence: '))
count1 = str1.count_vowel()
count2 = str2.count_vowel()
count3 = str3.count_vowel()
ans1 = str1.reverse_str()
ans1_final = " ".join(ans1)
ans2 = str2.reverse_str()
ans2_final = " ".join(ans2)
ans3 = str3.reverse_str()
ans3_final = " ".join(ans3)

mydict={
    ans1_final: count1,
    ans2_final: count2,
    ans3_final: count3
}
mytup = sorted(mydict.items(), key = operator.itemgetter(1), reverse= True)
print(mytup)

