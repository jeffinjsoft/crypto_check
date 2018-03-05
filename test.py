from combinations import comp
from test_check import check_hash

print 'Starting..!!'

#test
salt = '$6$JC1RHJdP'



for p in range(4):
    print 'Looking on :- '+str(p)

    comps = comp(p)
    for c in comps:
        if check_hash(c,salt):
            print 'Password matched :-'+c
            exit()
