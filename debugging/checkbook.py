class Checkbook:
    """
    Description:
        Represents a simple checkbook that allows deposits, withdrawals,
        and balance inquiries.

    Attributes:
        balance (float): The current account balance.
    """

    def __init__(self):
        """
        Description:
            Initializes a new Checkbook instance with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Description:
            Adds a specified amount to the account balance.

        Parameter:
            amount (float): The amount of money to deposit.
                            Must be a positive value.

        Return:
            None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Description:
            Withdraws a specified amount from the account if sufficient
            funds are available.

        Parameter:
            amount (float): The amount of money to withdraw.
                            Must be a positive value.

        Return:
            None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Description:
            Displays the current account balance.

        Return:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Description:
        Main loop of the program. Prompts the user for actions and
        handles input validation to prevent program crashes.

    Return:
        None
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
