![image](https://user-images.githubusercontent.com/91922356/217281133-4b75ff9f-5d04-4eb4-ba26-a7dfdd223190.png)


## **Introduction**
Sentiment analysis is the process of determining the emotional tone of a piece of text, such as a customer review, social media post, or news article. It is a field within Artificial Intelligence that has applications in various industries, such as marketing, journalism, and healthcare. The goal of sentiment analysis is to classify the sentiment of a text into one of several predefined categories, such as positive, negative, or neutral. 

With the widespread use of the internet and social media, customers now have a larger platform to voice their opinions and share their experiences with a brand. Because of that, this type of model become an important tool for businesses to understand and respond to big range of topics such as: 

- **Customer Feedback:** Sentiment analysis helps businesses understand customer feedback and opinions. This information can be used to improve products and services, and to address customer concerns and complaints.

- **Brand Reputation Management:** Sentiment analysis can be used to track brand reputation and monitor how a brand is perceived by its customers. This information can be used to improve brand image and to address negative sentiment before it becomes a major issue.

- **Market Research:** Sentiment analysis can be used to gather market research data and understand customer preferences, trends, and opinions. This information can be used to guide marketing and product development strategies.

- **Competitive Intelligence:** Sentiment analysis can be used to monitor competitor activity and to gain insights into competitor strengths and weaknesses.

With its ability to provide valuable insights into customer opinions, sentiment analysis is becoming increasingly important for businesses to stay ahead in a highly competitive market.

## **Dataset**
The dataset used in this project is available on the Kaggle platform:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

*This dataset was generously provided by Olist, the largest department store in Brazilian marketplaces. Olist connects small businesses from all over Brazil to channels without hassle and with a single contract. Those merchants are able to sell their products through the Olist Store and ship them directly to the customers using Olist logistics partners. See more on our website: www.olist.com*

The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. 

### **Data Schema** 
![image](https://user-images.githubusercontent.com/91922356/217290625-1d47e8e8-3a4b-4485-b2ac-f61cc4ca35b2.png)         
        
### **Dataframe**

The dataframe used on the model training was created using the SQL language. With 22 columns of independent variables that indicate the characteristics of different orders reviews. Each row of the dataset represents an order, each column being the informations about this order.

https://github.com/viniciusacosta/olist-nlp/blob/main/olist_reviews.csv

The features of this dataset present information about:

- **Product info:**
  - product_category_name
  - product_description_lenght
  - product_photos_qty

- **Order:**
  - price
  - freight_value 
  - shipping_limit_date
  - order_purchase_timestamp
  - order_approved_at
  - order_delivered_carrier_date
  - order_delivered_customer_date
  - order_estimated_delivery_date
  - order_status
  - day_diff
   
- **Customer info:**
  - customer_zip_code_prefix
  - customer_city
  - customer_state 
  
- **Review info:**
  - review_id
  - review_creation_date
  - review_answer_timestamp
  - review_score
  - review_comment_title
  - review_comment_message

## **Model**

There are various techniques and algorithms used for sentiment analysis, including rule-based approaches and machine learning algorithms like Naive Bayes, SVM, and deep learning models like BERT and LSTM.















