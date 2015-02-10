class chain_maker(dict):
    pass

def text_to_array():
    with open ("test_text.txt", "r") as myfile:
        data=myfile.read().replace('\n', ' ')
        #print data

        words = data.split()

    print words
    print len(words)
    return words

def make_lowercase(words):
    lowercase_words = [word.lower() for word in words]
    return lowercase_words

def make_chain(words): 
    chain = chain_maker()  
    for word in words:
        #if word is in chain
        if word in chain: 
            print "already exists"
            chain[word]['frequency'] += 1
            #if the next word has already followed that word increase that words probability
            # next_word = word + 1
            # print next_word

            #if chain[word]
            #else add that word as a word that follows that word

        else:
            print "else:"
            #append an object version of word to chain and give value of 1
            print word
            chain[word] = {'frequency':1}
            print chain
    return chain

words = text_to_array()
print words
lowercase_words = make_lowercase(words)
# print lowercase_words

chain = make_chain(lowercase_words)
print chain





