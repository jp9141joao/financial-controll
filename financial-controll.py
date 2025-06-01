import os
import time

# Function to add an expense to the balance, statement, and expenses list
def Add_Expense(balance, statement, expenses, expense_name, expense_amount, expense_type):
    """
    Adds an expense record to both the statement and the expenses list.
    - expense_type 1: essential expense
    - expense_type 2: non-essential expense
    """
    if expense_type == 1:
        # Add as an essential expense
        statement.append([expense_name, expense_amount, 'Essential', 'Expense'])
        expenses.append([expense_name, expense_amount, 'Essential', 'Expense'])
    else:
        # Add as a non‑essential expense
        statement.append([expense_name, expense_amount, 'Non‑Essential', 'Expense'])
        expenses.append([expense_name, expense_amount, 'Non‑Essential', 'Expense'])


# Function to add an income to the balance, statement, and incomes list
def Add_Income(balance, statement, incomes, income_name, income_amount, income_type):
    """
    Adds an income record to both the statement and the incomes list.
    - income_type 1: fixed income
    - income_type 2: variable income
    """
    if income_type == 1:
        # Add as a fixed income
        statement.append([income_name, income_amount, 'Fixed', 'Income'])
        incomes.append([income_name, income_amount, 'Fixed'])
    else:
        # Add as a variable income
        statement.append([income_name, income_amount, 'Variable', 'Income'])
        incomes.append([income_name, income_amount, 'Variable'])


# Function to display all recorded expenses and their total
def Show_Expenses(balance, statement, expenses):
    """
    Prints a table of all expenses with details and calculates the total expenses.
    If there are no expenses, prompts the user to add at least one.
    """
    total_items = len(expenses)
    total_amount = 0

    if total_items <= 0:
        print('Add at least one expense to view it!')
        time.sleep(3)
        return

    print('* Expenses Table *')
    for i in range(total_items):
        name, amount, category, _ = expenses[i]
        print(f'\n-----------------------------------\n'
              f'Name: {name}\n'
              f'Number: {i + 1}\n'
              f'Expense Type: {category}\n'
              f'Amount: ${amount:.2f}')
        total_amount += amount

    print(f'\n-----------------------------------\nTotal Expenses: ${total_amount:.2f}')


# Function to display all recorded incomes and their total
def Show_Income(balance, statement, incomes):
    """
    Prints a table of all incomes with details and calculates the total income.
    If there are no incomes, prompts the user to add at least one.
    """
    total_items = len(incomes)
    total_amount = 0

    if total_items <= 0:
        print('Add at least one income to view it!')
        time.sleep(3)
        return

    print('* Income Table *')
    for i in range(total_items):
        name, amount, category = incomes[i]
        print(f'\n-----------------------------------\n'
              f'Name: {name}\n'
              f'Number: {i + 1}\n'
              f'Income Type: {category}\n'
              f'Amount: ${amount:.2f}')
        total_amount += amount

    print(f'\n-----------------------------------\nTotal Income: ${total_amount:.2f}')


# Function to delete an expense based on its index in the expenses list
def Delete_Expense(number, statement, expenses):
    """
    Removes the specified expense from both the statement and the expenses list.
    - number: the 1‑based index of the expense to remove
    """
    # Find the same record object in the statement and remove it
    index_in_statement = statement.index(expenses[number - 1])
    statement.pop(index_in_statement)
    expenses.pop(number - 1)


# Function to delete an income based on its index in the incomes list
def Delete_Income(number, statement, incomes):
    """
    Removes the specified income from both the statement and the incomes list.
    - number: the 1‑based index of the income to remove
    """
    # Find the same record object in the statement and remove it
    index_in_statement = statement.index(incomes[number - 1])
    statement.pop(index_in_statement)
    incomes.pop(number - 1)


# Function to display the full statement (all transactions) and current balance
def Show_Statement(balance, statement):
    """
    Prints all transactions in chronological order.
    Expenses are shown as negative, incomes as positive.
    At the end, prints the total net of this statement and the current balance.
    """
    total_items = len(statement)
    net_total = 0

    print('* Statement *')
    if total_items <= 0:
        print(f'\n-----------------------------------\n\nEmpty\n\nBalance: ${balance:.2f}\n-----------------------------------')
    else:
        for record in statement:
            name, amount, category, record_type = record
            if record_type == 'Expense':
                print(f'\n-----------------------------------\n'
                      f'EXPENSE\n'
                      f'Name: {name}\n'
                      f'Type: {category}\n'
                      f'Amount: -${amount:.2f}')
                net_total -= amount
            else:
                print(f'\n-----------------------------------\n'
                      f'INCOME\n'
                      f'Name: {name}\n'
                      f'Type: {category}\n'
                      f'Amount: +${amount:.2f}')
                net_total += amount

    print('\n-----------------------------------')
    print(f'Statement Total: ${net_total:.2f}\n\nBalance: ${balance:.2f}')

    # Wait for the user to press 1 to return to the main menu
    choice = int(input('\nEnter "1" to go back\nR: '))
    while choice != 1:
        choice = int(input('\nInvalid value! Enter "1" to go back\nR: '))


# Main function to run the interactive menu and orchestrate all operations
def Main():
    # Prompt the user for the initial account balance, validating input
    while True:
        os.system('cls')
        user_input = input('\nEnter your account balance\nR: ')
        balance = None

        # Replace commas with dots to allow decimal input
        user_input = user_input.replace(',', '.')

        # Check if the input is a valid number (integer or float, including negatives)
        if (user_input.isdigit() or
            user_input.replace('.', '', 1).isdigit() or
            (user_input[0] == '-' and user_input[1:].replace('.', '', 1).isdigit())):
            balance = float(user_input)

        if balance is not None:
            break

    # Ask if the account has a credit limit, and if so, add it to the balance
    while True:
        os.system('cls')
        user_input = input('\nDoes your account have credit?\n1- Yes\n2- No\nR: ')
        confirmation = None

        if user_input.isdigit():
            confirmation = int(user_input)

        if confirmation is not None:
            if confirmation == 1:
                # Prompt for the credit limit
                while True:
                    os.system('cls')
                    user_input = input('\nEnter your account credit limit\nR: ')
                    credit = None

                    user_input = user_input.replace(',', '.')
                    if (user_input.isdigit() or
                        user_input.replace('.', '', 1).isdigit() or
                        (user_input[0] == '-' and user_input[1:].replace('.', '', 1).isdigit())):
                        credit = float(user_input)

                    if credit is not None:
                        break

                balance += credit
                layout = '\nBalance + Credit: '
                break

            elif confirmation == 2:
                layout = '\nBalance: '
                break

    # Initialize data structures for the statement, expenses, and incomes
    statement = []  # Will hold all transaction records (expenses + incomes)
    expenses = []   # Will hold only expense records
    incomes = []    # Will hold only income records

    # Main menu loop
    while True:
        os.system('cls')
        total_items = len(statement)
        menu_choice = int(input(f'{layout} ${balance:.2f}\n\n'
                                '* Menu *\n'
                                '1- Add expense\n'
                                '2- Add income\n'
                                '3- Show expenses\n'
                                '4- Show income\n'
                                '5- Show statement\n'
                                '6- Exit\n'
                                'R: '))

        if menu_choice == 6:
            # Exit the program
            print('Program Terminated!')
            break

        elif menu_choice == 1:
            # Add a new expense
            os.system('cls')
            expense_name = input('\nEnter the name of the expense\nR: ')
            expense_amount = float(input('\nEnter the amount of the expense\nR: '))
            while expense_amount <= 0:
                expense_amount = float(input('\nInvalid amount! Enter the expense amount again\nR: '))

            expense_type = int(input('\nSpecify if the expense is:\n'
                                     '1- Essential (rent, fuel, health plan, food, etc.)\n'
                                     '2- Non‑Essential (streaming service, delivery, gym, social events, etc.)\n'
                                     'R: '))
            while expense_type not in (1, 2):
                expense_type = int(input('\nSpecify if the expense is:\n'
                                         '1- Essential (rent, fuel, health plan, food, etc.)\n'
                                         '2- Non‑Essential (streaming service, delivery, gym, social events, etc.)\n'
                                         'R: '))

            # Deduct the expense amount from the balance
            balance -= expense_amount
            Add_Expense(balance, statement, expenses, expense_name, expense_amount, expense_type)

            print('\nExpense added!')
            choice = int(input('\nEnter "1" to go back\nR: '))
            while choice != 1:
                choice = int(input('\nInvalid value! Enter "1" to go back\nR: '))

        elif menu_choice == 2:
            # Add a new income
            os.system('cls')
            income_name = input('\nEnter the name of the income\nR: ')
            income_amount = float(input('\nEnter the amount of the income\nR: '))
            while income_amount <= 0:
                income_amount = float(input('\nInvalid amount! Enter the income amount again\nR: '))

            income_type = int(input('\nSpecify if the income is:\n'
                                    '1- Fixed (salary, passive income, etc.)\n'
                                    '2- Variable (investments, overtime, etc.)\n'
                                    'R: '))
            while income_type not in (1, 2):
                income_type = int(input('\nSpecify if the income is:\n'
                                        '1- Fixed (salary, passive income, etc.)\n'
                                        '2- Variable (investments, overtime, etc.)\n'
                                        'R: '))

            # Add the income amount to the balance
            balance += income_amount
            Add_Income(balance, statement, incomes, income_name, income_amount, income_type)

            print('\nIncome added!')
            choice = int(input('\nEnter "1" to go back\nR: '))
            while choice != 1:
                choice = int(input('\nInvalid value! Enter "1" to go back\nR: '))

        elif menu_choice == 3:
            # Show all expenses
            os.system('cls')
            Show_Expenses(balance, statement, expenses)

            delete_choice = int(input('\nDo you want to delete any expense?\n1- Yes\n2- No\nR: '))
            while delete_choice not in (1, 2):
                delete_choice = int(input('\nInvalid value! Enter again to confirm delete option\nR: '))

            if delete_choice == 1:
                number = int(input('\nEnter the number of the expense to delete\nR: '))
                while number > total_items or number <= 0:
                    number = int(input('\nInvalid number! Enter the expense number again\nR: '))

                # Revert the expense amount back into the balance
                balance += expenses[number - 1][1]
                Delete_Expense(number, statement, expenses)
                print('\nExpense deleted successfully!')

            choice = int(input('\nEnter "1" to go back\nR: '))
            while choice != 1:
                choice = int(input('\nInvalid value! Enter "1" to go back\nR: '))

        elif menu_choice == 4:
            # Show all incomes
            os.system('cls')
            Show_Income(balance, statement, incomes)

            delete_choice = int(input('\nDo you want to delete any income?\n1- Yes\n2- No\nR: '))
            while delete_choice not in (1, 2):
                delete_choice = int(input('\nInvalid value! Enter again to confirm delete option\nR: '))

            if delete_choice == 1:
                number = int(input('\nEnter the number of the income to delete\nR: '))
                while number > total_items or number <= 0:
                    number = int(input('\nInvalid number! Enter the income number again\nR: '))

                # Subtract the income amount from the balance (to remove its effect)
                balance -= incomes[number - 1][1]
                Delete_Income(number, statement, incomes)
                print('\nIncome deleted successfully!')

            choice = int(input('\nEnter "1" to go back\nR: '))
            while choice != 1:
                choice = int(input('\nInvalid value! Enter "1" to go back\nR: '))

        elif menu_choice == 5:
            # Show the full statement of all transactions
            os.system('cls')
            Show_Statement(balance, statement)

        else:
            # Invalid menu option: ask if user wants to continue or exit
            os.system('cls')
            print('\nInvalid Option!')
            continue_choice = int(input('\nDo you want to continue?\n1- Yes\n2- No\nR: '))
            while continue_choice not in (1, 2):
                continue_choice = int(input('\nInvalid Option!\nDo you want to continue?\n1- Yes\n2- No\nR: '))

            if continue_choice == 2:
                print('Program Terminated!')
                break


# Run the main function when the script is executed
Main()
