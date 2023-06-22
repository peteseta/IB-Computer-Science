from random import randint


class Client:
    def __init__(self, name, age, phone, id) -> None:
        """Create a new client object."""
        self.name = name
        self.age = age
        self.phone = phone
        self.id = id
        self.balance = 0
        print(f"Welcome {self.name}.")

    def deposit(self, amount):
        """Deposit money into the client's account."""
        self.balance += amount
        print(f"{self.name} deposited ${amount}.")
        print(f"New balance: ${self.balance}.")

    def withdraw(self, amount):
        """Withdraw money from the client's account."""
        if amount >= self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount
        print(f"{self.name} withdrew ${amount}.")
        print(f"New balance: ${self.balance}.")


class Bank:
    def __init__(self) -> None:
        """Create a new bank object."""
        self.clients = {}

    def new_account(self):
        """Create a new account for a client."""
        name = input("Name: ")
        age = input("Age: ")
        phone = input("Phone Number: ")
        while (new_acc_id := randint(100000, 999999)) in self.clients:
            new_acc_id = randint(100000, 999999)

        self.clients[new_acc_id] = Client(name, age, phone, new_acc_id)
        print(f"Your account number is {new_acc_id}.")

    def get_balance(self, id):
        """Get the balance of a client's account."""
        print(
            f"{self.clients[id].name} has ${self.clients[id].balance} in their account."
        )

    def transfer(self, sender_id, recip_id, amount):
        """Transfer money from one account to another."""
        if amount >= self.clients[sender_id].balance:
            print("Insufficient funds.")
        else:
            self.clients[sender_id].balance -= amount
            self.clients[recip_id].balance += amount
            print(
                f"Transfer successful. New balance: ${self.clients[sender_id].balance}."
            )


bank = Bank()

while True:
    choice = input(
        "Enter you bank account number or [1] to create a new account or [0] to quit:"
    )
    while not choice.isdigit():
        choice = input("enter a valid option!")

    if choice == "0":
        break
    elif choice == "1":
        bank.new_account()
    else:
        while int(choice) not in bank.clients:
            choice = input("enter a valid option!")

        client_activity = input(
            "[1] Deposit \n [2] Withdraw \n [3] Transfer \n [4] Check Balance \n [5] Quit \n"
        )
        while not choice.isdigit():
            client_activity = input("enter a valid option!")

        if client_activity == "1":
            amount = input("Amount: ")
            bank.clients[int(choice)].deposit(int(amount))

        if client_activity == "2":
            amount = input("Amount: ")
            bank.clients[int(choice)].withdraw(int(amount))

        if client_activity == "3":
            amount = input("Amount: ")
            recip_id = input("Recipient Account Number: ")
            bank.transfer(
                int(choice),
                int(recip_id),
                int(amount),
            )

        if client_activity == "4":
            bank.get_balance(int(choice))

        if client_activity == "5":
            break
