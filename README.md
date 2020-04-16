# coronaPrediction
A journey with Cindy and Aaron as we attempt to identify effective measures of containing COVID-19 and predict its future trajectory

Part A- Identify Regions That Effectively Slowed COVID-19 Spread
Step 1: Cluster regions by population density and contact with other regions (number of transportation trips in and out of region)
Step 2: Within each cluster, plot |final_daily_growth_rate - peak_daily_growth_rate| against time_in_between and cluster to find regions that effectively slowed the spread of COVID-19.  
Step 3: Prediction Model for future cases in regions using Linear Regression on current growth rate trajectory 

Part B- Identify Effective Measures for Slowing COVID-19 Spread
Step 1: Linear Regression between change_in_daily_growth_rate after start date of first measure implemented and measures_used 
Step 2: Find effective preventative measures ie. higher negative coefficients
Step 3: Prediction Model of future cases if selected measures are used in selected region

Step 5: Add in political data ?
Step 6:
Step *: Use Neural Networks to predict models


