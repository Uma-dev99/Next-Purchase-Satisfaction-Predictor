# Next-Purchase-Satisfaction-Predictor
The "Next Purchase Satisfaction Predictor" is a machine learning project designed to forecast customer satisfaction scores for future orders based on historical e-commerce data. By analyzing past customer interactions, order details, and review feedback, the project aims to predict how satisfied a customer will be with their next purchase.
# Dataset:

The project utilizes the Brazilian E-Commerce Public Dataset by Olist, which includes detailed records of 100,000 orders from 2016 to 2018. This dataset encompasses various attributes such as order status, price, payment methods, freight performance, customer locations, product attributes, and customer reviews.

# Key Components:

Data Ingestion and Cleaning:

Import and preprocess the dataset to create a clean and structured DataFrame.
Handle missing values, remove unnecessary columns, and prepare features for modeling.
Model Training:

Develop and train a machine learning model to predict customer satisfaction scores.
Utilize MLflow for tracking experiments, logging model parameters, and saving the trained model.
Model Evaluation:

Assess the performance of the trained model using appropriate metrics.
Log evaluation results with MLflow and determine if the model meets deployment criteria.
Continuous Deployment:

Implement a deployment pipeline to continuously update and deploy the model based on new data and performance evaluations.
Use MLflow for model deployment and tracking, ensuring that the most accurate model is used for predictions.
Streamlit Application:

Create an interactive web application using Streamlit to showcase the model's predictions.
Allow users to input features for a product and receive predicted satisfaction scores.
Technologies:

**ZenML:** For building and managing the machine learning pipeline, ensuring seamless integration and automation of the end-to-end workflow.
<br>**MLflow:** For experiment tracking, model management, and deployment.
<br>**Streamlit:** For developing an interactive interface to display predictions and engage users.

# Workflow:

## Train the Model:

Execute the training pipeline to process data, train the model, and evaluate its performance.

## Deploy the Model:

Run the deployment pipeline to update and deploy the model if it meets performance thresholds.

## Interact with the Model:

Use the Streamlit application to input new data and obtain predictions from the deployed model.

## Outcome:

The "Next Purchase Satisfaction Predictor" provides valuable insights into customer satisfaction, helping e-commerce businesses anticipate and improve the customer experience for future purchases. By leveraging advanced machine learning techniques and robust deployment practices, the project aims to enhance decision-making and drive better business outcomes.
