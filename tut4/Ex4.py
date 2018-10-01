def Ex4():
    wallSpace = float(raw_input("Enter the wall space in square feet: "))
    priceOfPaintPerGallon = float(raw_input("Enter the price of paint per gallon: "))
    numberOfGallonOfPaint = wallSpace/112
    hoursOfLabor = wallSpace/8
    paintCost = numberOfGallonOfPaint*priceOfPaintPerGallon
    laborCharges = hoursOfLabor*35
    totalPaintingCost = paintCost+laborCharges
    print("The number of gallons of paint required: "+str(numberOfGallonOfPaint))
    print("The hours of labor required: "+str(hoursOfLabor))
    print("The cost of the paint: "+str(paintCost))
    print("The labor charges: "+str(laborCharges))
    print("The painting cost: "+str(totalPaintingCost))

def __main__():
    Ex4()
__main__()
