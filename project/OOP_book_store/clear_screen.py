import os

def clear_screen():
    # Dùng lệnh phù hợp tùy theo hệ điều hành
    os.system('cls' if os.name == 'nt' else 'clear')