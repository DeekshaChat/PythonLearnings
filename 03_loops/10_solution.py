import time

attempt = 0
max_attempt = 5
wait_time =1

while attempt  < max_attempt:
    print(f"Attempt No: {attempt+1}, Wait time: {wait_time} seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1
   

