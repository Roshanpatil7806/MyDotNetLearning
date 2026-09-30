
# code 1
class Bank:
    _instance = None
#remove the positional error we use *args and **kwargs in code
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating Bank object...")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, bank_name):
        self.bank_name = bank_name


# First object
bank1 = Bank("SBI")

# Second object
bank2 = Bank("HDFC")
bank3 = Bank("ICICI")

print("Bank 1:", bank1.bank_name)
print("Bank 2:", bank2.bank_name)
print("Bank 3:", bank3.bank_name)

print("Are both objects same?", bank1 is bank2)



"""
# code 2
class BankVault:

    obj = None

    def __new__(cls, *args, **kwargs):

        if cls.obj is None:
            print("Creating the vault...")
            cls.obj = super().__new__(cls)

        return cls.obj

    def __init__(self,amount):
       self.amount = amount
    def add_amount(self, amount):
        self.amount = self.amount + amount
vault1 = BankVault(20)
vault2 = BankVault(30)
vault2.add_amount(500)

vault3 = BankVault(30)
vault2.add_amount(1000)
print("Vault 1:", vault1.amount)
print("Vault 2:", vault2.amount)
print("Vault 3:", vault3.amount)
print("Are both vaults same?", vault1 is vault2)

"""