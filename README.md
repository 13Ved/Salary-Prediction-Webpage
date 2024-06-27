# Salary-Prediction-Webpage

In this project, we aim to develop a salary prediction webpage using Streamlit, a popular Python library for creating interactive web applications, and the Stack Overflow survey dataset. We will utilize a Decision Tree regression model to predict salary based on various features such as years of experience, education level, Country and more.

# Dataset
The Stack Overflow survey dataset is a comprehensive resource containing information about developers' demographics, education, work experience, and salary. By using this dataset, we can build a predictive model that accurately predict salary based on user-provided input. We scaled the salary column and fitted the model, then fitted the model again using the unscaled salary. In both cases, there wasn't a significant reduction in the error rate.

# Machine Learning Algorithm
To begin, we will preprocess the Stack Overflow survey dataset by handling missing values, encoding categorical variables. Next, we will split the dataset into training and testing sets to train our Random Forest regression model.

A Decision Tree is a powerful machine learning algorithm that combines multiple decision trees to make accurate predictions. It is well-suited for regression problems like salary prediction, as it can handle complex relationships between features and target variable. The root mean squared error for the Decision Tree turned out to be the lowest compared to other machine learning algorithms such as XGBoost and Random Forest Regression.

# Objective

The salary prediction webpage will provide users with a user-friendly interface where they can input their relevant details such as education, work experience, Country, Industry, Age Group, and Workspace. The webpage will then use the Random Forest regression model to process this information and generate a salary prediction for the user.

By developing this salary prediction webpage, I aim to provide a useful tool for both employers and job seekers in the different industry. Employers can use this tool to make competitive salary offers, while job seekers can use it to negotiate their salaries effectively.
