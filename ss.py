import time
import random
import pyautogui
import argparse
from datetime import datetime

def keep_alive(interval_min=60, interval_max=180, movement_range=10):
    """
    Keeps Microsoft Teams active by making small mouse movements at random intervals.
    
    Args:
        interval_min (int): Minimum seconds between movements
        interval_max (int): Maximum seconds between movements
        movement_range (int): Maximum pixels to move in any direction
    """
    print("Teams Keep-Alive script is now running.")
    print("Press CTRL+C to stop the script.")
    print(f"Moving mouse every {interval_min} to {interval_max} seconds.")
    
    try:
        while True:
            # Get current time for logging
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # Store current mouse position
            current_x, current_y = pyautogui.position()
            
            # Generate random small movement
            x_move = random.randint(-movement_range, movement_range)
            y_move = random.randint(-movement_range, movement_range)
            
            # Move mouse slightly
            pyautogui.moveRel(x_move, y_move, duration=0.5)
            
            # Move back to original position
            pyautogui.moveTo(current_x, current_y, duration=0.5)
            
            print(f"[{current_time}] Mouse moved and returned to position.")
            
            # Wait for a random interval before next movement
            wait_time = random.randint(interval_min, interval_max)
            time.sleep(wait_time)
            
    except KeyboardInterrupt:
        print("\nTeams Keep-Alive script stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keep Microsoft Teams status active")
    parser.add_argument("-min", type=int, default=60, help="Minimum seconds between movements (default: 60)")
    parser.add_argument("-max", type=int, default=180, help="Maximum seconds between movements (default: 180)")
    parser.add_argument("-range", type=int, default=10, help="Maximum pixels to move in any direction (default: 10)")
    
    args = parser.parse_args()
    
    keep_alive(args.min, args.max, args.range)
