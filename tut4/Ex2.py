def Ex2():
    fatGrams = float(raw_input("Enter the fat grams amount: "))
    carbGrams = float(raw_input("Enter the crab grams amount: "))
    caloriesFromFat = fatGrams*9
    caloriesFromcarbs = carbGrams*4
    print("Calories from fat: "+str(caloriesFromFat))
    print("Calories from crabs: "+str(caloriesFromcarbs))

def __main__():
    Ex2()
__main__()