class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to" , self.name , self.lastName, "'s cart")


customer1 = Customer()
customer1.name = "Dulapah"
customer1.lastName = "V"
customer1.age = 18
customer1.addCart()

customer2 = Customer()
customer2.name = "Sitthapong"
customer2.lastName = "J"
customer2.age = 18
customer2.addCart()

customer3 = Customer()
customer3.name = "Waranyu"
customer3.lastName = "W"
customer3.age = 18
customer3.addCart()

customer4 = Customer()
customer4.name = "Jongswitt"
customer4.lastName = "K"
customer4.age = 18
customer4.addCart()
