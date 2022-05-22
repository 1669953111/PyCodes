import sys
import time

def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("Progress: {}%: ".format(i), "▋" * (i // 2), end="")  # ▋ * -
        time.sleep(0.05)

sys.stdout.flush()
time.sleep(0.05)
if __name__ == '__main__':
    progress_bar()