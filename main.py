import time
import random
import os, sys
import copy

def get_dictionary():
    t0 = time.time()
    f = open('dictionary.txt', 'r')
    lines = f.readlines()
    f.close()
    t1 = time.time()

    print 'time to readlines: ', (str( t1 - t0)[:5])
    print 'number of lines: ', len(lines)
    print '\n'
    for i in range(5):
        r = random.randint(0,len(lines))
        print 'word #', str(r), ' : ', str(lines[r])


    t0 = time.time()
    words = []
    for line in lines:
        strip_line = line.rstrip("\n")
        words.append(strip_line)
    t1= time.time()

    print 'len of words: ', str(len(words))
    print 'time to create list : ', str(t1-t0)[:5]

    print "FALSE: lines[0]=='AA': ", str(lines[0]=='AA')
    print "TRUE: lines[0]=='AA\n': ", str(lines[0]=='AA\n')
    print "TRUE: words[0]=='AA': ", str(words[0]=='AA')

    return words

words = get_dictionary()


def n_letter_words(n, input, **kwargs):
    return filter(lambda w: len(w) == n, input)

def demo_n_letter_words(words):
    
    for _n in range(1,20):
        
        n_letters = n_letter_words(_n, words)
        print "n=",str(_n), ": ", str(len(n_letters))    
        
        if len(n_letters) > 0:
            out = n_letters[:min(4, len(n_letters))]
            print ("\n").join(out)
    return 1

demo_n_letter_words(words)

def search_me(_w, words):
    return filter(lambda w: w ==_w, words)

def demo_search_me(words):
    for this_word in ["AA", "ITALIAN", "ENGLISH", "PHALLIC", "ABACUS", "ITALY", "ENGLAND"]:
        print this_word, " - ", str(search_me(this_word, words))

demo_search_me(words)
    



print '------------'
print words[0]

def random_word(N,**kwargs):
    r = random.randint()
    return ret



def search_words(l_chars, _words):
    
    """ lchars: list length-n of either "" (meaning anything) or a character.
        _words: list of n-char words; (not of n-char means zip wont work).
        returns: list of words that match the reuested letters at the requested indexes."""
     
    return filter( lambda w: all( 
                        map(lambda c_w: (c_w[0] == "" or (c_w[0] == c_w[1]))
                            , zip(l_chars, w) ) 
                            ) ,_words)

print 'yes sex'
ss = ["S","E","X"]
ww = ["SEX","DEX"]
print search_words(ss,ww)

print 'yes both'
ss = ["","E","X"]
ww = ["SEX","DEX"]
print search_words(ss,ww)

def satisfy(lwords,inds):
    
    """ lwords: n-length list of strings; either n-chars or 0-chars.
        inps: list of indexes on lwords to check
        returns true if all words at inds work with each other, false otherwise """

    for iword ,word in enumerate(lwords):
        
        if not( iword in inds): continue
        
        for iletter, letter in enumerate(word):
 
            if not(iletter in inds): continue
            if (letter != lwords[iletter][iword]):
                return False

    return True #-------------------------------



good = ["WILL", "ICEY", "LEAN", "LYNX"]
print satisfy(good, range(4))

good_kinda = ["WILL", "", "LEAN", "LYNX"]
print satisfy(good_kinda, [0,2,3])

good_kinda2 = ["WILL", "JJJJ", "LEAN", "LYNX"]
print satisfy(good_kinda, [0,2,3])

print 'SAD!'
good_kinda2 = ["WILL", "JJJJ", "LEAN", "LYNX"]
print satisfy(good_kinda2, [0,1,2,3])

good_kinda = ["WILL", "", "LEAN", "LYNX"]
print satisfy(good_kinda, [0,2,3])



def search_term(pos, current, **kwargs):
    
    ret = []
    
    for i,v in enumerate(current):
        if v == "" or i == pos:
            ret.append( "" )
        else:
            ret.append( v[pos] )

    return ret



words4 = n_letter_words(4,words)

seed = "WILL"
data = [seed,"","",""]

print 'search_term'
print search_term(0,data)
print search_term(1,data)
print  search_term(2,data)
print search_term(3,data)

data = ["","IDEA","",""]
print 'search_term IDEA'
print search_term(0,data)
print search_term(1,data)
print search_term(2,data)
print search_term(3,data)


data = ["WILL","IDEA","","LAST"]
print 'search_term WILL IDEA ? LAST'
print search_term(0,data)
print search_term(1,data)
print search_term(2,data)
print search_term(3,data)



##### 1-unknown algo
seed = "WILL"
data = ["WILL","IDEA","LEGS",""]
st = search_term(3,data)
w3 = search_words(st,words4)
print w3

#Golden Rule, if you come to an empty set, before they're all filled in, 
#go back, at least 1 step, possibly more

def missing_places(current):
    return [ i for i,v in enumerate(current) if v ==""]

print 'missingplaces:'
print missing_places(["WILL","IDEA","LEGS",""])
print missing_places(["","IDEA","",""])



def played_places(current):
    return [ i for i,v in enumerate(current) if v !=""]

for step in range( 100000 ):
    pass
    





possibles = []
possibles.append([seed])

# BASIC
possibles.append(["IDEA"])
# OR
search1 = list(seed[1])
search1.extend( ["" for _ in range(3)] )
possibles.append(search_words( search1, words4 ) )

winners = []

"""
for tryword in possibles[1]:
    
    search_x = copy.copy( search1)
    search tryword[1]
    set1 = set( search_words())
"""

#Note: the seed doesn't have to be the first word, could end up anywhere.    
#Note: The seed, e.g. "WILL" could be any index, e.g the last word
#Note: the last word could be SAD! as exlamation point would be used by no other word
#Note: could use emojis like :)
"""

      N
      O
      T
      E 
H E Y : )

 C
 H
 I
 C
 K
O'BRIEN
 N



"""
































































