# William Ikenna-Nwosu (wiknwo)
#  
# Modify and return the given map as follows: if the key 
# "a" has a value, set the key "b" to have that same value. 
# In all cases remove the key "c", leaving the rest of the 
# map unchanged.
#
# mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
# mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
# mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
def mapshare(maptoshare):
    if 'a' in maptoshare:
        maptoshare['b'] = maptoshare['a']
    maptoshare.pop('c', None)
    return maptoshare

def main():
    my_dict = {'a' : 'aaa', 'b' : 'bbb', 'c' : 'ccc'}
    print(mapshare(my_dict))

if __name__ == '__main__':
    main()