# Dicoding Collection Dashboard ✨

## Project Overview
This project aims to analyze product data through an end to end data analysis process starting from data gathering, data cleaning, exploratory data analysis, and business insight generation, which is then delivered through an interactive Streamlit dashboard

The dashboard helps users understand product characteristics, distribution across categories, and potential cost drivers related to product weight and dimensions

---

## Data Analysis Workflow
The analysis was conducted using the following steps

1. Data Gathering  
   The dataset was collected and loaded into a pandas DataFrame for analysis

2. Data Cleaning  
   - Missing values in numerical columns were handled using median imputation  
   - Missing values in categorical columns were filled with unknown  
   - No duplicate records were found in the dataset  

3. Outlier Handling  
   Outliers in numerical features were handled using the IQR based capping method to reduce the impact of extreme values while preserving all observations

4. Exploratory Data Analysis  
   - Descriptive statistics were analyzed for numerical features  
   - Product characteristics such as weight, dimensions, description length, and photos were explored  
   - Category based analysis was performed to identify dominant and cost intensive product groups  

5. Visualization and Business Analysis  
   Visual analysis was conducted to answer business questions related to logistics cost optimization and product characteristics

---

## Dashboard Features
The Streamlit dashboard provides

- Dataset overview and key metrics  
- Interactive exploration of numerical features  
- Visualization of top product categories based on average weight  
- Analysis of the relationship between product dimensions and weight  
- Category level insights to support business decision making  

---

## Project Structure
├── dashboard.py
├── requirements.txt
├── main_data.csv
├── notebook.ipynb


---

## Setup Environment - Anaconda
py -3.10 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


---

## Run Streamlit App
streamlit run dashboard.py
