#Gemotric mean
def calculate_gemomean(a,b):
    mean=a*b/(a+b)
    print(mean)

def isgreater(a,b):
    if a >b:
     print("1st no is greater")
    else:
     print("2st no is greater or equal")
   
a=12
b=5
isgreater(a,b)
calculate_gemomean(a,b)

c=23
d=56
calculate_gemomean(c,d)
isgreater(c,d)