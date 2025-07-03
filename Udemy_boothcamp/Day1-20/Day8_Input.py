# def greet_with_name(name):
#     print(f"Hello {name}")

# name = input("What is your name? ")

# greet_with_name(name)

# name = Adorie
# name -- parameter (name of data being passed on the function)
# Adorie -- argument (the data being passed on the function)

# def greet_with(name,loc):
#     print(f"Hello {name}. Welcome to {loc}")

# name = input("What is your name? ")
# loc = input("Where is it now? ")

# greet_with(name,loc)
# greet_with(name = "Cat", loc = "home")


# Love calculator

def calculate_love_score(name1, name2):
    name = name1.upper() + name2.upper()
    score1 = 0
    score2 = 0
    
    for i in "TRUE":
        score1 += name.count(i)
    
    for i in "LOVE":
        score2 += name.count(i)
    
    total_score = score1*10 + score2

    print(f"Love Score {total_score}")
    

calculate_love_score("Kanye West", "Kim Kardashian")
