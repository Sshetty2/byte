# def likes(names):
#     if len(names) == 0:
#         print('no one likes this')
#     if len(names) == 1:
#         print(f'{names[0]} likes this')
#     if len(names) == 2:
#         print(f'{names[0]} and {names[1]} like this')
#     if len(names) == 3:
#         print(f'{names[0]}, {names[1]} and 1 other person likes this')
#     if len(names) > 3:
#         print(f'{names[0]}, {names[1]} and {len(names)-2} other people like this')

# print(likes(["Max", "John", "Mark"] ))

#def bubble_sort(arr):
    # for i in arr:
    #     if curr = None:
    #         curr = i
    #     for j in newArr:
    #         if newArr == None:
    #             newArr.append(i)
    #         if i > j:
    #             curr = i 

# s1 = ['2','3','5','6','4']
# s2 = ['j','k','d','w','r']

# lst = [j + k for j in s1 for k in s2]



# ex_arr = [2,3,6,5,8,9,7,6,7,7,7,7,7,5,6,2,1,3]
# mylist=['a','b','c','d','e']


#myorder=[3,2,0,1,4]
#arr = [ arr[i] for i in myorder]
#print(arr)

#print(bubble_sort(mylist))

# def swap(tupple1, tupple2):
#     pass


# arr = [2,3,6,5,8,9,7,6,7,7,7,7,7,5,6,2,1,3]
# # n = len(arr)
# # lst= [(arr[j], arr[j+1] = arr[j+1], arr[j]) for i in range(n) for j in range(0, n-i-1) if if arr[j] > arr[j+1]]

# # print(lst)

# def bubbleSort(arr):
#     n = len(arr)
 
#     # Traverse through all array elements
#     for i in range(n):
 
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
 
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# #print(bubbleSort(arr))

# def binary_search_squared(n):
#     low = 0
#     high = n
#     mid = (low+high)*.5
#     while low <= high:
#         if mid*mid == n:
#             print(mid)
#             print("found num")
#             return mid
#         if mid*mid > n:
#             high = mid
#         else:
#             low = mid
#         mid = (low+high)*.5
#     return None

# arr = [1,3,5,7,9]

# print(binary_search_squared(576))

#rint(round(33/2)))
import dateutil.parser
import calendar

def date_format(datestring):
    date = dateutil.parser.parse(datestring)
    
    week_day_index = date.weekday()
    clock_time = date.strftime("%H:%M:%S")
    date_string = f"{calendar.day_abbr[week_day_index]} {date.day} {calendar.month_name[date.month]} "+ clock_time
    return date_string
    
print(date_format("2018-11-18T21:07:11Z"))