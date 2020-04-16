import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime as dt
from datetime import date

#Load in corona datasets
global_countermeasure_data = pd.read_csv("C://Users/ticto/Downloads/coronaPrediction-master/coronaPrediction-master/countermeasures_db_johnshopkins.csv")

global_corona_cases_daily = pd.read_csv("C:/Users/ticto/Downloads/coronaPrediction-master/coronaPrediction-master/cases_around_the_world.csv")

#Store Corona cases as percent of total population
global_corona_cases_daily_percent = global_corona_cases_daily.copy()

#Store daily increase in cases
global_corona_cases_daily_increase = global_corona_cases_daily.copy()

    #Columns with daily cases
cols_to_map = ['1/22/20', '1/23/20', '1/24/20',
       '1/25/20', '1/26/20', '1/27/20', '1/28/20', '1/29/20', '1/30/20',      
       '1/31/20', '2/1/20', '2/2/20', '2/3/20', '2/4/20', '2/5/20', '2/6/20', 
       '2/7/20', '2/8/20', '2/9/20', '2/10/20', '2/11/20', '2/12/20',
       '2/13/20', '2/14/20', '2/15/20', '2/16/20', '2/17/20', '2/18/20',
       '2/19/20', '2/20/20', '2/21/20', '2/22/20', '2/23/20', '2/24/20',
       '2/25/20', '2/26/20', '2/27/20', '2/28/20', '2/29/20', '3/1/20',
       '3/2/20', '3/3/20', '3/4/20', '3/5/20', '3/6/20', '3/7/20', '3/8/20',
       '3/9/20', '3/10/20', '3/11/20', '3/12/20', '3/13/20', '3/14/20',
       '3/15/20', '3/16/20', '3/17/20', '3/18/20', '3/19/20', '3/20/20',
       '3/21/20', '3/22/20', '3/23/20', '3/24/20', '3/25/20', '3/26/20',
       '3/27/20', '3/28/20', '3/29/20', '3/30/20', '3/31/20', '4/1/20',
       '4/2/20', '4/3/20', '4/4/20', '4/5/20', '4/6/20', '4/7/20', '4/8/20',
       '4/9/20', '4/10/20', '4/11/20', '4/12/20', '4/13/20', '4/14/20',
       '4/15/20']

    #loop through every column with daily case
for j in range(len(cols_to_map)):

    #loop thorugh every row in column
    for i in range(len(global_corona_cases_daily)):
        
        #store daily case number as percent of population
        global_corona_cases_daily_percent.loc[i, cols_to_map[j]] = (float(global_corona_cases_daily_percent.loc[i, cols_to_map[j]]) / float(global_corona_cases_daily_percent.loc[i, 'Population'])) * 100

        #store daily case number as daily increase (except for day 1)
        if j > 0:
            global_corona_cases_daily_increase.loc[i, cols_to_map[j]] = global_corona_cases_daily.loc[i, cols_to_map[j]] - global_corona_cases_daily.loc[i, cols_to_map[j-1]]

    #Dataframe with only daily increases
just_daily_increase = global_corona_cases_daily_increase[cols_to_map].copy()

    #Dataframe with country labels
country_names = global_corona_cases_daily['Country/Region'].copy()

    #Series of U.S. daily increases
US_daily_increase_series = just_daily_increase.iloc[202]

    #Peak day with max U.S. daily increase
US_max_daily_increase = US_daily_increase_series.idxmax()

    #Plot U.S. daily increase in cases
"""plt.plot(cols_to_map, global_corona_cases_daily_increase.loc[202, cols_to_map])
plt.title('U.S. daily increases in COVID-19 Cases')
plt.xlabel('Days')
plt.ylabel('Number of new COVID-19 Cases')
x_tick_locs = ['1/30/20','2/29/20','3/30/20', US_max_daily_increase]
plt.xticks(x_tick_locs, x_tick_locs)
plt.show()"""

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
    temp_daily_increase_series = just_daily_increase.iloc[i]

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
        peak_dateTime_object = dt.strptime(peak_day[i], '%m/%d/%y')

        #convert last day to dateTime object
        last_dateTime_object = dt.strptime(cols_to_map[len(cols_to_map)-1], '%m/%d/%y')

        #Find days since peak
        days_inbetween.append((last_dateTime_object-peak_dateTime_object).days)

#Plot number of days since peak against change in daily increase
plt.scatter(days_inbetween, change_in_daily_increase, alpha=0.2)
plt.xlabel('Number of days since peak COVID-19 spread')
plt.ylabel('Amount decreased in rate of daily COVID-19 spread since peak')
plt.ylim(bottom = 0)
plt.xlim(left = 0)
plt.show()

#Find most effective country at slowing COVID-19 spread
print(country_names[change_in_daily_increase.index(max(change_in_daily_increase))])