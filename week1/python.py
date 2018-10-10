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


def compute_divisors(num):
    counter = num
    divisors = []
    while num > 0:
        counter -= 1
        if counter == 0:
            break
        elif num % counter == 0:
            divisors.append(counter)
    return divisors


print(compute_divisors(10))

def sum_of_divisors(num):
	pass

def divisor_count(num):
	pass

def get_totatives(num):
	pass

def totient(num):
	pass

