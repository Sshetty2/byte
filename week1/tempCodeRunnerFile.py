
def compute_divisors(num):
    counter = num
    divisors = []
    while num > 0:
        counter -= 1
	    if num % counter == 0:
		    divisors.append(counter)
            num -=1


print(compute_divisors(10))

def sum_of_divisors(num):
	pass

def divisor_count(num):
	pass

def get_totatives(num):
	pass

def totient(num):
	pass

