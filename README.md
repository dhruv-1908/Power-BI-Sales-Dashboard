# Power-BI-Sales-Dashboard

For financial institutions to detect possible defaults and make well-informed lending 
decisions, credit risk analysis is crucial. The UCI Credit Card Default dataset, which 
comprises financial behavior and demographic information from more than 30,000 customers, 
is used in this report. Using methods like exploratory data analysis (EDA), clustering, 
principal component analysis (PCA), and predictive modeling, the objective is to examine 
trends that affect default risk. To determine their effect on client risk levels, important 
characteristics such as age, gender, education, marital status, credit limit, and past payment 
patterns are investigated. Financial analysts can enhance their risk assessment methods and 
put in place more efficient credit policies with the aid of data-driven insights from the 
interactive dashboards created in Power BI. 

In order to determine the probability of credit card client defaults, this report aims to 
perform a thorough credit risk analysis utilizing data visualization and machine learning 
techniques. The project's goal is to glean valuable insights from a sizable dataset that 
comprises payment patterns, financial transactions, and demographic characteristics. The 
report uses Power BI tools like principal component analysis (PCA), clustering, and 
predictive modelling to find important variables that affect default risk. High-risk client 
segmentation and interactive exploration are made possible by the dashboards that were 
developed. By increasing the precision of risk profiling, strengthening early warning systems, 
and assisting financial institutions in lowering their exposure to non-performing loans, this 
analysis aids in strategic lending decision-making.  

With the help of the UCI Credit Card Default dataset, which includes information on 
more than 30,000 credit card customers, this project aims to analyze credit risk. Age, 
education, gender, marital status, credit limits, payment history, and bill amounts are just a 
few of the demographic, financial, and behavioral factors that are examined. Interactive 
Power BI dashboards with data visualization, clustering, principal component analysis (PCA), 
and classification models are used to carry out the analysis. The project's scope is restricted to 
trend analysis, customer profile segmentation, and the development of predictive insights 
regarding default risk. The scope does not include operational elements like regulatory risk 
modeling, external credit bureau integration, or the implementation of real-time credit 
scoring. Enabling data-driven decision-making to support improved credit policies and risk 
mitigation techniques within financial institutions is the main goal.  
Design and Data Collection Methods  
Using data visualization and machine learning techniques, this project uses an 
organized analytical approach to evaluate credit risk among credit card customers. The UCI 
Credit Card Default dataset, which contains data on 30,000 credit card holders, is the data 
source. The dataset includes financial variables (credit limit, bill amounts, payment history), 
financial characteristics (age, gender, education, and marital status), and a binary target 
variable that indicates whether the client missed their payment the following month. To 
ensure that all analysis is based only on secondary data, no additional data was gathered 
beyond this dataset.  
Preprocessing the dataset was the first step in the data design process. This included 
handling null values, encoding categorical variables, standardizing numerical features, and 
creating new attributes (like the total bill and total payment). Following preparation, 
Microsoft Power BI was used to model the dataset for interactive exploration. Relationships 
between variables were established using a star schema, which made filtering and aggregation 
more efficient.  
The Power BI report was divided into several pages to address different analytical 
objectives. While segmentation was used using K-Means clustering to group clients based on 
financial similarity, the Exploratory Data Analysis (EDA) page visualizes demographic and 
behavioral patterns. Variance across features was explained using the results of PCA, which 
was carried out in Python to reduce dimensionality. Key performance indicators (KPIs) like 
AUC, precision, and recall were imported into Power BI for assessment after classification 
models like logistic regression and decision trees were trained externally in Python.  
To allow for dynamic filtering by factors like gender, age group, education, and 
marital status, slicers were incorporated throughout the report. End users can interact with the 
dashboard, gain insights, and assist in making strategic decisions for credit risk management 
thanks to this design approach.  


Power BI Sales Analysis and Data Modeling 
(1) Summary of Data Model 
Datasets Imported: 
• Orders.csv: Contains order-level information including Order ID, Order Date, 
Customer Name, City, and State. 
• Details.csv: Contains line-item level transaction details such as Amount, Profit, 
Quantity, Category, Sub-Category, and Payment Mode. 
Relationship: 
One-to-Many relationship: 
• Orders[Order ID] → Details[Order ID] 
• This relationship ensures each order maps to multiple line items 
Data Cleaning: 
• Checked for duplicates and blank entries but not found 
• Checked for appropriate data types (e.g., Date, Currency, Text) 
• Removed unnecessary columns (e.g., customer names, State in Orders) 
(2) DAX Measures Created 
Measure 
Description 
Total Sales 
Total transaction value 
DAX Formula 
Total Sales = 
SUM(Details[Amount]) 
Total Profit 
Total profit earned 
Total Profit = SUM(Details[Profit]) 
Average Profit per 
Order 
Avg. profit per unique 
order 
Average Profit per Order = 
DIVIDE([Total Profit], 
DISTINCTCOUNT(Details[Order 
ID])) 
Total Quantity Sold 
Sum of Quantity 
Total Quantity = 
SUM(Details[Quantity]) 
Profit Margin (%) 
Profitability measure 
Profit Margin = DIVIDE([Total 
Profit], [Total Sales]) * 100 
Monthly Sales 
Monthly trend of sales 
Monthly Sales Trend = 
CALCULATE([Total 
Sales],DATESMTD('Orders'[Order 
Date])) 
Top 5 Cities by Sales Ranked by Total Sales 
Hierarchical analysis 
Applied using Top N visual filter 
Sales by 
Category/Sub
Categoiry 
Applied using stacked Column Chart 
(3) Visualizations & Insights 
Visuals Created: 
• Line Chart: Monthly Sales Trend (shows seasonality or growth) 
• Stacked Bar Chart: Total Sales by Product Category & Sub-Category 
• Donut Chart: Distribution of Total Sales by Payment Modes 
• Clustered Bar Chart: Total Sales by Top 5 Cities 
• Card Visuals: Total Sales, Average Profit per Order, Total Quantity Sold, Profit 
Margin (%) 
• Sliders: Total Sales, Order Date (by month and year) 
Key Insights: 
• Top City: Indore contributed the highest total sales about $63680. 
• Most Selling Category: “Electronics” had the highest selling category. 
• Sales Trend: First quarter (Jan – March) showed a peak 
• Payment Mode Trend: COD was the most preferred payment method, and the least 
preferred payment method was debit card. 
(4) Optimization Techniques & Challenges 
Optimization Techniques Used: 
• Removed unnecessary columns (e.g., customer names, State in Orders) 
• Created measures instead of calculated columns where possible 
• Enabled star schema: clean one-to-many relationship 
• Applied Top N filter in visuals instead of using calculated columns 
Challenges Faced: 
• Limited Power BI functionality on Mac; used Power BI Online with limitations 
• Needed external help to generate .pbix from Windows environment 
• Difficulty using advanced Power Query online; opted to preprocess CSVs in Excel 
(5) Conclusion 
This report provides a well-structured, optimized, and interactive sales dashboard 
using Power BI. The data model allows dynamic filtering and insightful decision-making. 
The project strengthened our understanding of Power BI modelling, DAX, and 
performance best practices.
