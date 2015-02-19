import random

def text_to_array():
    with open ("test_text.txt", "r") as myfile:
        words=myfile.read().lower.split()

    # print words
    # print len(words)
    return words

def make_chain(words): 

    #Makes the chain as a dictionary
    chain = {}

    #print "counter: " + str(counter)
    #runs through words
    phrase = (words[0], words[1])

    for word in words[2:]:

        if phrase in chain:
            chain[phrase].append(word)

        else:
            #print str(phrase) + " doesn't exist in chain"
            chain[phrase] = [word]
            #print chain

        #remove old word from phrase
        # phrase = phrase[1:]

        phrase = (phrase[1], word)

    return chain

words = text_to_array()
#print words

chain = make_chain(words)
#print "Here is your chain:"
# print chain

def generate(chain):
    seed = random.choice(chain.keys())
    final_words = []

    for new_words in range(200):

        if seed not in chain:
            break

        picked = random.choice(chain[seed])
        final_words.append(picked)
        seed = (seed[1], picked)

    final = " ".join(final_words)
    print final


generate(chain)





