#imports
from textblob import TextBlob
#blob = TextBlob("Analytics Vidhya is a great platform to learn data science. \n It helps community through blogs, hackathons, discussions,etc.")
blob = TextBlob("I do not have love")
print (blob.sentiment)


