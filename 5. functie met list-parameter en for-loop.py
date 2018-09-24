import math
def kwadraten_som():
    grondgetallen=[]
    for i in range(5):
        x=int(input("Please enter a number: "))
        grondgetallen.append(x)
    positive_values = list(filter(lambda x: x >0, lst))
    square_sum=math.sqrt(positive_values)
    print(square_sum)
kwadraten_som()
