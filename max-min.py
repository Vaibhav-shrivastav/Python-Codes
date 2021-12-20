# program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,it will print out the largest and smallest of the numbers. 
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or largest < num:
        largest = num
    if smallest is None or smallest > num:
        smallest = num
 
print("Maximum is", largest)
print("Minimum is", smallest)
