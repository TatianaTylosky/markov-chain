import random

def text_to_array():
    with open ("test_text.txt", "r") as myfile:
        data=myfile.read().replace('\n', ' ')
        #print data

        words = data.split()
        #print type(words)

    # print words
    # print len(words)
    return words

class chain_maker(dict):
    pass

def make_lowercase(words):
    lowercase_words = [word.lower() for word in words]
    return lowercase_words

def make_chain(words): 

    #Makes the chain as a dictionary
    chain = chain_maker()

    counter = 1
    print "counter: " + str(counter)
    #runs through words
    phrase = []
    for word in words:

        if counter == len(words):
            print "complete"

        elif counter == 1:
            phrase.append(word)
            print "first run"
            counter += 1

        else:
            #add new word to phrase
            phrase.append(word)
            
            print 'phrase: ' + str(phrase)
            print 'counter: ' + str(counter)

            phrase = tuple(phrase)

            #next_word = "blarg"
            next_word = words[counter]


            if phrase in chain:
                print str(phrase) + " already exists"
                for x in chain:
                    print phrase
                    print chain[x] #gives you value not key?
                    if chain[phrase] == chain[x]:
                        print "test"
                        temp = chain[phrase]
                        temp.append(next_word)

            else:
                print str(phrase) + " doesn't exist in chain"
                chain[phrase] = [next_word]
                #print chain

            #remove old word from phrase
            phrase = phrase[1:]

            phrase = list(phrase)

            counter += 1

    return chain

words = text_to_array()
#print words
lowercase_words = make_lowercase(words)
# print lowercase_words

chain = make_chain(lowercase_words)
#print "Here is your chain:"
print chain

def generate(chain):
    seed = ('be', 'four')
    final_words = []

    for new_words in range(200):

        if seed not in chain:
            break

        picked = random.choice(chain[seed])
        final_words.append(picked)
        seed = (seed[1], picked)

    final = " ".join(final_words)
    print final
    # if tuple(seed) in chain:
    #     print chain[seed]

    # else:
    #     print "error, you need a dif seed phrase"


generate(chain)





