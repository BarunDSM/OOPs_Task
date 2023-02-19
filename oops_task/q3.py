# Q3. What is multiple inheritance?
# Ans: When a class is derived from more than one base class it is called multiple Inheritance.

    
# Example:
class c1:
    def t1(self):
        print("c1")

class c2:
    def t2(self):
        print("c2")

class c3(c1,c2):
    pass

c3_ob=c3()
c3_ob.t1()
c3_ob.t2()
