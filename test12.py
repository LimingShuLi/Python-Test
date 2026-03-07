class ATM:
    def __init__(self, first, second):
      self.number = first
      self.bank = second

ATM1 = ATM(100, "工商银行")
ATM2 = ATM(101, "中国银行")
print(ATM1.number, ATM2.bank)

def zonggong(ATM):
    print(ATM.number + ATM.number)

zonggong(ATM1)

#或
def atm(number,bank):
    print(number,bank)

atm(100,"工商银行")