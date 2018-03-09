from helper import comp, check_hash, parse_options, split_arr

import time
from multiprocessing import Process, Manager, cpu_count

# max_lookup = 4
max_thread = cpu_count()



## PP

import pp


ppservers = ("172.17.7.37","172.17.7.128",)
job_server = pp.Server(ppservers=ppservers)

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

def do_check(ar,salt,sha):

    for c in ar:
        if check_hash(c,salt,sha):
            print '##############################################'
            print 'Password matched :- %s'%(c)
            print '##############################################'
            print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
            # raise RuntimeError('There was an error!')

            return c


def start_check(user,sha,p):
    print 'Staring check'
    print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    al = sha.split('$')[1].strip()
    s_v = sha.split('$')[2].strip()
    salt = "$"+al+"$"+s_v



    print 'Looking on '+user+' serious :- '+str(p)

    comps = comp(p)
    size = len(comps)/12
    # print size
    s_out = split_arr(comps,size)
    print 'Lenth of arr --> %d'%len(s_out)
    # print "len -- >"+str(len(s_out))
    ps_l = []

    c = 1
    jobs = [(input, job_server.submit(do_check, (input,salt,sha,), (check_hash,), ("time","crypt",))) for input in s_out]

    for input, job in jobs:
        # print "Sum of primes below is", job()
        if job() != None:
            job_server.print_stats()
            exit()

    job_server.print_stats()



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
                start_check(options.user,usr_hash,options.char_limit)
            else:
                print 'user Not found in %s file'%options.file
                exit()



if __name__ == '__main__':
    main()
