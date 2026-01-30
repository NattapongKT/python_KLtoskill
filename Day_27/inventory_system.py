class Inventory:
    def __init__(self):
        self.stocks = {"apple": 10, "orange": 5}

    def add_stock(self, item, quantity):
        if quantity < 0:
            return False
        # [BUG 1]: พิมพ์ผิดจาก += เป็น = (ทำให้ค่าเดิมหายไป)
        self.stocks[item] = quantity 
        return True

    def remove_stock(self, item, quantity):
        if item not in self.stocks:
            return False
        
        # [BUG 2]: ลอจิกการเช็คของพอไหมผิด (ใช้ > แทนที่จะเป็น >=)
        if self.stocks[item] > quantity:
            self.stocks[item] -= quantity
            return True
        return False