#[:]is a range selector
"""It prevents the referncing  """
list=[3,4,5,6,7]
dup_list=list[:]
dup_list[0]=5
print(list)
dup_list=list[0:3]#this wont have the ending element
print(dup_list)
dup_list=list[:-1]
print(dup_list)

tuple=(1,2,3,4)
tuple1=tuple[:]
print(tuple1)
tuple1=tuple[:-1]
print(tuple1)
""" Does not work for sets and dictionaries
set={1,2,3,4}
print(set)
set1=set[:]
print(set1)
dict={'rahul':'64'}
dict1=dict[:-1]
"""
#range selector does shallow copy for complex data structures
list=[3,4,5,6,7]
dup_list=list[:]
dup_list[0]=5
print(list)
#here it is doing deep copy

list=[{'rahul':'64','vemuri':'56'}]
dup_list=list.copy()
dup_list[0]['rahul']='56'
print(list)
