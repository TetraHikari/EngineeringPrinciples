import ZODB, ZODB.config, BTrees.OOBTree, transaction
import account
path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

# root.customers = BTrees.OOBTree.BTree()
# root.customers["Suisei"] = account.Customer("Jone")
# root.customers["Mio"] = account.Customer("Dave")
# sui = root.customers["Suisei"]
# mio = root.customers["Mio"]

# bankSui = sui.addAccount(account.CurrentAccount(400.0, sui, 5000))
# bankMio = mio.addAccount(account.SavingsAccount(200.0, mio, 1.0))

# bankMio.deposit(500.0)
# bankSui.withdraw(200.0)
# bankMio.transfer(150.0, bankSui)

root.customers = BTrees.OOBTree.BTree()
root.customers['Dave'] = account.Customer('Dave')
d = root.customers['Dave']
root.customers['Jone'] = account.Customer('Jone')
j = root.customers['Jone']

print("Create Account:")
b1 = d.addAccount(account.SavingsAccount(400, d, 1))
b2 = j.addAccount(account.CurrentAccount(200, j, 5000))
b2.deposit(500)
b1.withdraw(200)
b2.transfer(150, b1)


for customer in root.customers:
    obj = root.customers[customer]
    obj.printStatus()
    print("")
    index = 0
    while obj.getAccounts(index) != None:
        obj.getAccounts(index).printBankTransaction()
        print("")
        index += 1