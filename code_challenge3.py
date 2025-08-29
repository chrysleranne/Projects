name = input("Hi, what is your name?")
fare = eval(input("Your fare free?"))
isStudent = input("Are you a currently a student? (yes / no) ")

if isStudent.lower() == "yes":
        discount = fare * 0.2
        new_fare = fare - discount
        print("Hi",name, "Your discount is ", discount,"Your new fare is ", new_fare)
else:
        print("Hi", name,"You're only eligible for regular price")