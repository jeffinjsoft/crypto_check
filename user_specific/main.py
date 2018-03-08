from helper import comp, check_hash, parse_options, split_arr

import time
from multiprocessing import Process, Manager, cpu_count


# max_lookup = 4
max_thread = cpu_count()


def check_user(f,u):
    users = []
    h = ''
    with open(f) as file:
        for d in file:
            us =  str(d.split(':')[0]).strip()
            if len(u) > 0 and u == us:
                # h = str(d.split(':')[])
                h = d.split(':')[1]

    return h

def do_check(ar,salt,sha,return_dict):

    for c in ar:
        if check_hash(c,salt,sha):
            print '##############################################'
            print 'Password matched :- %s'%(c)
            print '##############################################'
            print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
            # raise RuntimeError('There was an error!')
            return_dict[c] = c


def start_check(user,sha):
    print 'Staring check'
    print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    al = sha.split('$')[1].strip()
    s_v = sha.split('$')[2].strip()
    salt = "$"+al+"$"+s_v

    for p in range(1,max_lookup+1):
    # for p in range(1,4):

        print 'Looking on '+user+' serious :- '+str(p)

        comps = comp(p)
        size = len(comps)/max_thread
        # print size
        s_out = split_arr(comps,size)
        # print "len -- >"+str(len(s_out))
        ps_l = []

        c = 1
        manager = Manager()
        return_dict = manager.dict()
        for p_o in s_out:
            print 'Starting thread %d'%c
            ps = Process(target=do_check, args=(p_o,salt,sha,return_dict,))
            ps.daemon = True
            ps.start()
            ps_l.append(ps)
            # ps[c].join()
            c = c + 1
        for p_s in ps_l:
            p_s.join()
        if len(return_dict) > 0:
            print "completed -->%d"%p
            exit()
        print "completed -->%d"%p
        print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())


def main():
    print 'Starting..!!'
    parser, options, arguments = parse_options()

    if options.file == None:
        print 'Please provide file path with --file options'
        exit()
    else:
        if options.user == None:
            print 'Please provide username with --user option'
            exit()
        else:
            global max_lookup
            max_lookup = options.max_lookup
            print "Setting MAX look up count to --> %d"%max_lookup
            usr_hash = check_user(options.file,options.user)
            if len(usr_hash) > 0:
                print 'user found'
                start_check(options.user,usr_hash)
            else:
                print 'user Not found in %s file'%options.file
                exit()




    # ps = {}
    # for u in users:
    #     ps[u] = Process(target=do_check, args=(u,users[u],))
    #     ps[u].start()
    #     # time.sleep(1)
    #


if __name__ == '__main__':
    main()
