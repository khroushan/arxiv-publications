import pandas as pd


file_name = "covid_publication.csv"
data = pd.read_csv(file_name).drop('Unnamed: 0', axis=1)
print(data.columns)
print(data.head(5))

########## 
def create_word_dict(text:str, num_most_common:int = 10000):
    import string
    # replace all punctuations with whitespace     
    translator = str.maketrans(string.punctuation, 
                               ' '*len(string.punctuation))
    text_remove_punc = text.translate(translator)
    
    text_to_lower = text_remove_punc.lower()
    words = text_to_lower.split()
    
    word_count = {}
    for word in words:
        if not(word in word_count.keys()):
            word_count[word] = 1
        word_count[word]+=1

    return word_count, len(word_count)
##########

some_text = data.summary[0]
word_count, num_words = create_word_dict(some_text)

print(word_count)
print("number of unique words: {}".format(num_words))
