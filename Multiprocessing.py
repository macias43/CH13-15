import multiprocessing
import random
import time
from datetime import datetime

# Function to be executed by each process
def process_function():
    # Generates a random sleep time between 0 and 1 second
    sleep_time = random.random()
    
    # Sleep for the random time
    time.sleep(sleep_time)
    
    # Getting the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Printing the current time
    print(f"Process ID {multiprocessing.current_process().pid}: Current Time - {current_time}")

if __name__ == "__main__":
    # Creating three separate processes
    processes = [multiprocessing.Process(target=process_function) for _ in range(3)]
    
    # Starting each process
    for process in processes:
        process.start()
    
    # Waiting for all processes to finish
    for process in processes:
        process.join()
