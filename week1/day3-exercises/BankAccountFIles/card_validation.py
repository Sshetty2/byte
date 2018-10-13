
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
