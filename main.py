from combinations import comp
from check import check_hash
from parser import parse_options

import time
import threading

max_lookup = 4
max_thread = 4

print 'Starting..!!'

g_out = {}


def get_users(f_path):
    out = {}
    with open(f_path) as file:
        for d in file:
            h = d.split(':')[1]
            if h != '*':
                u =  str(d.split(':')[0]).strip()
                if len(u) > 0:
                    out[u] = h

        return out



def do_check(user,sha):
    print user
    print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    al = sha.split('$')[1].strip()
    s_v = sha.split('$')[2].strip()
    salt = "$"+al+"$"+s_v

    for p in range(max_lookup+1):
        print 'Looking on '+user+' serious :- '+str(p)

        comps = comp(p)
        c_f = 0
        for c in comps:
            if check_hash(c,salt,sha):
                print 'Password matched :-'+c+' for user -->'+user
                c_f = 1
                g_out[user]=c
                break
        if c_f == 1:
            break



def main():
    parser, options, arguments = parse_options()

    if options.file == None:
        print 'Please provide file path'
        exit()
    else:
        users = get_users(options.file)
        print users

    threads = []
    for u in users:
        t = threading.Thread(target=do_check, args=(u,users[u],))
        threads.append(t)
        t.start()
        time.sleep(1)

    print '##############################################'
    print '##############################################'
    print '##############################################'


    print g_out

    print '##############################################'
    print '##############################################'
    print '##############################################'

if __name__ == '__main__':
    main()
