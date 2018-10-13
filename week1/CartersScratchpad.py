from pprint import pprint

# #
# # Phase 1 - day 2
# #
# # Hold on to your butts...

# while True: # change to False to skip this part
#     line = input("type 'done' or give me an int >")
#     if line == 'done':
#         break
#     try:
#         value = int(line.strip())
#         print("Your integer was {}".format(value))
#     except ValueError:
#         print("ERROR: enter 'done' or an integer value")

# print("\n file IO")

# file_object = open('samplefile.txt', 'r') # r = read, w = write, a = append 
# line = file_object.readline()
# print(line)
# file_object.close()


# with open("samplefile.txt", "r") as file_object:
#     for line in file_object:
#         print("LINE: {}".format(line))


# with open("outputfile.txt", "w") as file_object:
#     for row in range(0,100,10):
#         for column in range(10):
#             print("{:<3}".format(row + column), end="", file=file_object)
#         print(file=file_object)


# from pprint import pprint # useful for viewing large datatypes
# pprint(matrix)

# print(matrix[4][7])

string = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
stringlist = string.split()
# print("stringlist: ", stringlist)
# print(", and ".join(stringlist))

# newlist = []
# for intstring in string.split():
#     newlist.append(int(intstring))
# print("newlist: ", newlist)

# # look up PEP8
# newlist2 = [int(value) for value in stringlist if int(value) % 2 == 0]
# print(newlist2)

# array = [[column + row for column in range(0, 10)] for row in range(0, 100, 10)]
# pprint(array)

# complist = [int(s) for s in string.split() if s[0] == '1']
# print("complist: ", complist)

# some list operations to look up:
# print("sum: ", sum([1,2,3,4,5,6]))
# print()
# print("sorted: ", sorted([1,5,3,4,2,6]))
# li = [3, -1, 2]
# print(sorted(li))
# print(li)
# li.sort(reverse=True)
# print(li)

# def mykey(n):
#     return abs(n)

# li.sort(key=lambda x: abs(x))
# print(li)

# print("lambdas & sorted with key: ", sorted([-3,-2,-1,0,1,2,3,4], 
#                                             key = lambda x: abs(x)))

#  Pick this up on Thursday

x = [7,6,5,4,3,2,1]
x.sort()
print(".sort (compare to sorted): ", x)
print()

# # copy the values of a list
# a = list(x)
# b = a

# a.sort()
# # b will be sorted

# a = list(x)
# b = a
# a = sorted(a) # a becomes a new, sorted, copy of its old values
# b != a

# a = list(x)
# b = a

# if a is b:
#     print("TRUE, reference equality.")

# a = list(x)
# b = list(a)

# if a is b:
#     print("FALSE, not reference equal.")

# if a == b:
#     print("TRUE, value equality.")

# x.append(8)
# x.append(9)
# print(x)
# topelement = x.pop()
# print(topelement)
# print(x)
# print()

# print(x[1])
# #print(x[start:stop:step])
# print("range: ", x[0:2])
# print("range: ", x[::-1])
# print("negative index: ", x[-2])
# # these are value copies of the list or sublist
# a = x[:] # another way to copy a list
# if a == x:
#     print("they are copies")

dic = {
    "a": 1,
    "b": 2,
    "d": [4, 5, 6]
}

accounts = {
    12345: {
        "firstname" : "Carter",
        "lastname" : "Adams",
        "pin" : 1234,
        "balance" : 3.50
    },
    45678: {

    }
}

print(dic["a"])
dic["b"] = 4
print(dic["b"])
# print(dic["c"]) # a KeyError
print(dic.get("c")) # returns a default value of None if the key does not exist
print(dic.get("c", 0)) # optional second parameter is the default value rather than None
print(dic["d"][1])

# dic = {
#     "a" : 0,
#     "b" : 1,
#     "c" : 2,
#     "d" : [1, 2, 3 ,4],
#     "e" : {
#         "ea" : "string value",
#         "eb" : [5, 6, 7, 8]
#     },
#     0 : "zero",
#     (1, 2) : "tuple key",
#     None: "any *immutable* type can be a key"
# }
# pprint(dic)
# print(dic["a"])
# print(dic[0])
# print(dic[(1,2)])

# try:
#     print(dic["z"])
# except KeyError:
#     print("indexing a nonexistent key will throw an error")

# print(dic.get("a"))
# print(dic.get("z"))

# print(dic.get("b"), "Default Value (commonly 'None')")
# print(dic.get("z"), "Default Value (commonly 'None')")

# print("\n This pattern might be useful: ")
if "new key" in dic:
    dic["new key"] += 1
else:
    dic["new key"] = 1

# print()

# print("iterating through a dictionary: ")
# for key in dic:
#     print("{key}: {value} for {key}".format(key=key, value=dic[key]))

# # digression, unpacking named arguments
# for key in dic:
#     pair = {"key": key, "value": dic[key]}
#     print("{key}: {value} for {key}".format(**pair)) # same as
#     print("{key}: {value} for {key}".format(key=key, value=dic[key])

# # key, value = ("key", "value")
# for key, value in dic.items():
#     print("{}:{}".format(key, value))
# # ("key": 1)
# ("key2": 2)

# # NOTE: you are not guaranteed *any* sort of regularity with the order of 
# # dictionary keys. Dictionaries are stored in implementation-dependent hashmaps
# # look up what that means.

# # but:

# sdic = {  
#     "zz" : "(all strings, all numeric)",
#     "z" : "of a comparable type",
#     "aa" : "to sort a dictionary",
#     "l" : "the keys must all be"
# }

# pprint(sorted(sdic, key=lambda k: len(k)))
# print("\n now figure out this line: ")
# print("\n".join([sdic[key] for key in sorted(sdic)]))

# print("\n this might be useful: ")
# sort_by_value = {
#     "one" : 1,
#     "twenty" : 20,
#     "negative one hundred" : -100,
#     "a million" : 1000000,
#     "zero" : 0
# }

# print("\n".join([k for k in sorted(sort_by_value, 
#                                     key=lambda x: sort_by_value[x])]))

# print("\n recursion")
# print("Basic idea: solve for a base (n=0) case")
# print("Assume f(n-1) works")
# print("Solve for n with f(n-1)\n")

# # now read chapters 1 - 3 of "Grokking Algorithms" to get recursion

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

import json

d = {
    "a" : 1,
    "b" : {
        "c" : 2,
        "d" : [1, 2, 3]
    },
    "c" : "four"
}

with open("output.json", "w") as file_object:
    json.dump(d, file_object, indent=2)

with open("output.json", "r") as file_object:
    newdata = json.load(file_object)

pprint(newdata)