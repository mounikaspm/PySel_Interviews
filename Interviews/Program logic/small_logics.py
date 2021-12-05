'''Merge Dic'''
import datetime
import time
import copy

import datetime as datetime

d1 = {0: 'me', 1: 'mine'}
d2 = {3: 'you', 4: 'yours'}

d2 = d1.copy.copy()

# d3 = d1  d2

# print(d2)

'''Remove list duplicates '''
# convert list to set and list again

l1 = [1, 2, 3, 2, 5, 6, 1]

l1 = list(set(l1))

# print(l1)

''' Reverse a string '''

# print "Ram is my name" as "Ram si my eman"

str1 = "Palindrome"

str2 = str1[::-1]
print(str2)

''' Reverse list'''

list1 = [1, 2, 3, 4]
list1.reverse()

print(list1)

''' current system date and time''' # not completed

date_today = datetime.date.today()
time_now = datetime.time.strftime()
datetime_now = datetime.now()

print(date_today)
print(datetime_now)


''' Print substring without inbuilt function'''

str = 'abcde12345'

str1 = ''

for i in str:
    str1 = i + str1

for j in range(0, 5):
    print(str1[j])

