def Ex3():
    classASeatsNum = int(raw_input("Enter the number of class A seats: "))
    classBSeatsNum = int(raw_input("Enter the number of class B seats: "))
    classCSeatsNum = int(raw_input("Enter the number of class C seats: "))
    totalIncome = classASeatsNum*20 + classBSeatsNum*15 + classCSeatsNum*10
    print("The total income is: "+str(totalIncome))

def __main__():
    Ex3()
__main__()