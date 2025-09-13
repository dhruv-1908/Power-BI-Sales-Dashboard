import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_excel('credit card clients.xlsx')  # Or wherever your file is

# Feature engineering
df['AvgBillAmount'] = df[[f'BILL_AMT{i}' for i in range(1, 7)]].mean(axis=1)
df['AvgPaymentAmount'] = df[[f'PAY_AMT{i}' for i in range(1, 7)]].mean(axis=1)
df['AvgPaymentDelay'] = df[['PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']].mean(axis=1)
df['UtilizationRatio'] = df['AvgBillAmount'] / df['LIMIT_BAL']

# Select features
features = df[['LIMIT_BAL', 'AvgBillAmount', 'AvgPaymentAmount', 'AvgPaymentDelay', 'UtilizationRatio']].fillna(0)

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
df['ClusterGroup'] = kmeans.fit_predict(scaled_features)

# Export results
df[['ID', 'ClusterGroup']].to_csv("clustered_customers.csv", index=False)
