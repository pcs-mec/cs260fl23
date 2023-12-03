from icecream import ic

class Student():
    def __init__(self, name, sid, ssn):
        self.name = name
        self.sid = sid
        self.ssn = ssn

    def __repr__(self):
        return f'{self.name} {self.sid} {self.ssn}'

    def __lt__(self, other):
        return self.sid < other.sid

s1 = Student(name = 'jane', sid = 1, ssn = "555-22-2123")
s2 = Student(name = 'jon', sid = 2, ssn = "555-33-5523")
s3 = Student(name = 'Oki', sid = 3, ssn = "555-44-5555")
_s1 = Student(name = 'jane', sid = 1, ssn = "555-22-2123")


##########################################################
# what if you need to sort a list of Students by the sid field
my_list_2 = [s3, s1, s2,_s1]
ic(my_list_2)
print('sort list with sorted() function by sid field, you can overload __lt__()')
print('Note: sorted() returns a ***new*** sorted list')
ic(sorted(my_list_2))

print()

# sort by sid 
# list has built-in method .sort() that performs in-place sorting
print('sort list with .sort() method by sid field')
my_list_2.sort(key=lambda x: x.sid, reverse = True)
ic(my_list_2) 

