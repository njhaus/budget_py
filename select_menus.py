import inquirer


start_questions = [
  inquirer.List('task',
                message="What would you like to do?",
                choices=[
                    # 'Learn', 
                    'Create', 
                    'Open', 
                    'Test', 
                    'Quit'],
            ),
]

create_questions = [
  inquirer.List('create',
                message="What would you like to do?",
                choices=['Start with default categories', 'Create categories from scratch'],
            ),
]

run_questions = [
  inquirer.List('run',
                message="What would you like to do?",
                choices=[ 'View my categories',
                         'Make a withdrawal',
                         'Make a deposit',
                         'View one category activity',
                         'View my spending',
                         'Transfer funds',
                          'Create a New Category',
                          'Edit a category',
                          'Delete a category',
                          'Quit'
                          ],
            ),
]



boolean_questions = [
  inquirer.List('boolean',
                message="",
                choices=['Yes', 'No'],
            ),
]

continue_questions = [
  inquirer.List('continue',
                message="Continue?",
                choices=['Continue'],
            ),
]