import ZODB, ZODB.config, BTrees._OOBTree, transaction
import persistent
from abc import ABC, abstractmethod
import transaction
import z_obj

path = "./config.xml"

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

if __name__ == "__main__":
    root.customers = BTrees._OOBTree.OOBTree()
    root.customers["Dave"] = z_obj.Customer('Dave')
    d = root.customers["Dave"]
    root.customers["Jone"] = z_obj.Customer('Jone')
    j = root.customers["Jone"]

    print("Create Account:")
    b1 = d.addAccount(z_obj.SavingAccount(400,d))
    b2 = j.addAccount(z_obj.CurrentAccount(200,d))
    d.printStatus()
    j.printStatus() 

    print("\nDeposit 500 to Account 2")
    b2.deposit(500)
    b2.printStatus()

    print("\nWithdraw 200 from Account 1")
    b1.withdraw(200)
    b1.printStatus()

    print("\nTransfer 100 from Account 2 to Account 1")
    b2.transfer(150, b1)
    b1.printStatus()
    b2.printStatus()

    transaction.commit()


