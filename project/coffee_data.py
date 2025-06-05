ingredients = {
    "latte": {
        "water": 200,
        "milk": 250,
        "sugar": 10,
        "coffee_beans": 24,
        "cream": 0
    },
    "cappuccino": {
        "water": 150,
        "milk": 180,
        "sugar": 0,
        "coffee_beans": 20,
        "cream": 0
    },
    "espresso": {
        "water": 30,
        "milk": 0,
        "sugar": 0,
        "coffee_beans": 18,
        "cream": 0
    },
    "americano": {
        "water": 250,
        "milk": 0,
        "sugar": 0,
        "coffee_beans": 18,
        "cream": 0
    },
    "macchiato": {
        "water": 30,
        "milk": 15,
        "sugar": 0,
        "coffee_beans": 18,
        "cream": 0
    },
    "mocha": {
        "water": 200,
        "milk": 200,
        "sugar": 0,
        "coffee_beans": 24,
        "cream": 20 # Assuming whipped cream falls under 'cream'
    },
    "flatwhite": {
        "water": 180,
        "milk": 220,
        "sugar": 0,
        "coffee_beans": 22,
        "cream": 0
    },
    "irish": {
        "water": 150,
        "milk": 0,
        "sugar": 15, # Brown sugar
        "coffee_beans": 20,
        "cream": 30
    },
    "coldbrew": {
        "water": 500,
        "milk": 0,
        "sugar": 0,
        "coffee_beans": 60,
        "cream": 0
    },
    "frappuccino": {
        "water": 100,
        "milk": 150,
        "sugar": 20, # Sugar syrup
        "coffee_beans": 25,
        "cream": 30 # Whipped cream,
    }
}

art = """
     ( (
       ) )
    ........
    |      |] WELCOME TO OUR MAGIC COFFEE SHOP 
    \      /         Enjoy your brew ☕
     `----'

╔═════════════════════ MENU ═════════════════════╗
║                                                ║
║       Latte         ...............   $4.00    ║
║       Cappuccino    ...............   $4.00    ║
║       Espresso      ...............   $2.50    ║
║       Americano     ...............   $3.00    ║
║       Macchiato     ...............   $3.50    ║
║       Mocha         ...............   $4.50    ║
║       Flatwhite     ...............   $4.25    ║
║       Irish         ...............   $6.00    ║
║       Coldbrew      ...............   $4.25    ║
║       Frappuccino   ...............   $5.00    ║
║                                                ║
╚════════════════════════════════════════════════╝
"""

coffee_prices = {
    "latte": 4.00,
    "cappuccino": 4.00,
    "espresso": 2.50,
    "americano": 3.00,
    "macchiato": 3.50,
    "mocha": 4.50,
    "flatwhite": 4.25,
    "irish": 6.00, 
    "coldbrew": 4.25,
    "frappuccino": 5.00,
}

stock = {
    "water": 5000,
    "milk": 5000,
    "sugar": 500, 
    "coffee_beans": 500,
    "cream": 500, 
}

