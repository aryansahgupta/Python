num=int(input("enter the number::"))
def call(num):
    if(num>0):
     print(num,"is a positive")
    elif(num==0):
       print(num," is a Zero")
    else:
       print(num,"is a negative")     
call(num)