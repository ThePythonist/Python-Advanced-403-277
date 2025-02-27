class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Basket:
    def __init__(self, id):
        self.id = id
        self.products = []
        self.total_price = 0

    def addToBasket(self, prd, num=1):
        for i in range(num):
            self.products.append(prd)
            self.total_price += prd.price

        print(f"Product {prd.name} added to basket")
        print("=" * 100)

    def removeFromBasket(self, prd):
        if prd in self.products:
            self.products.remove(prd)
            self.total_price -= prd.price
            print(f"Removed {prd.name} from basket")
            print("=" * 100)
        else:
            print("Product is not in the basket")
            print("=" * 100)

    def showFactor(self):
        print(f"Factor : {self.total_price}")


prd1 = Product(1001, "asus vivobook", 65000)
prd2 = Product(1002, "asus tuf", 88500)
prd3 = Product(1003, "lenovo thinkpad", 49000)

ali = Basket(1)
kiarash = Basket(2)

ali.addToBasket(prd1, 2)

print([i.name for i in ali.products])
print("=" * 100)

ali.removeFromBasket(prd2)
print([i.name for i in ali.products])
print("=" * 100)

ali.showFactor()
