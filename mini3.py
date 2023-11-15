class MobileRecharge:
    def __init__(self):
        self.customer_accounts = []

    def add_mobile_account(self, mobile_number, owner_name, balance=0):
        self.customer_accounts.append({
            'mobile_number': mobile_number,
            'owner_name': owner_name,
            'balance': balance
        })
        print(f"Account balance is: {balance}")
        print(f"""Account on "{mobile_number}" number is created successfully""")

    def recharge_mobile(self, mobile_number, amount):
        for account in self.customer_accounts:
            if mobile_number == account['mobile_number']:
                account['balance'] += amount
                print(f"Account recharged successfully! New balance is {account['balance']}")
                break
        else:
            print("Mobile number not found.")

    def check_mobile_balance(self, mobile_number):
        for account in self.customer_accounts:
            if mobile_number == account['mobile_number']:
                print(f"Current balance for mobile number {mobile_number} is {account['balance']}")
                break
        else:
            print("Mobile number not found.")

    def display_mobile_account_details(self, mobile_number):
        for account in self.customer_accounts:
            if mobile_number == account['mobile_number']:
                print(f"Mobile Number: {account['mobile_number']}")
                print(f"Owner Name: {account['owner_name']}")
                print(f"Balance: {account['balance']}")
                break
        else:
            print("Mobile number not found.")


obj = MobileRecharge()

while True:
    print("1. Add new mobile account\n2. Recharge mobile account\n3. Check mobile balance\n4. Display account details\n5. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        mobile_number = int(input("Enter the mobile account:"))
        owner_name = input("Enter owner name:")
        obj.add_mobile_account(mobile_number, owner_name)

    elif choice == 2:
        mobile_number = int(input("Enter your mobile number:"))
        amount = int(input("Enter the amount to be recharged:"))
        obj.recharge_mobile(mobile_number, amount)

    elif choice == 3:
        mobile_number = int(input("Enter the mobile number to check balance:"))
        obj.check_mobile_balance(mobile_number)

    elif choice == 4:
        mobile_number = int(input("Enter the mobile number to display details:"))
        obj.display_mobile_account_details(mobile_number)

    elif choice == 5:
        break
