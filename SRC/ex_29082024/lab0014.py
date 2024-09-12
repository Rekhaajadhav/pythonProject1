my_list=[1,3,4,3]
print(my_list)
for i in my_list:
    print(i)

my_list.append(6)
print(my_list)
my_list.extend([38,76,87])
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.pop()
print(my_list)

my_list[6]=54
print(my_list)