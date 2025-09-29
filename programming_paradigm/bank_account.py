class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional initial balance.
        Default initial balance is zero.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        
        Args:
            amount (float): The amount to deposit
            
        Returns:
            None
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if funds are sufficient.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            bool: True if withdrawal was successful, False otherwise
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")


