import time
def iclock():
    while True:
        try:
            input("Press enter to start,ctrl+c to stop.")
            start_time=time.time()
            print("timer has started")
            while True:
                print("Time:",round(time.time()-start_time,0),'secs','\n')
                time.sleep(1)
        except KeyboardInterrupt:
            print("Time has stopped")
iclock()


















