import pandas as pd
import tdqm.auto as tdqm
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoModel

path = 'nlp-model_1e-07'
tokenizer = AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased', do_lower_case=False)
modelo = AutoModelForSequenceClassification.from_pretrained(path)

df = pd.read_csv('olist_reviews.csv')

results = {'sig_neg': [],
           'sig_neu': [],
           'sig_pos': [],
           'prob_neg': [],
           'prob_neu': [],
           'prob_pos': [],
           'sentiment': []}

for index, row in tqdm(df.iterrows(), total=len(df)):
   texts, labels = row['review_comment_message'], [row['review_score']]
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

dicio = {0: 'Negative',
         1: 'Neutral',
         2: 'Positive'}

results_df['sentiment'] = results_df['sentiment'].replace(dicio)

results_df.to_csv('olist_model_results.csv', index=False)
