import pandas as pd
import csv
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoModel

path = 'nlp-model_1e-07'
tokenizer = AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased', do_lower_case=False)
modelo = AutoModelForSequenceClassification.from_pretrained(path)

df = pd.read_csv('olist_reviews.csv')
with open('olist_reviews.csv', encoding='Latin1') as f:
    reader = csv.reader(f, delimiter=',', quotechar='\"')
    corpus = list(reader)

    header, corpus = corpus[0], corpus[1:]

reviews = [w[20] for w in corpus]
ratings = [2 if w[19] in ['4', '5'] else 0 if w[19] in ['1', '2'] else 1 for w in corpus]
data = [{'X': review, 'y': rating} for (review, rating) in zip(reviews, ratings)]
dic = {'X': [], 'y': []}

for n in data:
   dic['X'].append(n['X'])
   dic['y'].append(n['y'])

data = pd.DataFrame.from_dict(dic)

results = {'sig_neg': [],
           'sig_neu': [],
           'sig_pos': [],
           'prob_neg': [],
           'prob_neu': [],
           'prob_pos': [],
           'sentiment': []}

for index, row in data.iterrows():
   texts, labels = row['X'], [row['y']]
   encoded_text = tokenizer(texts, return_tensors='pt')
   output = modelo(**encoded_text)
   scores = output[0][0].detach()

   prob_results = torch.softmax(scores, dim=0)
   results['prob_neg'].append(prob_results.numpy()[0])
   results['prob_neu'].append(prob_results.numpy()[1])
   results['prob_pos'].append(prob_results.numpy()[2])

   sigmoid_results = torch.sigmoid(scores)
   results['sig_neg'].append(sigmoid_results.numpy()[0])
   results['sig_neu'].append(sigmoid_results.numpy()[1])
   results['sig_pos'].append(sigmoid_results.numpy()[2])

   sent_pred = torch.argmax(output.logits, 1)
   results['sentiment'].append(sent_pred.numpy()[0])

results = pd.DataFrame.from_dict(results)
results_df = pd.concat([df, results], axis=1)

results_df.to_csv('olist_model_results.csv', index=False)
