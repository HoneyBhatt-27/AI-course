"""
File:
Project:
Author:
Version:
Release:
"""

#sequentil datatype

"""
    1.list-[]
        -mutable
        -any datatype is supportted

    2.Tuple - ()
        -immutable

    3. Set - {}
        -sytores only unique values
    
    4.Dictonary 
        -mutable

"""

nums=[1,2,3]
cart=["phone" , "book" , 10 , False , None , {1: "a"} , nums]

print(cart)
cart[0]="pc"

marks =(22,33,44,55)
print(marks)

#marks[0]=30
print(type(marks))