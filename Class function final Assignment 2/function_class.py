class classfunction1():
    def print():
        print("HOPE AI")
        
    def Buy_inputs():
        name=input("ENTER YOUR NAME:")
        age=int(input("ENTER THE AGE:"))
        name=input("ENTER THE SCHOOL NAME:")
        name=input("ENTER THE DRGREE:")

    def Multiplication():    
        num1=int(input("a="))
        num2=int(input("b="))
        print("Multiplication=", num1*num2)

    def len():
        list2=[10,20,14,55,43,87,76]
        print(list2)
        print('Number of item in the list2:',len(list2))

    def positive():
        num=int(input("Enter any number:"))
        if(num<5):
            print("No is positive")
        else:
            print("negative")

    def marriage_elegibility():
        Gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age<=21):
            print("NOT ELIGIBLE")
        elif(age<18):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")
