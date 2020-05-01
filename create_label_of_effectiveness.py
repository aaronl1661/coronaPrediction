import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime as dt
from datetime import date

#Load in corona datasets
global_countermeasure_data = pd.read_csv("C://Users/ticto/Downloads/coronaPrediction-master/coronaPrediction-master/countermeasures_db_johnshopkins.csv")

global_corona_cases_daily = pd.read_csv("C:/Users/ticto/Downloads/coronaPrediction-master/coronaPrediction-master/cases_around_the_world.csv")

#Store Corona cases as percent of total population
global_corona_cases_daily_percent = global_corona_cases_daily.copy(deep=True)

#Store daily increase in cases
global_corona_cases_daily_increase = global_corona_cases_daily.copy(deep=True)

    #Columns with daily cases
cols_to_map = ['1/22/2020', '1/23/2020', '1/24/2020',
       '1/25/2020', '1/26/2020', '1/27/2020', '1/28/2020', '1/29/2020', '1/30/2020',      
       '1/31/2020', '2/1/2020', '2/2/2020', '2/3/2020', '2/4/2020', '2/5/2020', '2/6/2020', 
       '2/7/2020', '2/8/2020', '2/9/2020', '2/10/2020', '2/11/2020', '2/12/2020',
       '2/13/2020', '2/14/2020', '2/15/2020', '2/16/2020', '2/17/2020', '2/18/2020',
       '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020',
       '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020',
       '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020',
       '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020',
       '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020',
       '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020',
       '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020',
       '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020',
       '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020',
       '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020',
       '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', 
       '4/29/2020', '4/30/2020']

#loop through every column with daily case
for j in range(len(cols_to_map)):

    #loop thorugh every row in column
    for i in range(len(global_corona_cases_daily)):
        
        #store daily case number as percent of population
        global_corona_cases_daily_percent.at[i, cols_to_map[j]] = (float(global_corona_cases_daily.at[i, cols_to_map[j]]) / float(global_corona_cases_daily.at[i, 'Population'])) * 100

        #store daily case number as daily increase (except for day 1)
        if j > 0:
            global_corona_cases_daily_increase.at[i, cols_to_map[j]] = global_corona_cases_daily.at[i, cols_to_map[j]] - global_corona_cases_daily.at[i, cols_to_map[j-1]]

    #Dataframe with only daily increases
just_daily_increase = global_corona_cases_daily_increase[cols_to_map].copy(deep=True)

    #Dataframe with country labels
country_names = global_corona_cases_daily['Country/Region'].copy(deep=True)

    #Series of U.S. daily increases
France_daily_increase_series = just_daily_increase.iloc[123].copy(deep=True)

    #Peak day with max U.S. daily increase
France_max_daily_increase = France_daily_increase_series.idxmax()

    #Plot U.S. daily increase in cases
plt.figure()
plt.plot(cols_to_map, France_daily_increase_series)
plt.title('France daily increases in COVID-19 Cases')
plt.xlabel('Days')
plt.ylabel('Number of new COVID-19 Cases')
x_tick_locs = ['1/30/2020','2/29/2020', France_max_daily_increase]
plt.xticks(x_tick_locs, x_tick_locs)

#Find change in daily increase rate for all Countries/Regions

    #Store max daily increase, value and day
peak_daily_increases = []
peak_day = []

    #Store most recent daily increase
final_daily_increases = []

    #Store change in daily increase
change_in_daily_increase = []

    #loop through each row (country)
for i in range(len(just_daily_increase)):

    #Select country
    temp_daily_increase_series = just_daily_increase.iloc[i].copy(deep=True)

    #Store max daily increase of country
    peak_daily_increases.append(temp_daily_increase_series.max())

    #Store date of max increase
    peak_day.append(temp_daily_increase_series.idxmax())

    #Store final daily increase of country
    final_daily_increases.append(temp_daily_increase_series[len(temp_daily_increase_series)-1])

    #Store change in daily increase
    change_in_daily_increase.append(abs(final_daily_increases[i]-peak_daily_increases[i]))

#Find number of days between peak and final
days_inbetween = []

    #loop through each country
for i in range(len(change_in_daily_increase)):
        
        #convert peak day to dateTime object
        peak_dateTime_object = dt.strptime(peak_day[i], '%m/%d/%Y')

        #convert last day to dateTime object
        last_dateTime_object = dt.strptime(cols_to_map[len(cols_to_map)-1], '%m/%d/%Y')

        #Find days since peak
        days_inbetween.append((last_dateTime_object-peak_dateTime_object).days)

#Plot number of days since peak against change in daily increase
plt.figure()
plt.scatter(days_inbetween, change_in_daily_increase, alpha=0.2)
plt.xlabel('Number of days since peak COVID-19 spread')
plt.ylabel('Amount decreased in rate of daily COVID-19 spread since peak')
plt.ylim(bottom = 0)
plt.xlim(left = 0)
plt.show()

#Find most effective country at slowing COVID-19 spread
print(country_names[change_in_daily_increase.index(max(change_in_daily_increase))])
