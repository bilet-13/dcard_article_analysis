from snownlp import SnowNLP
import matplotlib.pyplot as plt
import json

school_forms = ['ntu', 'ncku', 'ntpu', 'nycu']
key = 'title'
positive_tag = 'Positive'
not_positive_tag = 'Not positive'

for school in school_forms:

    fpath = "./data/" + school + '12-01-100.json'
    
    with open(fpath, 'r', encoding="utf-8") as f:
        list_data = json.load(f)

    positive_num = 0
    negative_num = 0

    for data in list_data:
        s = SnowNLP(data[key])

        print(s.sentiments)
        if s.sentiments > 0.5:
            data['sentiment'] = positive_tag
            positive_num += 1
        else :
            data['sentiment'] = not_positive_tag
            negative_num += 1
        
        print(data)
        

    result_fpath = "./data/" + school + '12-01-100_sentiment_result.json'

    with open(result_fpath, 'w', encoding='utf-8') as result_file:
        json.dump(list_data, result_file, indent=2, ensure_ascii=False)

    fig = plt.figure()
    
    labels = [positive_tag, not_positive_tag]
    plt.title(school, fontsize=20)
    colors = ['orangered', 'skyblue']

    plt.pie([positive_num, negative_num], textprops = {"fontsize" : 14}, labels=labels, colors=colors, autopct = "%1.1f%%")

    plt.savefig(school + '.png')
    plt.show()
        


