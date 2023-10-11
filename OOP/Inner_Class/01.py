'''
    inner class là một lớp con nằm bên trong lớp cha
'''

class Customer:
    def __init__(self, id, name, bdno, bstreet, bcity, bcountry, bpin,sdno, sstreet, scity, scountry, spin) -> None:
        self.CusId = id
        self.CusName = name
        self.billAddress = self.Address(bdno, bstreet, bcity, bcountry, bpin)
        self.deliveryAddress = self.Address(sdno, sstreet, scity, scountry, spin)

    class Address:
       def __init__(self, dno, street, city, country, pin) -> None:
           self.deno = dno
           self.street= street
           self.city = city
           self.country = country
           self.pin = pin

       def display(self):
            print(self.deno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)

cus1 = Customer(10, 'Join',101, 'abc','Binh Thuan','Viet Nam', 10001, 200, 'btn','Binh Thuan','Viet Nam', 4000) 
cus1.billAddress.display()