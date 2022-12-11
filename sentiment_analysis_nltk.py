from snownlp import SnowNLP
import matplotlib.pyplot as plt
import json
import googletrans
import time
import nltk
nltk.download([
"names",
"stopwords",
"state_union",
"twitter_samples",
"movie_reviews",
"averaged_perceptron_tagger",
"vader_lexicon",
"punkt",
])

from nltk.sentiment import SentimentIntensityAnalyzer

school_forms = ['ntu', 'ncku', 'ntpu', 'nycu']
key = 'title'
positive_tag = 'Positive'
neutral_tag = 'Neutral'
negative_tag = 'Negative'
date = '12-05'
data_num = '-500'
sleep_time = 1

translator = googletrans.Translator()

sia = SentimentIntensityAnalyzer()
# def get_analysis_snownlp():

# def get_sentiment_nltk():

def sentiment_result(text):
    time.sleep(sleep_time)
    english_text = translator.translate(text, dest='en').text

    polarity_scores = sia.polarity_scores(english_text)

    if polarity_scores['neu'] == 1.0:
        return neutral_tag

    elif polarity_scores['compound'] > 0:
        return positive_tag

    else:
        return negative_tag

for school in school_forms:

    fpath = "./data/" + school + date + data_num +'.json'
    positive_list = []

    with open(fpath, 'r', encoding="utf-8") as f:
        list_data = json.load(f)

    dict_num = {
        positive_tag : 0,
        neutral_tag : 0,
        negative_tag : 0
    }

    for data in list_data:
        s = SnowNLP(data[key])

        data['sentiment'] = sentiment_result(data[key])

        if data['sentiment'] == positive_tag:
            positive_list.append(data)

        dict_num[ data['sentiment'] ] += 1
        
        
        # print(data)
        

    result_fpath = "./data/" + school + date + data_num +'-NLTK-sentiment_result.json'

    with open(result_fpath, 'w', encoding='utf-8') as result_file:
        json.dump(list_data, result_file, indent=2, ensure_ascii=False)

    positive_result_fpath = "./data/" + school + date + data_num +'-NLTK-positive_sentiment_result.json'

    with open(positive_result_fpath, 'w', encoding='utf-8') as result_file:
        json.dump(positive_list, result_file, indent=2, ensure_ascii=False)
    
    fig = plt.figure()
    
    labels = [positive_tag, neutral_tag ,negative_tag]
    plt.title(school, fontsize=20)
    colors = ['orangered', 'seagreen', 'skyblue']

    plt.pie( list( dict_num.values() ), textprops = {"fontsize" : 14}, labels=labels, colors=colors, autopct = "%1.1f%%")

    plt.savefig(school + '-NLTK.png')
    plt.show()
        
        