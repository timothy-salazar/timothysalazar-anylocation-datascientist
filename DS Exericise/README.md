# Warwick - Data Science Challenge

There are three challenges below, and you will only be tasked on completing two of the three. 

If you're not having fun doing these challenges, maybe you are not a good fit for the position because the data scientists at Warwick are tackling very similar challenges every day. 

## Rules

- Use Python 3.x

- Responses to each challenge will be inside a folder entitled **ds-{challengenumber}**.

- Store all provided or procured data in a PostgreSQL database with the apprpriate primary and foreign key relations as needed. Provide a PG dump of your database.

- Transparency and reproducibility of results and analysis are important to us. Your work should be clean, succinctly commented, and easy to follow.

- The entire set of queries, transforms, visualizations, and models leading up to the write-up should be contained in a Jupyter Notebook and be up to date with the results.

- Conduct exploratory data analysis and data visualization. Please note any interesting relationships in the data.

- Fit many machine learning models and find the most accurate predictor using the cost function of choice. Explain why your model and cost function was appropriate.

- Test and validate your model appropriately and comment on the results. Please note the method of how you validated your model.  

### Challenge 1 - Regression 

There is a target variable in the dataset [regression.zip](assets/regression.zip) called **Price**. Please create a model that predicts **Price** given a set of observed regressors.

### Challenge 2 - Time Series 

Please create a model that predicts the **Wilshire US REIT Index** (WILLREITIND) given a set of time series of your choice. WILLREITIND is available on [FRED](https://fred.stlouisfed.org/series/WILLREITIND); this is your regressand. Take some time to visit the [FRED](https://fred.stlouisfed.org/) website and browse through the regressors you would like to capture. Then utilize the FRED API to collect 4 time series (i.e. regressors of choice) and create a time series model which forecasts 1-year WILLREITIND, resampling to daily resolution (365 predictions).

### Challenge 3 - Classification

The aliens have raided the office and wiped out everything in the database, leaving Warwick only these [datasets](assets/classification.zip). Suppose that Warwick has ~$100 million left to invest in its current fund. 

After thoroughly analyzing the data and modeling, come up with one investable asset and label each county as **SELL**, **HOLD** or **BUY** rating for that asset. For example, your classification model may output BUY for class A office properties in Maricopa County, AZ but output SELL for Oklahoma County, OK.
 
