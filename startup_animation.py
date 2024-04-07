import time
import sys
import os

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/macOS
        os.system('clear')

def animate_text(text):
    delay = 0.001
    clear_screen()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(0.5)

def startup_animation():
    ascii_art = r"""
 _____                  _             _   ______                _    
|_   _|                (_)           | | |  ____|              | |   
  | |  ___ _ __ _ __ ___ _ _ __   __ _| | | |__ | |__   ___  ___| | __
  | | / _ \ '__| '_ ` _ \ | '_ \ / _` | | |  __|| '_ \ / _ \/ _ \ |/ /
 _| ||  __/ |  | | | | | | | | | (_| | | | |   | |_) | (_) | (_) <   
 \___/\___|_|  |_| |_| |_|_| |_|\__,_|_| |_|   |_.__/ \___/ \___/_|\_\
                                                                      
  __  __                                   
 |  \/  |                                  
 | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                            __/ |          
                           |___/           
"""
    animate_text(ascii_art)

if __name__ == "__main__":
    startup_animation()
