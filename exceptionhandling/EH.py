
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
except Exception as e:
    print(e)    
#except ZeroDivisionError:
    #print( "Error: Cannot divide by zero")
finally:
    print("This block will always execute")  