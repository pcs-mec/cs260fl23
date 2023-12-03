from icecream import ic

class Student():
    def __init__(self, name, sid, ssn):
        self.name = name
        self.sid = sid
        self.ssn = ssn

    def __repr__(self):
        return f'{self.name} {self.sid} {self.ssn}'

s1 = Student(name = 'jane', sid = 1, ssn = "555-22-2123")
s2 = Student(name = 'jon', sid = 2, ssn = "555-33-5523")
s3 = Student(name = 'Oki', sid = 3, ssn = "555-44-5555")
_s1 = Student(name = 'jane', sid = 1, ssn = "555-22-2123")

##########################################################
# s1,_s1 are different objects, but have same information.
# what if you need to be able to compare two objects:
#    such that return True if information is the same

# example: 
# s1 == _s1 --> True
# s1 == s2 --> False
ic(s1, s2, s3, _s1)
ic(s1 == _s1)
ic(s1 == s3)

my_list = [s1,s3]
print('[s1,s3]',my_list)
# _s1 in my_list  --> True if fields are the same
ic(_s1 in my_list)

# overload __eq__() see 1.demo_class_eq.py

print("----")

##########################################################
# what if you wanted to take full advantage of set()
my_set = set([s1,s3])
ic(my_set)
print('add _s1 into the set')
my_set.add(_s1)
ic(my_set)

# overload __hash__(), 
# see 2.demo_class_set.py with a WARNING
print("----")

##########################################################
# what if you need to sort a list of Students by the sid field
my_list_2 = [s3, s1, s2, _s1]
ic(my_list_2) 
# sort by sid, see 3.demo_class_sort.py
