import time
import os

def dramatic_zomato_opening():
    """Simulates a dramatic opening of the Zomato app."""
    
    # ANSI escape codes for text color and style
    RED = '\033[91m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{BOLD}{WHITE}*A dark screen. The sound of rain on a windowpane.*{ENDC}")
    time.sleep(2)
    print(f"{BLUE}*A single, flickering streetlamp illuminates the scene.*{ENDC}")
    time.sleep(1.5)
    print(f"{WHITE}*Thunder rolls in the distance, a low rumble.*{ENDC}")
    time.sleep(1)
    print(f"{WHITE}*A quiet, mournful cello melody begins...*{ENDC}")
    time.sleep(2)
    
    print("\n" + " " * 10 + f"{BOLD}{YELLOW}Zomato{ENDC}")
    print(" " * 10 + f"{BOLD}{WHITE}  •  {ENDC}")
    time.sleep(2)
    
    print(f"\n{BOLD}{WHITE}*A hand reaches out, fingers hovering over the icon...*{ENDC}")
    time.sleep(1)
    
    # Music swells
    print(f"{YELLOW}*The cello melody swells, joined by an ethereal choir...*{ENDC}")
    time.sleep(1.5)
    
    # Lightning flash and thunder
    print(f"\n{BOLD}{RED}*SUDDENLY, the music cuts.*{ENDC}")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BOLD}{YELLOW}*BLINDING FLASH OF LIGHTNING!*{ENDC}")
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BOLD}{YELLOW}*BLINDING FLASH OF LIGHTNING!*{ENDC}")
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BOLD}{YELLOW}*BLINDING FLASH OF LIGHTNING!*{ENDC}")
    time.sleep(0.1)
    print(f"{BOLD}{RED}*DEAFENING THUNDERCLAP!*{ENDC}")
    time.sleep(1)

    # Transition to the vibrant app screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BOLD}{WHITE}...In the aftermath, the screen is filled with vibrant food.{ENDC}")
    time.sleep(1)
    
    print(f"\n{BOLD}{YELLOW}🍲 Delicious Burgers {ENDC}")
    time.sleep(0.5)
    print(f"{BOLD}{RED}🍕 Crispy Pizzas {ENDC}")
    time.sleep(0.5)
    print(f"{BOLD}{BLUE}🍜 Savory Noodles {ENDC}")
    time.sleep(0.5)
    print(f"{BOLD}{WHITE}🍰 Sweet Desserts {ENDC}")
    time.sleep(1)
    
    print(f"\n{BOLD}{WHITE}*The storm rages on outside, but inside, the world is warm and delicious.*{ENDC}")
    time.sleep(2)
    
    print(f"\n{BOLD}{YELLOW}Welcome to Zomato.{ENDC}")
    
if __name__ == "__main__":
    dramatic_zomato_opening()

