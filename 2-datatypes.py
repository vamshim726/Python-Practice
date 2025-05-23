#datatypes
'''
   numeric types:  int, float, complex, 
    it stores sinle values

    sequence types: list , string, tuple
    it stores multiple values of mutiple types in single variable



    boolean  , dictionary ,set

  
      
    num1=list()   == it creates empty list

    tuple == it enclosed in ( )
    nums2=()   == it create empty tuple

    string== collection of mutipe characters

    set ={10,20}
    - it stores mutiple values,
    - unordered 
    - duplicates not allowed
    -  if we take duplicates also it consider 1 times


    dict() == create empty dictionary

'''
nums =[10,20,30,[1,2],True,3.5,"a","hi"]


print(nums, type(nums))


nums_tuple=(10,20,30)
print(nums_tuple)


nums_dictionary={"m1":10,"m2":20,"m3":30}
nums_dictionary["m2"]=50
nums_dictionary.update({"m4":80})
nums_dictionary.pop("m2")
print(nums_dictionary)




#list
l1=[10,20,"hi",True,(1,3)]
l2=list()

#tuple

t1=(1,2,3)
t2=()

#set

s1={10,3,4,3,True,"hi"}
s1=set()

#dict

d1={"m1":10,"m2":20}
d2=dict()




