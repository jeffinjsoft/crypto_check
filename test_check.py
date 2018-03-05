import crypt

#bla
sha = '$6$JC1RHJdP$AbMal9HiO4NqZSntc5.NA4/QGjFRCn3v1ECkLRDqM6mZ1yfzEYgQdP42P5JLy.aC0jgZFaXheo45yj9.cxP1x0'

# #a
# sha = '$6$PSrys.E4$lU0lfZ61OzrG6TPYO4TFKHsKHO8kty/K4nGe.KHh1lNNtqSs3CMdCE3dvD/uIyGMMzfEk9dtNrZnwocrMc47c.'
def check_hash(p,s):
    c_pass = crypt.crypt(p,s)
    if c_pass == sha:
        return 1
    else:
        return 0
