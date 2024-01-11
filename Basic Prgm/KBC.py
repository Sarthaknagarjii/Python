AB = input("Should we start playing : ")

Question1 = ["select the capital of mp "]
Answer1 = [["A. Bhopal"], ["B. Indore"], [" C. Jablapur"], ["D. Gwalior"]]
prizemoney1 = [1000]
Question2 = ["What is the financial capital of india ?"]
Answer2 = ["A. Delhi", "B. Chennai", "C. Mumbai", "D. Pune"]
prizemoney2 = [2000]
Question3 = ["What is the capital of india ?"]
Answer3 = ["A. Delhi", "B. gandhinagar", "C. kolkkta", "D. khilchipur"]
prizemoney3 = [3000]
Question4 = ["What is the street food capital of india ?"]
Answer = ["A. Ranchi", "B. Indore", "C. Coimbatore", "D. Pune"]
prizemoney4 = [4000]
Question5 = ["What is the Cultural capital of india ?"]
Answer5 = ["A. Bhopal", "B. Ujjain", "C. Nasik", "D. Kolkata"]
prizemoney5 = [5000]

if AB == "yes":
    print("lets Play kaun Banega Crore Pati...!")
    print("Question 1 ", Question1)
    print("options are", Answer1)
    Ans = input("Please give your answer : ")
    if Ans == "Bhopal":
        print("You own", prizemoney1, "RS")
        for i in range(1, 2):
            print("Question 2", Question2)
            print("Options are : ", Answer2)
            ans = input("Please give you answer : ")
            if ans == "Mumbai":
                print("you own", prizemoney2, "Rs")
            else:
                print("better luck next time")
    else:
        print("Thank you for playing KBC ")

else:
    print("Okay! NO Problem")

