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

# Explore Page

The Stack Overflow survey dataset's exploratory data analysis (EDA) explore page was made in order to offer insightful information on the respondents' salaries and demographics. There would be multiple visualizations on this page. A pie chart representing the number of individuals based on nations would graphically reflect the distribution of survey respondents, providing a clear image of the geographic diversity. A bar chart displaying the mean income based on countries would highlight the average compensation across different regions. An overview of the dataset would be provided by a bar chart showing the mean salary by industry, which would enable users to understand the relationship between location, industry, and salary. We found out that majority of the survey was done by US employee and the maximum number of people working in the IT industry. This would help determine which industries offer higher or lower salaries. 

# Conclusion
In conclusion, our project effectively utilized the Stack Overflow survey dataset to build predictive models for salary estimation and conducted exploratory data analysis to uncover valuable insights. Using Python along with libraries like pandas for data manipulation, scikit-learn for model training (including Decision Trees for accurate salary predictions), and matplotlib for visualization, we successfully analyzed mean salary distributions across different countries and industries. We employed the pickle library to serialize trained models for deployment and leveraged Streamlit for creating an interactive web-based explore page. This allowed users to dynamically explore and visualize survey data, including a pie chart showcasing the geographic distribution of survey respondents and also to predict the salary given the certain inputs from the user. Overall, the project highlights the robustness of Decision Trees in predictive modeling and demonstrates the utility of pickle and Streamlit for model serialization and interactive data exploration.

