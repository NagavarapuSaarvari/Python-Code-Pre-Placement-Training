amt = int(input("Enter the amount: "))
denominations = [1,2,5,10,20,50,100,200,500]
denominations.sort(reverse=True)
notes = []
while amt>0:
    for i in denominations:
        while amt >= i:
            n = amt//i
            notes.append(n)
            amt = amt - n*i
print(denominations)
print(notes)