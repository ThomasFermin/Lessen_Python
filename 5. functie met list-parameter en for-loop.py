def kwadraten_som():
    total = 0
    grondgetallen=[]
    for i in range(5):
        x=int(input("Please enter a number: "))
        if x > 0:
            grondgetallen.append(x)
    for i in grondgetallen:
        total = total + i * i
    print(total)
kwadraten_som()