# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix
#
# # Load your dataset (replace with actual path)
# df = pd.read_excel('credit card clients.xlsx')
#
# # Define features and target
# features = ['LIMIT_BAL', 'AGE', 'SEX', 'EDUCATION', 'MARRIAGE',
#             'PAY_0', 'PAY_2', 'PAY_3', 'BILL_AMT1', 'PAY_AMT1']
# target = 'default payment next month'
#
# # Clean dataset
# df = df.dropna()
#
# # Prepare data
# X = df[features]
# y = df[target]
#
# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Train logistic regression model
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, y_train)
#
# # Predict on test data
# y_pred = model.predict(X_test)
#
# # Generate confusion matrix
# cm = confusion_matrix(y_test, y_pred)
#
# # Create DataFrame suitable for Power BI visualization
# confusion_df = pd.DataFrame({
#     'Actual': [0, 0, 1, 1],
#     'Predicted': [0, 1, 0, 1],
#     'Count': [cm[0,0], cm[0,1], cm[1,0], cm[1,1]]
# })
#
# # Save the result for Power BI import
# confusion_df.to_csv('confusion_matrix.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Uncomment to debug column names
# print(dataset.columns.tolist())

# Replace with your actual column names from Power BI
features = ['LIMIT_BAL', 'AGE', 'SEX', 'EDUCATION', 'MARRIAGE',
            'PAY_0', 'PAY_2', 'PAY_3', 'BILL_AMT1', 'PAY_AMT1']
target = 'default.payment.next.month'

# Drop missing values
dataset = dataset.dropna()

# Train-test split
X = dataset[features]
y = dataset[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Predicted 0', 'Predicted 1'],
            yticklabels=['Actual 0', 'Actual 1'])

plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()
