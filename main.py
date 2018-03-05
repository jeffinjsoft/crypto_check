from combinations import comp
from check import check_hash

print 'Starting..!!'


salt = '$6$.lilLq/l'

# #a
# salt = '$6$PSrys.E4'


for p in range(5):
    print 'Looking on :- '+str(p)

    comps = comp(p)
    for c in comps:
        if check_hash(c,salt):
            print 'Password matched :-'+c
            exit()
