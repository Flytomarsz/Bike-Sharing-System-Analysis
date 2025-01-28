# Bike Sharing System in 2012 for Registered User Only📊
## Project Background
Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return back at another position. The core dataset has two years historical log corresponding in 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA.

This dataset has significant differences between casual user and registrated user. This project thoroughly analyzes registrated user only in 2012 in order to increasing user's membership by identifying registrated user behavioral.

Python Notebook used to inspect, cleaning data, and executive summary for this analysis can be found here [(https://github.com/Flytomarsz/Bike-Sharing-System-Analysis/blob/main/Proyek_Analisis_Data%20(1).ipynb)].

An interactive dashboard using Streamlit apps to report and explore bike rental behavioral can be found here [link].

## Business Questions
1. How is the user's segmentation in 2012?
2. How is the impact of rush hours (9 A.M - 5 P.M) for bike rental demand on weekdays in 2012 for registered user?
3. How much percentage of bycicle rental demand across seasons in 2012 for registered user?
4. How is the demand's pattern between casual and registered users across different seasons?

## Dataset
The ```Bike-sharing-dataset.zip``` taken from [https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset], contains:
- ```day.csv```: day.csv - bike sharing counts aggregated on daily basis. Records: 731 days
- ```hour.csv```: hour.csv : bike sharing counts aggregated on hourly basis. Records: 17379 hours

## Objectives
- **Customer's Segmentation:** Identify the the gap between casual user's total & registrated user's total, focusing on the majority, improving cutomer's experiences.
- **Peak Hours Optimization:** Budget optimization by identifying total of bike deployment during peak hours on weekday as the most busiest daily time across different seasons.
- **Demand Across Seasons :** Budget optimization by identifying total of bicycle deployment during the most high demand bike rental across different seasons.
- **Seasonal Deep Analysis:** Using Clustering Analysis for identify bike rental's demand for each seasons.

## Scope
- ```casual```: count of casual users
- ```registered```: count of registered users
- ```cnt```: count of total rental bikes including both casual and registered
- ```dteday``` : date
- ```season``` : season (1:springer, 2:summer, 3:fall, 4:winter)
- ```yr``` : year (0: 2011, 1:2012)
- ```mnth``` : month ( 1 to 12)
- ```hr``` : hour (0 to 23)
- ```weekday``` : day of the week
- ```weathersit``` : 
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

## Tools
- **Python**: Data manipulation & analysis.
- **Jupyter Notebook**: Environtment for executing python script.
- **Matplotlib** and **Seaborn**: For data visualisation.
- **Panda** and **Scikit Learn**: For data processing and exploratory data analysis (EDA).

## Key Findings
1. There's big gap between casual user and registrated user, probably because of customer retention.
2. Peak hours and Season give a big impact for bike demand & tracking bike deployment in order to saving costs.
3. With the trackable bike demand, the company could saving cost by spending sufficient funds.

## Analysis Results
### How is the user's segmentation in 2012?
1. Registered user are the majority with total 1,676,811 users than the casual users in total 372,765 users.
2. The high percentage of registered user indicates that bike rental services successfully optimizing user's membership retention, fostering long-term relationships. This might reflect positively on customer satisfaction.

### How is the impact of rush hours (9 A.M - 5 P.M) for bike rental demand on weekdays in 2012 for registered user?
1. The line chart reveals two distinct peak periods: around **9 AM** and around **5 PM**. These spikes correspond to typical commuting hours, indicating bike rentals are primarily used by individuals commuting to work or school during this period. This suggests that bike rentals are heavily utilized as a convenient mode of transportation during daily rush hours.

### How much percentage of bycicle rental demand across seasons in 2012 for registered user?
1. **Summer** (Season 3) has the **highest percentage** of bicycle rental demand among registered users in 2012, accounting for approximately 30.46% of the total rentals.
2. **Spring** (Season 2) and **Fall** (Season 4) have comparable demand, with 26.56% and 26.15%, respectively.
3. **Winter** (Season 1) shows the **lowest demand** for bicycle rentals, contributing only 16.83% to the total.
4. This trend indicates that warmer seasons (Spring and Summer) tend to have higher bicycle rental activity, likely due to favorable weather conditions, while colder seasons like Winter exhibit significantly lower activity.

### Clutering Analysis: How is the demand's pattern between casual and registered users across different seasons?
1. **Cluster 0**, which includes **Summer** (cnt = 208.3) and **Winter** (cnt = 198.9), reflects **moderate** bike rental activity.
2. **Cluster 1** (**Spring**) has the **lowest average** bike rentals (cnt = 111.1) compared to other clusters, likely indicating reduced cycling activity during this season. In contrast.
3. **Cluster 2** (**Fall**) shows the **highest average** bike rentals (cnt = 236.0), suggesting Fall is the most active season for bike usage. This pattern might be influenced by seasonal factors such as weather and user preferences for outdoor activities.

## Insights 
1. Maintaining bike conditions in both high demand & low demand is a better step to spend funds without wasting it on unessecary things.
2. Ensuring the number of bike deployment on crucial time such peak hours on weekday & during warm seasons is a good steps to maintaining bike conditions.
3. To maintaining user retention, i suggest to choose the bike replacement system by buying a new one or servicing the damaged bike.
4. Create a system or schedule for replacing the used bike with the bike that have been serviced in order to keeping the bike in good condition.
