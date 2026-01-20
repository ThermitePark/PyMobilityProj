import time
import _thread


# Spawn a new thread
def thread_test():
    while True:
        print("\tsecond")
        time.sleep(0.7)
        
_thread.start_new_thread(thread_test, ())


while True:
    print("first")
    time.sleep(0.3)
    
    
        