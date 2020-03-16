class Product:
    # Class attributes / static variables
    TAX = 15

    @staticmethod
    def set_tax(newtax):
        Product.TAX = newtax

    def __init__(self, name, price, features):
        self.name = name
        self.price = price
        self.features = features

    def print_details(self):
        print(self.name)
        print(self.price)
        for f in self.features:
            print(f)

    def add_feature(self, feature):
        self.features.append(feature)

    def remove_feature(self, feature):
        self.features.remove(feature)

    def net_price(self):
        return self.price + self.price * Product.TAX / 100


p = Product("Product1", 10000, ["f1", "f2", "f3"])
Product.set_tax(20)    # call static method
p.add_feature("f4")
p.print_details()
print(p.net_price())

# p2 = Product("Product2", 50000, ["f1", "f2", "f3"])
# p2.add_feature("f4")
# p2.print_details()
