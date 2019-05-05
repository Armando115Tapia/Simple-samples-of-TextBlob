from textblob import TextBlob

text = '''
I love you.
You have a beautifull that i never show never.
'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence)	
    print(sentence.sentiment.polarity)  
# 0.060
# -0.341

blob.translate(to="es")  # 'La amenaza titular de The Blob...'
