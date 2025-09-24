# Week 2 – Logging System Info
# Use Copilot to help you complete the code

import psutil
from datetime import datetime

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Use psutil to get CPU, memory, and disk usage
    cpu = psutil.cpu_percent(interval=1)  # Get CPU usage over 1 second interval
    memory = psutil.virtual_memory().percent  # Get memory usage percentage
    disk = psutil.disk_usage('/').percent  # Get disk usage for root directory

    log_line = f"[{now}] CPU: {cpu}% | MEM: {memory}% | DISK: {disk}%\n"
    return log_line

def write_log(log_line):
    # Open 'log.txt' in append mode and write the log_line
    with open('log.txt', 'a') as f:
        f.write(log_line)

if __name__ == "__main__":
    line = get_system_info()
    print("Logging:", line.strip())  # strip() removes the newline for cleaner console output
    write_log(line)