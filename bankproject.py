class CheckPin:
    def verify(self, pin: int) -> bool:
        return 1000 <= pin <= 9999

class Balance:
    def __init__(self) -> None:
        self.bal: int = 2000

    def getBalance(self) -> int:
        return self.bal

class Transaction:
    b = Balance()

    def process(self, amt: int) -> None:
        pass

class Withdraw(Transaction):
    def process(self, amt: int) -> None:
        if amt <= self.b.bal:
            print("Amount withdrawn is", amt)
            self.b.bal -= amt
            print("Remaining balance is", self.b.getBalance())
            print("Transaction successful..")
        else:
            print("Insufficient funds")

class Deposit(Transaction):
    def process(self, amt: int) -> None:
        print("Amount deposit is", amt)
        self.b.bal += amt
        print("Balance is", self.b.getBalance())

class ATM:
    count: int = 0
    pin: int = 1234  # Initial PIN for demonstration purposes

    def reset_pin(self) -> None:
        current_pin = int(input("Enter current PIN: "))
        if current_pin == self.pin:
            new_pin = int(input("Enter new PIN: "))
            if 1000 <= new_pin <= 9999:
                self.pin = new_pin
                print("PIN reset successful.")
            else:
                print("Invalid new PIN. Must be a 4-digit number.")
        else:
            print("Incorrect current PIN.")

    def start(self) -> None:
        while True:
            entered_pin = int(input("Enter PIN Number: "))
            c=1
            if entered_pin == self.pin:
                cpn = CheckPin()
                if cpn.verify(entered_pin):
                    print("Enter your choice:")
                    print("1. Withdraw  2. Deposit  3. Reset PIN")
                    ch = int(input("Enter one from above: "))
                    if ch == 1:
                        amt = int(input("Enter an amount for withdrawal: "))
                        if amt > 0 and amt % 100 == 0:
                            wd = Withdraw()
                            wd.process(amt)
                            break
                        else:
                            print("Invalid amount")
                            break
                    elif ch == 2:
                        amt = int(input("Enter an amount for deposit: "))
                        if amt > 0 and amt % 100 == 0:
                            de = Deposit()
                            de.process(amt)
                            break
                        else:
                            print("Invalid amount")
                            break
                    elif ch == 3:
                        self.reset_pin()
                        c+=1
                        if c==3:
                            break
                    else:
                        print("Invalid choice")
                        break
                else:
                    print("Invalid PIN")
                    self.count += 1
                    if self.count == 3:
                        print("Blocked")
                        break
            else:
                print("Incorrect PIN")
                self.count += 1
                if self.count == 3:
                    print("Blocked")
                    break
# Example usage:
atm = ATM()
atm.start()
