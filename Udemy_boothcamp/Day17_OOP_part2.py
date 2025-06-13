class User:
    # to initialize attributes
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
    
    def add_followers(self):
        self.followers +=1

    # the init function will automatically be called when a new obj is created


# PascalCase // camelCase // snake_case

user_1 = User("001","adorie")
user_2 = User("002", "foxie")

user_1.add_followers()
print(user_1.followers)
