# doubling the elements of a list
list=[1,2,3,4]
double_list=[i*2 for i in list]
print(double_list)
#if at the end of the comprehension
double_list=[i*2 for i in list if i%2==0]
print(double_list)
calc_items=[2,5]
double_list=[i*2 for i in list if i in calc_items]
print(double_list)