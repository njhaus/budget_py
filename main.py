from pprint import pprint
import inquirer
from select_menus import start_questions, run_questions, boolean_questions, continue_questions
from budget import Category, create_spend_chart
from categories import Budget
import unittest

def main():    
    new_budget = Budget()
    def start():
        print("\nWelcome to Budget Champ 1.0!")
        print("This program allows you to perform various budgeting actions.\n")
        print("You can use the following commands:")
        # print("learn   : Learn how to use the program")
        print("create  : Create a new budget")
        print("open    : Open an existing budget")
        print("test    : Show output of tests used when debugging the program")
        print("quit    : Quit the program")
        print('\n')
        answers = inquirer.prompt(start_questions)
        pprint(answers)
        get_command = answers['task']

        match get_command:
            # case "Learn":
            #     learn()
            case "Create":
                create(True)
            case "Open":
                open()
            case "Test":
                test()
            case "Quit":
                quit()

    # def learn():
    #     print('learn')
    #     pass

    def create(new):
        if new:
            print("\nBegin by creating some categories!")
            print("(Enter -b to go back, -q to quit, or -d if you're done creating categories.\n")
        else:
            print("\nCreate a new category!")
        while True:
            category_name = input("Enter Category Name: ")
            if check_for_cmd(category_name):
                    break
            if not category_name:
                print('Please enter a category name.')
            else:
                break
        while True:
            category_allotted = input("Enter amount of $ planned for this category: ")
            if check_for_cmd(category_allotted):
                break
            try:
                category_allotted = float(category_allotted)
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        # Make a new category called whatever the user input
        new_category = Category(category_name, category_allotted, category_allotted)
        new_budget.add_category(new_category)
        # Make another?
        print(f'\nCategory "{new_category.name}" created! Would you like to make another?\n')
        new_answers = inquirer.prompt(boolean_questions)
        pprint(new_answers)
        get_new_command = new_answers['boolean']
        match get_new_command:
            case 'Yes':
                create(False)
            case "No":
                print('Welcome to your budget!\n')
                run()


    def open():
        print('You have no saved budgets.\n')
        if user_continue():
            start()


    def run():
        run_answers = inquirer.prompt(run_questions)
        pprint(run_answers)
        get_run_command = run_answers['run']
        match get_run_command:
            case "View my categories":
                print("\nYour Categories:\n")
                categories = new_budget.get_categories()
                for c in categories:
                    print(f'{c}\n')
                    print(f'Current Balance: {"{:.2f}".format(c.balance)}')
                    print(f'Monthly allowance: {"{:.2f}".format(c.allotted)}')
                    print('\n')
                if user_continue():
                    run()
            case 'Make a deposit':
                c = choose_category()
                while True:
                    amount = input("Enter an amount: ")
                    try:
                        amount = float(amount)
                        break
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                description = input('Add a description (optional): ')
                c.deposit(amount, description)
                if user_continue():
                    run()
            case 'Make a withdrawal':
                c = choose_category()
                while True:
                    amount = input("Enter an amount: ")
                    try:
                        amount = float(amount)
                        break
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                description = input('Add a description (optional): ')
                c.withdraw(amount, description)
                if user_continue():
                    run()
            case 'Transfer funds':
                print("Transfer from:")
                transfer_from = choose_category()
                while True:
                    print("Transfer to:")
                    transfer_to = choose_category()
                    if transfer_to == transfer_from:
                        print('Please choose two different categories.')
                    else:
                        break
                while True:
                    amount = input("Enter an amount: ")
                    try:
                        amount = float(amount)
                        break
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                transfer_from.transfer(amount, transfer_to)
                if user_continue():
                    run()
            case 'View one category activity':
                c = choose_category()
                print(c)
                if user_continue():
                    run()
            case 'View my spending':
                categories = new_budget.get_categories()
                chart = create_spend_chart(categories)
                print(chart)
                if user_continue():
                    run()
            case 'Create a New Category':
                create(False)
            case 'Edit a category':
                print('Which category would you like to edit?')
                edit_category = choose_category()
                new_name = input('Edit category name (Leave blank to keep the same): ')
                new_allotment = input('Edit monthly allowance (Leave blank to keep the same): ')
                if new_name:
                    new_budget.edit_category(edit_category.name, new_name)
                    edit_category.set_name(new_name)
                if new_allotment:
                    try:
                        new_allotment = float(new_allotment)  # Convert to float
                        edit_category.set_allotted(new_allotment)
                    except ValueError:
                        print("Allotment not changed -- invalid input.")
                print('Reset category transactions?')
                reset_answers = inquirer.prompt(boolean_questions)
                pprint(reset_answers)
                get_reset_command = reset_answers['boolean']
                match get_reset_command:
                    case 'Yes':
                        edit_category.reset_ledger()
                        print(f'Resetting {edit_category}\n')
                        run()
                    case "No":
                        run()
            case 'Delete a category':
                c = choose_category('name')
                print(f'Are you sure you want to delete {c}?')
                delete_answers = inquirer.prompt(boolean_questions)
                pprint(delete_answers)
                get_delete_command = delete_answers['boolean']
                match get_delete_command:
                    case 'Yes':
                        print(f'Deleting {c}\n')
                        new_budget.remove_category(c)
                    case "No":
                        print(f'{c} not deleted.\n')
                        run()
                if user_continue():
                    run()
            case 'Quit':
                quit()

        

    def test():
        unittest.main(module='test', exit=False)
        if user_continue():
            start()


    def quit():
        print('Are you sure you want to exit the program?')
        quit_answers = inquirer.prompt(boolean_questions)
        pprint(quit_answers)
        get_quit_command = quit_answers['boolean']
        match get_quit_command:
            case 'Yes':
                print('Exiting the program. See you again soon!\n')
                exit()
            case "No":
                start()


    def check_for_cmd(cmd):
        # Return True in order to break the loop
        if cmd == '-b':
            start()
            return True
        if cmd == '-q':
            quit()
            return True
        if cmd == '-d':
            run()
            return True


    # argument: name or category?
    def choose_category(type = 'category'):
        category_list = new_budget.get_category_names()
        category_questions = [
                inquirer.List('category',
                            message="Choose a category",
                            choices=category_list,
                        ),
            ]
        category_answers = inquirer.prompt(category_questions)
        pprint(category_answers)
        get_category_command = category_answers['category']
        if type == 'name':
            # returns only chosen name
            return get_category_command
        else:
            # returns full Category object
            return new_budget.get_category(get_category_command)
    


    def user_continue():
        continue_answers = inquirer.prompt(continue_questions)
        pprint(continue_answers)
        get_continue_command = continue_answers['continue']
        if get_continue_command:
            return True


    start()


main()