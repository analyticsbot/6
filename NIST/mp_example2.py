import multiprocessing
import os
import signal
import time

def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def run_worker(j):
    print 'Run worker', j

def fun_worker(k):
    print 'Fun worker', k
    
def main():
    print "Initializng 5 workers"
    pool = multiprocessing.Pool(5, init_worker)

    print "Starting 5 jobs of 15 seconds each"
    for i in range(5):
        pool.apply_async(run_worker, args = (i,))
        pool.apply_async(fun_worker, args = (i*i,))

    try:
        print "Waiting 10 seconds"
        time.sleep(10)

    except KeyboardInterrupt:
        print "Caught KeyboardInterrupt, terminating workers"
        pool.terminate()
        pool.join()

    else:
        print "Quitting normally"
        pool.close()
        pool.join()

if __name__ == "__main__":
    main()
