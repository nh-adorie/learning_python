class User:
    # to initialize attributes
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # the init function will automatically be called when a new obj is created
    
    def follow(self, user):
        self.following += 1
        user.followers +=1


# PascalCase // camelCase // snake_case

user_1 = User("001","adorie")
user_2 = User("002", "foxie")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

