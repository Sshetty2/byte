
def mcNugCheck(x):
    value = True
    for i in [6,9,20,29,26,15]:
        if x%i == 0:
            value = False
    return value
            
def mcNuggetNums(num):
    return list(filter(mcNugCheck, list((range(0,num+1)))))


print(mcNuggetNums(500))