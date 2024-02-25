class Budget:
    def __init__(self):
        self.user_categories = {}

    def get_categories(self):
        return [category
                for category in self.user_categories.values()
                ]
    
    def get_category_names(self):
        return [category.name
                for category in self.user_categories.values()
                ]

    def get_category(self, name):
        return self.user_categories[name]
    
    def add_category(self, category):
        self.user_categories[category.name] = category

    def remove_category(self, category_name):
        del self.user_categories[category_name]

    def edit_category(self, category_name, new_name):
        if category_name in self.user_categories:
            # Retrieve the category object
            category = self.user_categories.pop(category_name)
            # Update the category name
            category.name = new_name
            # Add the category back with the new name as the key
            self.user_categories[new_name] = category
            

