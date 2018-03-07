from helper import comp, check_hash, parse_options

import time
from multiprocessing import Process


max_lookup = 4
max_thread = 4


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
            usr = check_user(options.file,options.user)
            if len(usr) > 0:
                print 'user found'
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
