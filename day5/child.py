from father import father
from mother import mother
# class mother:
#     def bignose(self):
#         print("mother has big nose")
    
# class father:
#     def blueeyes(self):
#         print("child has blue eyes")
    
class child ( mother,father):
    def ww(self):
        return "child sleeps early"

ch=child()
ch.blueeyes()
ch.bignose()

f=father()
f=ch 
print(f.ww())