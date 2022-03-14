'''
Python Project by Shubham

This project is the sentiment analysis of tweets of the Joe Biden and Donald Trump during the
2020 Presidential Election Period.
This analysis provides a visualization of the positive and negative sentiments shared by them
over the twitter.
The script also shows the election result based on number of votes
'''

#Installing Libraries
import csv
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Opening CSV files
b = open('joebiden_tweets.csv', encoding='UTF8')
t = open('trump_tweets.csv', encoding='UTF8')
csv_reader1 = csv.reader(b)
csv_reader2 = csv.reader(t)

#Creating lists to save data
biden_data = []
trump_data = []

for row in csv_reader1:
    biden_data.append(row[3])

#Cleaning CSV file
def txt_clean(word_list, stopwords_list):
    clean_words = []
    line = word_list.strip().split()
    for word in line:
        word_l = word.lower()
        if word_l not in stopwords_list:
            if word_l.isalpha():
                clean_words.append(word_l)
    return clean_words

#Removing Stopwords
stopwords_file = open('stopwords_en.txt','r', encoding='utf8')
stopwords = []
clean_biden_data = []
clean_biden_words = []
for word in stopwords_file:
    stopwords.append(word.strip())
for row in biden_data:
    clean_words = txt_clean(row, stopwords)
    clean_biden_words.append(clean_words)
    all_words_string = ' '.join(clean_words)
    clean_biden_data.append(all_words_string)

#Counting the most tweeted words by Joe Biden
a1 = sum(clean_biden_words,[])
Counter = Counter(a1)
most_occur1 = Counter.most_common(10)
print("The 10 most common tweeted words during election campaign by Joe Biden are:")
print(most_occur1)
print()

#Same procedure for other file
for row in csv_reader2:
    trump_data.append(row[10])
clean_trump_data = []
clean_trump_words = []
for word in stopwords_file:
    stopwords.append(word.strip())
for row in trump_data:
    clean_words = txt_clean(row, stopwords)
    clean_trump_words.append(clean_words)
    all_words_string = ' '.join(clean_words)
    clean_trump_data.append(all_words_string)

#Counting the most tweeted words by Donald Trump
from collections import Counter
a2 = sum(clean_trump_words,[])
Counter = Counter(a2)
most_occur2 = Counter.most_common(10)
print("The 10 most common tweeted words during election campaign by Donald Trump are:")
print(most_occur2)

#Sentiment Analysis of Biden Tweets to print most positive and negative tweets
sentence_sentiment_dict1={}
def sentiment(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    sentence_sentiment_dict1[sentence]=sentiment_dict['compound']
for sentence in clean_biden_data:
    sentiment(sentence)
print()
print('The top 3 positive sentiments on twitter by Joe Biden are:')
sorted_positive1 = sorted(sentence_sentiment_dict1.items(), key=lambda kv: kv[1],reverse=True)
positive3 = sorted_positive1[0:3]
pos=[]
for z in positive3:
  pos.append(z[0])
print(pos)
print()
print('The top 3 negative sentiments on twitter by Joe Biden are:')
sorted_negative1 = sorted(sentence_sentiment_dict1.items(), key=lambda kv: kv[1])
negative3 = sorted_negative1[0:3]
neg=[]
for z in negative3:
  neg.append(z[0])
print(neg)
print()

# Calculating a polarity score which gives us a sentiment dictionary
SID_obj1 = SentimentIntensityAnalyzer()
polarity_dict1 = SID_obj1.polarity_scores(clean_biden_data)
print("Polarity of Tweets is as follows :")
print()
print("Polarity percentage of tweets is", polarity_dict1['neg'] * 100, "% Negative")
print("Polarity percentage of tweets is", polarity_dict1['neu'] * 100, "% Neutral")
print("Polarity percentage of tweets is", polarity_dict1['pos'] * 100, "% Positive")
print()
print("Overall polarity percentage of Joe Biden's tweets is", end=" : ")

# Calculating overall sentiment by compound score
if polarity_dict1['compound'] >= 0.05:
    print("Positive")
elif polarity_dict1['compound'] <= - 0.05:
    print("Negative")
else:
    print("Neutral")
print()

#Sentiment Analysis of Trump Tweets to print most positive and negative tweets
sentence_sentiment_dict2={}
def sentiment(sentence):
    sid_obj2 = SentimentIntensityAnalyzer()
    sentiment_dict2 = sid_obj2.polarity_scores(sentence)
    sentence_sentiment_dict2[sentence]=sentiment_dict2['compound']

for sentence in clean_trump_data:
    sentiment(sentence)
print('The top 3 positive sentiments on twitter by Donald Trump are:')
sorted_positive2 = sorted(sentence_sentiment_dict2.items(), key=lambda kv: kv[1],reverse=True)
positive3 = sorted_positive2[0:3]
pos=[]
for z in positive3:
  pos.append(z[0])
print(pos)
print()
print('The top 3 negative sentiments on twitter by Donald Trump are:')
sorted_negative2 = sorted(sentence_sentiment_dict2.items(), key=lambda kv: kv[1])
negative3 = sorted_negative2[0:3]
neg=[]
for z in negative3:
  neg.append(z[0])
print(neg)

# Calculating a polarity score which gives us a sentiment dictionary
SID_obj2 = SentimentIntensityAnalyzer()
polarity_dict = SID_obj2.polarity_scores(clean_trump_data)
print("Polarity of tweets is as follows :")
print()
print("Polarity percentage of tweets is", polarity_dict['neg'] * 100, "% Negative")
print("Polarity percentage of tweets is", polarity_dict['neu'] * 100, "% Neutral")
print("Polarity percentage of tweets is", polarity_dict['pos'] * 100, "% Positive")
print()
print("Overall polarity percentage of Donald Trump's tweets is", end=" : ")

# Calculating overall sentiment by compound score
if polarity_dict['compound'] >= 0.05:
    print("Positive")
elif polarity_dict['compound'] <= - 0.05:
    print("Negative")
else:
    print("Neutral")
print()

#Plotting a wordcloud of tweets by Biden & Trump
wc1 = ' '.join(clean_biden_data)
wc2 = ' '.join(clean_trump_data)
wordcloud1 = WordCloud(max_font_size=50, max_words=1000, background_color="white").generate(wc1)
plt.figure()
plt.imshow(wordcloud1, interpolation='bilinear')
plt.title("Joe Biden Tweets")
plt.axis("off")
wordcloud2 = WordCloud(max_font_size=50, max_words=1000, background_color="white").generate(wc2)
plt.figure()
plt.imshow(wordcloud2, interpolation='bilinear')
plt.title("Donald Trump Tweets")
plt.axis("off")

#Plotting a Pie Chart of Election Results
labels = 'Joe Biden', 'Donald Trump'
votes = [306,232]
fig1, ax1 = plt.subplots()
ax1.pie(votes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.title("2020 Presidential Election Result", bbox={'facecolor':'0.8', 'pad':5})
plt.show()