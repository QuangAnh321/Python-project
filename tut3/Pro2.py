number = raw_input("Enter a list of numbers: ")
sum = 0
for x in number:
     if x.isdigit():
         sum += int(x)
print(sum)