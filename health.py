Person = int(input("What do you want ? \n Do you want to log an entry or retrieve the entries? \n press 1 for log  and press 2 for  retrive : "))
num1 = int(input("Press 1 for Food , Press 2 for Exercise : "))
num2 = int(input("Press 1 for Harry, Press 2 for clary and 3 for Mohammad : "))

def getdata():
    import datetime
    return datetime.datetime.now()

if Person == 1:
    if num1 == 1 and num2 == 1: #food for harry
        f = open("FoodR","a")
        inp = input("Enter the Food performed by Harry \n")
        time = str(getdata())
        f.write(inp + "[" + time + "]" + "\n")
        f.close()
        
    elif num1 == 2 and num2 == 1: #exercise for harry
        f2 = open("FoodM", "a")
        inp2 = input ("Enter the Food of Mohammad \n")
        time = str(getdata())
        f2.write(inp2 + "[" + time + "]" + "\n")
        f2.close()
        
    elif num1 == 1 and num2 == 2: #food for clary
        f1 = open("FoodC", "a")
        inp1 = input("Enter the Food performed by Clary \n")
        time = str(getdata())
        f1.write(inp1 + "[" + time + "]" + "\n")
        f1.close()
        
    elif num1 == 2 and num2 == 2: # exercise for clary
        f3= open("exerciseR", "a")
        inp3 = input("Enter the Exercise of Harry \n")
        time = str(getdata())
        f3.write(inp3 + "[" + time + "]" + "\n")
        f3.close()
        
    elif num1 == 1 and num2 == 3: # food for Mohammad
        f4 = open("exerciseC","a")
        inp4 = input("Enter the Exercise of Clary \n")
        time = str(getdata())
        f4.write(inp4 + "[" + time + "]" + "\n")
        f4.close()
    
    elif num1 == 2 and num2 == 3: #exercise for Mohammad
        f = open("exerciseM" ,"a")
        inp = input("Enter the Exercise of Mohammad \n")
        time = str(getdata())
        f.write(inp + "[" + time + "]" + "\n") 
        f.close()
    
    else:
       print("enter valid details")
        
               
    if Person == 2:
        if num1 ==1 and num2 == 1:
            f = open("FoodR" , "rt")
            print(f.read())
            f.close()
            
        elif num1 == 2 and num2 == 1:
            f1 = open("FoodC")
            print(f1.read())
            f1.close()
            
        elif num1 == 1 and num2 == 2:
            f2 = open("FoodM")
            print(f2.read())
            f2.close()
        
        elif num1 == 2 and num2 == 2:
            f3 = open("exerciseR")
            print(f3.read())
            f3.close()   
            
        elif num1 == 1 and num2 == 3:
            f4 = open("exerciseC")
            print(f4.read())
            f4.close()
            
        elif num1 == 2 and num2 == 3:
            f4 = open("exerciseM")
            print(f4.read())
            f4.close()
            
        
            
        
        
        
        
