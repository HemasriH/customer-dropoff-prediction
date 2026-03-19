# Customer Journey Analytics and Drop-Off Prediction in E-Commerce
### Introduction
Understanding customer behavior is essential for improving conversion rates in e-commerce platforms.
This project analyzes customer journey interactions to identify where users drop off during the purchase process and predicts churn risk using Machine Learning and Marketing Analytics techniques.
### Project Objective
The main objective of this project is to analyze customer browsing behavior and identify stages where customers abandon the purchase journey.
The system helps to:
* Understand customer interaction patterns
* Detect purchase drop-off stages
* Identify high churn-risk users
* Recommend marketing strategies to improve conversions
### Dataset Description
The dataset contains e-commerce user interaction events that track customer activities during their shopping journey.
Total Records: 74,817
Each record represents an event such as:
* Website visit
* Product view
* Add to cart
* Purchase
Key Features
* UserID – unique identifier
* Timestamp – activity time
* EventType – user action
* Product_name – viewed product
* Product_price – product price
### Data Preprocessing
The following preprocessing steps were performed:
* Converted timestamp to datetime format
* Removed unnecessary columns
* Sorted user actions by UserID and time
* Calculated time difference between events
* Created customer journey sessions
* A new journey session was created if the time gap exceeded 24 hours.
### Customer Journey Analysis
Customer journeys were analyzed to understand decision patterns:
* Page views
* Product views
* Add to cart actions
* Purchase completion

This helps identify the stage where users abandon the process.
### Drop-Off Stage Identification
Customers may drop off at different stages:
* Website Visit → user leaves early
* Product View → views but does not add to cart
* Add to Cart → adds but does not purchase
* Purchase → successful conversion
### Churn Risk Categorization
Customers were categorized into churn risk levels:
- High Risk → Added to cart but did not purchase
- Medium Risk → Viewed product but did not add to cart
- Low Risk → Completed purchase
### Customer Segmentation
K-Means clustering was used to segment customers into:
- Browsers
- Interested Users
- High Intent Users
- Buyers

This helps businesses understand customer intent levels.
### Feature Engineering
Important features created:
- Page views
- Product views
- Cart adds
- Total events
- Purchase status
- Scaled product price

### Machine Learning Models Used
- Logistic Regression
- Support Vector Machine
- Decision Tree
- Random Forest
⭐Best Model
Decision Tree was selected as the best model based on:
- Accuracy: 82%
- Better classification performance
### Marketing Recommendation System
Based on predicted drop-off stage, marketing strategies were suggested:
- Add to Cart Drop-off → Offer discount or free shipping
- Product View Drop-off → Recommend similar products
- Website Visit Drop-off → Show trending products
- Purchase → Suggest bundle offers

These strategies help improve customer conversion probability.
### Types of Analytics Used
- Descriptive Analytics → Understanding past behavior
- Diagnostic Analytics → Identifying drop-off stages
- Predictive Analytics → Predicting churn and drop-off
- Prescriptive Analytics → Suggesting marketing actions
### Conclusion
This project analyzes complete customer journey behavior instead of only detecting whether a purchase happens or not.
By predicting drop-off stages and churn risk, businesses can take data-driven marketing actions to increase engagement, reduce churn, and improve sales conversions.
