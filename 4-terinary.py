'''
its a short end form of if else



'''

#num is postive or not

num=50
print( "zero" if num==0 else "negitive" if num<0 else "positive")



letter="9"
print("capital" if letter>="A" and letter<="Z"  else "small" if letter>="a" and letter<="z" else "special char")


n1=2
print("div by both 3 and 5" if n1%3==0 and n1%5==0 else " div by 3" if n1%3==0 else "div by 5" if n1%5==0 else "not by both 3 5")


#print negitvie if neg num or print single dit, 2 digit, 3 digit, 3 or more

num1="10"

if int(num1)>=0:
    c=0
    for i in num1:
        c+=1
    print("1 digit" if c==1 else "2 digit" if c==2 else "3 digit" if c==3 else "more than 3 digits")
else:
    print("negitive num")