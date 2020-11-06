# list1 =[1,3,4,5,9,8]
# list2 =list(map(lambda x: x**2,list1))
# print(list2)


#2

# nums =[1,2,3]
# print(sum(nums))

#3
# info =[1,6,0,4]
# print(all(info))

#4

# list_1 =[1,3,5,4,-1]
# new_list =list(map(lambda x: True if x <0 else False, list_1))
# print(any(new_list))


#5


# numbers =[1, 2, 3, 0, -1]
# def nums(num):
#     return num<0

# new_nums =list(filter(nums, numbers))
# print(new_nums)

#6


# list1 = [1, 2, 3, 0, -1]
# list2= list(filter(lambda x: x%2==0, list1))
# print(list2)

#7

# list_ =['hello', 'world', 'incapsulation', 'inheritance']
# new_list =list(filter(lambda x: x[0]=='i', list_))
# print(new_list)

#8

# from functools import reduce
# nums =[1, 2, 3, 4]
# def sum_nums(num1,num2):
#     return num1 + num2

# result = reduce(sum_nums, nums)
# print(result)

# variant 2 

# from functools import reduce
# nums =[1, 2, 3, 4]
# res =reduce(lambda num1,num2:num1+num2, nums)
# print(res)

#9


# numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_ =list(filter(lambda x:x%2 ==0, numbers ))
# odd_ =list(filter(lambda x:x%2 !=0, numbers ))
# print('Amount of even nums: ',len(even_),'\nAmount of even nums: ',len(odd_))


#10

# numbers =[-1, 2, 3, 4, -5, 6, 7, -8, 9]
# negative_=[]
# positive_=[]
# def sort_num(num):
#     if num >0:
#         positive_.append(num)
#     else:
#         negative_.append(num)

# list(map(sort_num, numbers))
# print('Positive numbers: ',positive_,'\nnegative numbers:',negative_)

#11


# nums =[-1, 2, 3, 4, -5, 6, 7, -8, 9, 0]
# def replace_(num):
#     if num < 0:
#         num = -1
#         return num
#     else:
#          num =1
#          return num
# print(list(map(replace_, nums)))

#12


# object_ = input('Ent records through a space: ').split()
# shifter_ =len(input('Ent negotive or positive num(in range of objects quantity): '))
# def shift_():
#     new_list = object_[shifter_:] + object_[:shifter_]
#     print(new_list)

# shift_()

#13

# def reverseArray(a):
#     return arr[::-1]

#14

# def isBalanced(s):
#     new =[]
#     brackets = {"(":")","[":"]","{":"}"}
#     for i in s:
#         if i in["(", "[", "{"]:
#             new.append(i)
#         else:
#             if new:
#                 top = new.pop()
#                 if brackets[top] != i:
#                     return "NO"
#             else:
#                 return "NO"
    
#     return "NO" if new else "YES"







