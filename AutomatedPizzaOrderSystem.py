class pizza:
    def __init__(self,size:str,CrustType:str,):
        self.__size = size
        self.__CrustType = CrustType
        self.__TotalCost = 0
        self.__ToppingCost = 0 
        self.__topping = []

    @property
    def topping(self):
        return self.__topping
    
    @topping.setter
    def topping(self,topping):
        self.__topping.append(topping)
        self.__ToppingCost = self.__ToppingCost + 0.5

    def __ToppingCost(self):
        ToppingCost = self.__ToppingCost
        return ToppingCost

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,PizzaSize):
        self.__size = PizzaSize
    
    @property
    def CrustType(self):
        return self.__CrustType
    
    @CrustType.setter
    def CrustType(self,CrustType):
        self.__CrustType = CrustType
    
    def __SizeCost(self):
        SizeCost = 0 
        if self.__size == 'small':
            SizeCost = SizeCost + 5
        elif self.__size == 'medium':
            SizeCost = SizeCost + 7
        elif self.__size == 'large':
            SizeCost = SizeCost + 9

        return SizeCost
        

    def __CrustCost(self):
        CrustCost = 0 
        if self.__CrustType == 'stuffed':
            CrustCost = CrustCost +  2
        return CrustCost

    @property
    def TotalCost(self):
        self.__TotalCost = pizza.__SizeCost(self) + pizza.__CrustCost(self) + pizza.__ToppingCost(self)

        return self.__TotalCost

    def __repr__(self):
        return f"Pizza size: {self.__size} Crust Type: {self.__CrustType}"

class order:
    def __init__(self,CustomerName:str,CustomerAddress:str,CustomerPhone:str):
        self.__CustomerName = CustomerName
        self.__CustomerAddress = CustomerAddress
        self.__CustomerPhone = CustomerPhone
        self.__PizzaList = []
    @property
    def CustomerName(self):
        return self.__CustomerName
    
    @CustomerName.setter
    def CustomerName(self,name):
        self.__CustomerName = name
    
    @property
    def CustomerAddress(self):
        return self.__CustomerAddress
    
    @CustomerAddress.setter
    def CustomerAdrress(self,address):
        self.__CustomerAddress = address
    
    @property
    def CustomerPhone(self):
        return self.__CustomerPhone
    
    @CustomerPhone.setter
    def CustomerPhone(self,phone):
        self.__CustomerPhone = phone
    
    
    @property
    def PizzaList(self):
        return self.__PizzaList
    
    def MakePizza(self,size,crust):
        TempPizza = pizza(size,crust)
        self.__PizzaList.append(TempPizza)
        return TempPizza

print('Hello :)')
print('Welcome to automate pizza ordering system')
print("type 'no' if you want to stop ")


UserName = input('Enter your name: ')
UserAddress = input('Enter your address: ')
UserPhone = input('Enter your phone number: ')
UserPizzaNum = int(input('Enter number of pizza you want to order: '))

if UserPizzaNum > 0:
    UserOrder = order(UserName,UserAddress,UserPhone)

    for i in range(UserPizzaNum):
        print(f"Enter details for Pizza {i+1}")
        TempSize = input('Enter the size for pizza "small","medium" or "large":  ')
        TempCrust = input('Enter the type of crust to use "thin" ,"regular" or "stuffed": ')
        TempPizza = UserOrder.MakePizza(TempSize,TempCrust)
        AddTopping = input(" Do you want to add topping or not ? y/n: ")
        while True:
            if AddTopping == 'y':
                TempTopping = input('Enter your topping: ')
                TempPizza.topping = TempTopping
                break
            else:
                break
                

else:
    print('Invalid amount of pizza :( ')
print()
print()
print('Thank You for ordering from pizza automated system :)')
print()
print(f'Customer name: {UserName}')
print(f"Customer address: {UserAddress}")
print(f"Customer phone: {UserPhone}")
print(f"Number of pizza orders: {UserPizzaNum}")
TotalCostSum = 0 
y = 0 
for i in UserOrder.PizzaList:
    y = y + 1
    TotalCostSum = TotalCostSum + i.TotalCost
    print(f"Pizza {y} price: ${i.TotalCost}")
print(f"Total: ${TotalCostSum}")

