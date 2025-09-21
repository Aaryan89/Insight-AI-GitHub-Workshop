import time

def start_timer_display_msg():
    print("Get ready!!!")
    for i in range(1, 6):
        print(f'{i}...')
        time.sleep(2)
    time.sleep(5)

def press_enter_key():
    print("Its lights out and away we go!!!!!!!")
    start = time.perf_counter()
    print("Press enter")
    end = time.perf_counter()
    elapsed_time = start - end
    if elapsed_time <= 0:
        print("Thats a jumpstart...")
    else:
        print(f'Your reaction time is: {elapsed_time:.3f} seconds')    

press_enter_key()
start_timer_display_msg()
