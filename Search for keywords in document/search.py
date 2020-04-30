import os
from sklearn.feature_extraction.text import CountVectorizer

docs = os.listdir("C:/Users/Administrator/Desktop/Test_Docs")

dict_data = {}
for doc in docs:
    file_exts = doc.split('.')
    if 'txt' in file_exts:
        with open(doc,encoding='utf-8') as data:
            vectorizer = CountVectorizer(ngram_range=(1, 2))
            vectorizer.fit(data)
            for feats in vectorizer.get_feature_names():
                if feats in dict_data.keys():
                    dict_data[feats].append(doc)
                else:
                    dict_data[feats] = [doc]
        
       
    
        
def search_query(word):
    return dict_data[word.lower()]
    
  
print(search_query('plenumAir purifierAir'))