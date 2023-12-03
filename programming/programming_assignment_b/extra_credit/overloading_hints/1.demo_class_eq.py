from icecream import ic

class Student():
    def __init__(self, name, sid, ssn):
        self.name = name
        self.sid = sid
        self.ssn = ssn


    def __eq__(self, other):
        # return self.ssn == other.ssn
        """ better way """
        if isinstance(other, self.__class__):
            return self.sid == other.sid and self.ssn == other.ssn
        return NotImplemented

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
# _s1 in my_list --> True if fields are the same
ic(_s1 in my_list) # 

# see the overload __eq__() method in this file


