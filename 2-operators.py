
'''

arithmetic operators
+, -, *, /, //, ** 


modulus %

n%d = ans

if n>d ==> n%d
or
n<d ==>n



'''
n1=10
n2=20

print("addition",n1+n2)
print("differnce",n1-n2)
print("mutiply",n1*n2)
print("division",n1/n2)
print("remainder",n1%n2)
print("floor division",n1//n2)
print("power",n1**n2)




'''

relational / comparision operators

>,>=, , <= , !=


'''

print("greater :",(n1>n2))
print("greater than or  equal:",(n1>=n2))
print("greater :",(n1>n2))
print("less than or  equal:",(n1<=n2))
print("lesthan :",(n1<n2))
print("==:",(n1==n2))



'''

logical operators

    and

    or

    not

'''


# alphabet or not program

alpha="5"

if alpha >= "A" and alpha <="Z" or alpha >= "a" and alpha <="z":
    print("alphabet")
else:
    print("not alphabet")


#num even or not

num1=10
print("even" if num1%2 ==0 else "not even")

#is given input not aplphabet

alpha="#"

res= alpha >= "A" and alpha <="Z" or alpha >= "a" and alpha <="z"
print( not res)