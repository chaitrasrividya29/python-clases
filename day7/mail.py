from abc import ABC, abstractmethod
class mail(ABC):
    @abstractmethod
    def send(self):
       pass
class email(mail):
    def __init__(self,message):
        self.message=message
    def  send(self):
        print("the message sent is",self.message)
class sms(mail):
    def __init__(self,message):
        self.message=message
    def  send(self):
        print(" the message sent is",self.message)
 
class whatsapp(mail):
    def __init__(self,message):
        self.message=message
    def  send(self):
        print(" the message sent is",self.message)

s=sms("this is sms")
e=email("this is sms")
w=whatsapp("this is sms")