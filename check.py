import crypt

#test
sha = '$6$.lilLq/l$98DKK932dHltrY/zJ1M7HPK18VR.QcQCAe2h7BUNfTxwJMOGpGqjcPn58vlw8p0XZBX.Sbbq7bEtnHIFE.pR5/'

# #a
# sha = '$6$PSrys.E4$lU0lfZ61OzrG6TPYO4TFKHsKHO8kty/K4nGe.KHh1lNNtqSs3CMdCE3dvD/uIyGMMzfEk9dtNrZnwocrMc47c.'
def check_hash(p,s):
    c_pass = crypt.crypt(p,s)
    if c_pass == sha:
        return 1
    else:
        return 0
