import time
from datetime import datetime, timedelta

class customer:
    def custom(self):
        self.customer_first_name=input("enter customer first name: ")
        self.customer_last_name=input("enter customer last name: ")
        self.customer_id=int(input("enter customer id: "))
        self.customer_contact=input("enter contact details: ")
        self.customer_build_no=input("enter building number: ")
        self.customer_line=input("enter line/colony: ")
        self.customer_district=input("enter district: ")
        self.customer_zip=input("enter zipcode: ")
        self.all_customer=[self.customer_first_name, self.customer_last_name, self.customer_id, self.customer_contact, self.customer_build_no, self.customer_line, self.customer_district, self.customer_zip]
        return self.all_customer

class order_item(customer):
    def order_det(self):
        self.order_id=int(input("enter order id: "))
        n=int(input("enter the number of items"))
        self.order_data={}
        while(True):
            i=int(input("1: continue \n 2.exit"))
            if i==1:
                self.product=input("enter product name: ")
                self.quantity=int(input("enter the quantity: "))
                self.order_data[self.product]=self.quantity
            else:
                break
        self.orders=[self.order_id, self.order_data]
        return self.orders

class order(order_item):
    def _init_(self):
        self.order_date = datetime.now().strftime("%d-%m-%Y")
        self.shipping_date = (datetime.now() + timedelta(days=4)).strftime("%d-%m-%Y")
        self.all_orders=[super().order_det(),self.order_date,self.shipping_date]
        return self.all_orders

class transaction(order):
    def _init_(self):
        self.transaction_det={tuple(super().custom()):super()._init_()}
        print("ORDER SUCESSFUL\n","{first, last, Cid, contact, address}: [[Oid, order items],order date, shipping date]")
        print(self.transaction_det)
    
tr=transaction()