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
    word_length = len(words)
    counter = word_length  
    for word in words:
        counter += 1
        #if word is in chain
        if word in chain: 
            print "TEST"
            print words
            #print words[counter + 1]
            print "already exists"
            chain[word]['frequency'] += 1
            #if the next word has already followed that word increase that words probability
            #next_word = words[counter]
            print 'word: ' + word
            # print 'next word: ' + next_word

            # if next_word in chain[word]:
            #     print 'next word already appears in word chain'
            #     chain[word][next_word] += 1

            # else:
            #     print 'next word is not already in word chain'
            #     chain[word][next_word] = 1

        else:
            print "else:"
            #append an object version of word to chain and give value of 1
            print word
            chain[word] = {'frequency':1}

            # next_word = words[counter]
            print 'word: ' + word
            # print 'next word: ' + next_word

            # if next_word in chain[word]:
            #     print 'next word already appears in word chain'
            #     chain[word][next_word] += 1

            # else:
            #     print 'next word is not already in word chain'
            #     chain[word][next_word] = 1

            print chain



    return chain

words = text_to_array()
print words
lowercase_words = make_lowercase(words)
# print lowercase_words

chain = make_chain(lowercase_words)
print chain





