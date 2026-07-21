#task1
#keep asking valid integer number
#if not valid integer number print error
#task2
#handle index error while accessing list elements if it is out of range handle it 
#l=[1,2,3,4]
#print(l[4])


#task1
"""while True:
    try:
        num = int(input("Enter an integer: "))
        print("Valid integer entered:", num)
        break
    except ValueError:
        print("Error: Please enter a valid integer.")
"""

l=[1,2,3,4]
try:
    print(l[4])
except IndexError as e:
    print(e)