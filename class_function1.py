class classfuncation():
    def Subfields():
            list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            print("Sub-fields in AI are:")
            for temp in list:
                print(temp)
                
    def oddeven():
        num=int(input("Enter The Number:"))
        if((num%2)==0):
            print(num,"even number")
            message="even number"
        else:
            print(num,"odd number:")
            message="odd number"
        return message        

    def marriage_elegibility():
        Gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age<=21):
            print("NOT ELIGIBLE")
        elif(age<18):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")

    def percentage():
        m1=int(input("Subject1="))
        m2=int(input("Subject2="))
        m3=int(input("Subject3="))
        m4=int(input("Subject4="))
        m5=int(input("Subject5="))
        Total=m1+m2+m3+m4+m5
        print("Total:",Total)
        percentage=(Total/500)*100
        print("percentage:",percentage)
        return percentage

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("area formula:(Height*Breadth)/2")
        print("area of Triangle:",(Height*Breadth/2))
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle:",(Height1+Height2+Breadth))