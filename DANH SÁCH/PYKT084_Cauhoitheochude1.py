
n = int(input())
a = []
for i in range(n):
    s = input()
    if s != " " and s != "":
        a.append(s)
    else:
        print(a[0] + ":",len(a)-1)
        a.clear()
print(a[0]+":",len(a)-1)



'''

13
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?
 
Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?

sa
asdfgh
asdf

'''