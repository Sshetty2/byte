# from datetime import datetime

# # year = input("How Old are you?")


# # birthday = datetime(Y, M, D, 0, 0, 0)
# # diff = datetime.utcnow() - birthday

# # month  = datetime.utcnow().month - birthday.month

# # yearsDiff = datetime.utcnow().year - birthday.year
# # monthsDiff = datetime.utcnow().month - birthday.month
# # hoursDIff = datetime.utcnow().hours - birthday.hours
# # minutesDiff = datetime.utcnow().minutes - birthday.minutes
# # dayDiff = datetime.utcnow().minutes - birthday.days

# def dateConvert(string):
#     string = string.replace('-', ' ').split(' ')
#     birthday = datetime(string[0], string[1], string[2], 0, 0, 0)
#     yearsDiff = datetime.utcnow().year - birthday.year
#     totalMonths = (datetime.utcnow().month - birthday.month) +
#     hoursDIff = datetime.utcnow().hours - birthday.hours
#     minutesDiff = datetime.utcnow().minutes - birthday.minutes
#     dayDiff = datetime.utcnow().minutes - birthday.days
#     newString = f'months : %216, days : 6480, hours : 155520, and minutes : 388800'




# print(split("1989-06-18"))


# def compute_divisors(num):
#     counter = num
#     divisors = []
#     while num > 0:
#         counter -= 1
# 	    if num % counter == 0:
# 		    divisors.append(counter)
#             num -=1


# def compute_divisors(num):
#     counter = num
#     divisors = []
#     while num > 0:
#         counter -= 1
#         if counter == 0:
#             break
#         elif num % counter == 0:
#             divisors.append(counter)
#     return divisors


# print(compute_divisors(10))

# def sum_of_divisors(num):
# 	pass

# def divisor_count(num):
# 	pass

# def get_totatives(num):
# 	pass

# def totient(num):
# 	pass


# file_object = open('article.txt', 'r') # r = read, w = write, a = append 
# line = file_object.readline()
# print(line)
# file_object.close()

# with open("article.txt", "r") as file_object:
#     newArr = []
#     newArr2 = []
#     newDic= {}
#     for line in file_object:
#         for i in line.split():
#             for char in '-.,\n':
#                 i = i.strip().replace(char,' ')
#             newArr.append(i) 
#     for i in newArr:
#         i = i.replace('\"', ' ')
#         print(i)
        
    # for i in newArr:
    #     if not i in newDic: 
    #         newDic[i] = 1
    #     else: 
    #         newDic[i] += 1
    # print(newDic)

    # for char in '-.,\n':
    #     Text=Text.replace(char,' ')
    # Text = Text.lower()

# def fib(n):
#     if n == 0:
#         return [0] 
#     elif n == 1:
#         return [0,1]
#     else:
#         lst = fib(n-1)
#         lst.append(lst[-1] + lst[-2])
#         print(lst)
#         return lst
 




# fibonacciReturn = (fib(10))


# def fibonacci(n):
#     for i in fibonacciReturn:
#         if i < n:
#             print(i)


def cardValidation():

    card = input("input card number:")
    while len(card) < 15 or len(card) > 16:
        card = input("input valid card number that is greater than 15: ")
    while cardLuhnChecksumIsValid(card) == False:
        card = input("card number is invalid, please input valid card number: ")
    if len(card) == 15 and (card[0]+card[1] == "34" or card[0]+card[1] == "37"):
        print("Its an amex")
        quit()
    if card[0] == "4":
        print("its a visa")
        quit()
    if card[0]+card[1]+card[2]+card[3] == "6011":
        print("its a discover")
        quit()
    if card[0]+card[1] == "51" or card[0]+card[1] == "52" or card[0]+card[1] == "53" or card[0]+card[1] == "54" or card[0]+card[1] == "55":
        print("its a mastercard")
        quit()
    else:
        print("The card number you entered was the wrong length or it wasn't a type that could be recognized")
        quit()




import random 
import json

# def inputTerminal():
#     optionsMenu = input("Please select from the following options.. \n 1. Create Account \n 2. Log In \n 3. Quit \n input: ")
#     print(type(optionsMenu))
#     while optionsMenu not in ["1","2","3"]:
#         optionsMenu = input("Please input correct value \n input:")
#     if optionsMenu == "1":
#         newAccountInfo = input("input new account info")
#         #Append json object with account info 
#         print("new account created \n ... Porting back to main menu")
#         return inputTerminal()
#     if optionsMenu == "2"
#         logIn()


# dictionary = {red = blue, }
# def logIn():
#     testarr1 = arr1.split()[0]
#     testarr2 = arr1.split()[1]
#     testarr3 = testarr1[0] + testarr2
#     print(testarr3)
# logIn()
# #designate login procedures

# def checkBalance():
# #queries server for balance information

# def makeWithdrawal(x):
# #retreives x dollars from bank account

# def run():
#     masterUserAccts = {}

<<<<<<< HEAD
# validCardNumber = "6011001620"
# invalidCardNumber = "343125645896542"

# def cardLuhnChecksumIsValid(card_number):
#     """ checks to make sure that the card passes a luhn mod-10 checksum """
#     sum = 0
#     num_digits = len(card_number)
#     oddeven = num_digits & 1
=======
validCardNumber = "6011001620"
invalidCardNumber = "343125645896542"

def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ((sum % 10) == 0)

cardLuhnChecksumIsValid(validCardNumber)
# cardValidation()
# cardLuhnChecksumIsValid(validCardNumber)
>>>>>>> 69b0729... updated git repo

#     for count in range(0, num_digits):
#         digit = int(card_number[count])

#         if not (( count & 1 ) ^ oddeven ):
#             digit = digit * 2
#         if digit > 9:
#             digit = digit - 9

#         sum = sum + digit

#     return ((sum % 10) == 0)

# cardLuhnChecksumIsValid(validCardNumber)
# cardValidation()
# cardLuhnChecksumIsValid(validCardNumber)
def namesplit(name):

    newstring = []

    for i  in name : 
        if i not in ['*', '\\']:
            newstring.append(i)
        else: 
            return ''.join(newstring)

print(namesplit('Emmitt Smith*\SmitEm00'))
