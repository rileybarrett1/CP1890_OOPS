from dataclasses import dataclass

@dataclass
class product:
    name: str
    price: float
    discountpercent: int

    def getDiscountamount(self):
        return self.price * (self.discountpercent / 100)

    def getdiscountprice(self):
        return self.price - self.getDiscountamount()

