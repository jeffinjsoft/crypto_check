from multiprocessing import Process

import time
def do_check(n):
    print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    print n
    time.sleep(2)

ps = {}
for i in range(10):

    ps[i] = Process(target=do_check, args=(i,))
    ps[i].start()
