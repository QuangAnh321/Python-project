string = raw_input("Enter the Morse code: ")
if string == " ":
    newString = " "
elif string == "--..--":
    newString = ","
elif string == ".-.-.-":
    newString = "."
elif string == "..--..":
    newString = "?"
elif string == "-----":
    newString = "0"
elif string == ".----":
    newString = "1"
elif string == "..---":
    newString = "2"
elif string == "...--":
    newString = "3"
elif string == "....-":
    newString = "4"
elif string == ".....":
    newString = "5"

print("The converted code is: "+newString)
