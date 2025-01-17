# Customer Segmentation using RFM Analysis and K-Means Clustering

## Overview
This project utilizes RFM (Recency, Frequency, Monetary) analysis combined with the K-Means clustering algorithm to segment customers based on their purchasing behavior. The goal is to identify patterns and group customers into clusters for targeted marketing and improved customer management.

## Features
- **RFM Analysis**: Evaluates customer behavior using:
  - **Recency**: How recently a customer made a purchase.
  - **Frequency**: How often a customer makes purchases.
  - **Monetary**: The total spending of the customer.
- **K-Means Clustering**: Groups customers into clusters for actionable insights.
- **Visualization**: Visual representations of clusters and RFM scores.
- **Insights**: Identify loyal customers, at-risk customers, and more.

## Technologies Used
- **Python**: Core language for data processing.
- **Pandas**: For data manipulation.
- **Matplotlib/Seaborn**: For visualizing clusters and RFM scores.
- **Scikit-learn**: For implementing the K-Means algorithm.

## Dataset
The dataset contains the following columns:
- **CustomerID**: Unique identifier for customers.
- **InvoiceDate**: Date of purchase.
- **Amount**: Monetary value of the transaction.

## Requirements
- **numpy**==1.23.5  
- **pandas**==1.5.3  
- **matplotlib**==3.7.1  
- **seaborn**==0.12.2  
- **scikit-learn**==1.2.2  
- **jupyter**==1.0.0  


## Results
Segmented customers into X clusters (e.g., High-value customers, At-risk customers).
Visualized RFM scores and clusters for actionable insights.
