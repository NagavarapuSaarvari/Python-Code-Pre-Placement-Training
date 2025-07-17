amt = int(input("Enter the amount: "))
denominations = [1,2,5,10,20,50,100,200,500]
denominations.sort(reverse=True)
notes = []
count = []
while amt > 0:
    for i in denominations:
        pos = False
        while amt >= i:
            c = amt//i
            amt = amt - c*i
            pos = True
        if pos:
            notes.append(i)
            count.append(c)
print(notes)
print(count)