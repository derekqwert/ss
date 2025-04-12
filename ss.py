import ctypes
import time
import random

# Windows API constants for mouse input
MOUSEEVENTF_MOVE = 0x0001

# Function to simulate mouse movement
def move_mouse(dx, dy):
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)

print("Teams Keep-Alive script is now running (Press Ctrl+C to stop)")
try:
    while True:
        # Small random mouse movement
        move_mouse(1, 0)
        time.sleep(0.1)
        move_mouse(-1, 0)
        
        # Wait between movements (2-4 minutes)
        wait_time = random.randint(120, 240)
        print(f"Moved mouse. Waiting {wait_time} seconds until next movement...")
        time.sleep(wait_time)
except KeyboardInterrupt:
    print("Script stopped")
