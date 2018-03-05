import crypt

#test


# #a
# sha = '$6$PSrys.E4$lU0lfZ61OzrG6TPYO4TFKHsKHO8kty/K4nGe.KHh1lNNtqSs3CMdCE3dvD/uIyGMMzfEk9dtNrZnwocrMc47c.'
def check_hash(p,s,sha):
    c_pass = crypt.crypt(p,s)
    if c_pass == sha:
        return 1
    else:
        return 0
