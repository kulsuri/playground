# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

from time import sleep

def sample_function():
    print("wassup")

def job_schedule(f, delay_in_ms):

    delay_in_sec = delay_in_ms / 1000

    sleep(delay_in_sec)

    return f()

job_schedule(sample_function, 2000)

