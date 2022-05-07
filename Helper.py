import nltk
from nltk.stem.porter import PorterStemmer
nltk.download("punkt")

def nlp_tokenize(sentence):
    return nltk.word_tokenize(sentence.lower())

def nlp_stemming(word):
    stemmer=PorterStemmer()
    return stemmer.stem(word)

def bag_of_words(tokenize_word_list,all_word_list):
        all_words_arr=np.zeros(len(all_word_list))
        for word in tokenize_word_list:
            word_pos=all_word_list.index(word)
            all_words_arr[word_pos]=1
        return all_words_arr