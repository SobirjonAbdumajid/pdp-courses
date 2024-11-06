import time

def do():
    started = time.time() 
    print(started)

    time.sleep(3) # main

    # print('somsa') # main
    
    finished = time.time() 
    print(started)

    print(f'took {finished - started} seconds')
do()