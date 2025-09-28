import psutil
import time

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    print(f"CPU: {cpu}% | RAM: {ram}%")
    time.sleep(10)
