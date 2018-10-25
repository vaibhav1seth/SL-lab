class CusRev:
    def __init__(self,sentence):
       self.vowel_count=sum([1 if letter.lower() in ['a','e','i','o','u'] else 0 for letter in sentence])
       self.rev=list(reversed(sentence.split()))


c1=CusRev(input("Help me with the first string."))
c2=CusRev(input("Help me with the second string"))
c3=CusRev(input("Help me with the third string"))

print(sorted([(c.rev,c.vowel_count) for c in [c1,c2,c3]],key=lambda s:s[1],reverse=True))

