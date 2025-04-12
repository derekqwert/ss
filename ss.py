import time
import pyautogui
import random
import argparse
from datetime import datetime

def keep_screen_alive(interval=60, jitter=True, mode="cursor"):
    """
    Keep the screen alive by simulating user activity.
    
    Parameters:
    - interval: Time in seconds between actions (default: 60)
    - jitter: Add random variation to the interval (default: True)
    - mode: Activity mode - "cursor" moves mouse, "key" presses shift key,
            "both" alternates between mouse and keyboard (default: "cursor")
    """
    print(f"Screen Keep Alive started at {datetime.now().strftime('%H:%M:%S')}")
    print(f"Mode: {mode}, Interval: {interval} seconds")
    print("Press Ctrl+C to stop the program")
    
    try:
        count = 0
        while True:
            # Add random jitter to the interval if enabled
            actual_interval = interval
            if jitter:
                actual_interval = interval + random.uniform(-interval * 0.1, interval * 0.1)
            
            # Perform action based on mode
            if mode == "cursor" or (mode == "both" and count % 2 == 0):
                # Get current mouse position
                current_x, current_y = pyautogui.position()
                
                # Move the cursor slightly in a random direction and then back
                offset_x = random.randint(10, 30) * random.choice([-1, 1])
                offset_y = random.randint(10, 30) * random.choice([-1, 1])
                
                pyautogui.moveTo(current_x + offset_x, current_y + offset_y, duration=0.5)
                time.sleep(0.5)
                pyautogui.moveTo(current_x, current_y, duration=0.5)
                
                print(f"{datetime.now().strftime('%H:%M:%S')} - Moved cursor")
            else:
                # Press and release the shift key (minimal impact)
                pyautogui.press('shift')
                print(f"{datetime.now().strftime('%H:%M:%S')} - Pressed shift key")
            
            count += 1
            time.sleep(actual_interval)
            
    except KeyboardInterrupt:
        print(f"\nScreen Keep Alive stopped at {datetime.now().strftime('%H:%M:%S')}")
        print(f"Ran for {count} cycles")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keep your screen active by simulating user activity")
    parser.add_argument("-i", "--interval", type=int, default=60, 
                        help="Time in seconds between actions (default: 60)")
    parser.add_argument("-j", "--no-jitter", action="store_false", dest="jitter",
                        help="Disable random variation in the interval")
    parser.add_argument("-m", "--mode", choices=["cursor", "key", "both"], default="cursor",
                        help="Activity mode: cursor, key, or both (default: cursor)")
    
    args = parser.parse_args()
    
    keep_screen_alive(interval=args.interval, jitter=args.jitter, mode=args.mode)
