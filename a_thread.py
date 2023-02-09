#TechCree - ssk test thread
from time import sleep
import _thread

#load more libaries

import time, random
import utime

# thread one
def core0_thread():
    #test
    print("hello world 1")
    

# threat two
def core1_thread():
    #test
    print("hello world 2")


second_thread = _thread.start_new_thread(core1_thread, ())

core0_thread()