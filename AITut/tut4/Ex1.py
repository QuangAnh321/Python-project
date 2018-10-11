
def Ex1():
    actualValue = int(raw_input("Eneter the actual value: "))
    assessmentValue = int((actualValue*6)/10)
    print("The assement value is: "+str(assessmentValue))
    propertyTax = float((assessmentValue*0.72)/100)
    print("The property tax is: "+str(propertyTax))

def __main__():
    Ex1()
__main__()