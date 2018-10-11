phoneNumber = raw_input("Enter phone number in XXX-XXX-XXXX format: ")
phoneNumber = phoneNumber.split('-')

for x in phoneNumber[1:2]:
      for char in phoneNumber:
            if char == 'A' or char == 'B' or char == 'C':
                  char == '2'
            elif char == 'D' or char == 'E' or char == 'F':
                  char = '3'
            elif char == 'G' or char == 'H' or char == 'I':
                  char = '4'
            elif char == 'J' or char == 'K' or char == 'L':
                  char = '5'
            elif char == 'M' or char == 'N' or char == 'O':
                  char = '6'
            elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
                  char = '7'
            elif char == 'T' or char == 'U' or char == 'V':
                  char = '8'
            elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
                  char = '9'
 
print(phoneNumber)