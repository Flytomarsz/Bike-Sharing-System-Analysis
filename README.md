# Bike Sharing System in 2012 for Registered User Only📊
## Project Background
Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return back at another position. The core dataset has two years historical log corresponding in 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA.

This dataset has significant differences between casual user and registrated user. This project thoroughly analyzes registrated user only in 2012 in order to increasing user's membership by identifying registrated user behavioral.

Python Notebook used to inspect and clean the data for this analysis can be found here [link].

An interactive Tableau dashboard used to report and explore sales trends can be found here [link].

## Business Questions
1. How is the user's segmentation in 2012?
2. How is the impact of rush hours (9 A.M - 5 P.M) for bike rental demand on weekdays in 2012 for registered user?
3. How much percentage of bycicle rental demand across seasons in 2012 for registered user?
4. How is the demand's pattern between casual and registered users across different seasons?

## Objectives
- **Customer's Segmentation:** Identify the the gap between casual user's total & registrated user's total, focusing on the majority, improving cutomer's experiences.
- **Peak Hours Optimization:** Budget optimization by identifying total of bike deployment during peak hours on weekday as the most busiest daily time across different seasons.
- **Demand Across Seasons :** Budget optimization by identifying total of bicycle deployment during the most high demand bike rental across different seasons.
- **Seasonal Deep Analysis:** Using Clustering Analysis for identify bike rental's demand for each seasons.

## Scope
- ```dteday``` : date
- ```season``` : season (1:springer, 2:summer, 3:fall, 4:winter)

## Executive Summary
![image](https://github.com/user-attachments/assets/ad500897-6e92-450d-af9c-3b2c7e39a7cd)


## Analysis Results & Insights
### How is the user's segmentation in 2012?
1. Registered user are the majority than the casual useres.
2. The high percentage of registered user indicates that bike rental services successfully optimizing user's membership retention, fostering long-term relationships. This might reflect positively on customer satisfaction.

### How is the impact of rush hours (9 A.M - 5 P.M) for bike rental demand on weekdays in 2012 for registered user?
1. The line chart reveals two distinct peak periods: around **9 AM** and around **5 PM**. These spikes correspond to typical commuting hours, indicating bike rentals are primarily used by individuals commuting to work or school during this period. This suggests that bike rentals are heavily utilized as a convenient mode of transportation during daily rush hours.

### How much percentage of bycicle rental demand across seasons in 2012 for registered user?
1. **Summer** (Season 3) has the **highest percentage** of bicycle rental demand among registered users in 2012, accounting for approximately 30.46% of the total rentals.
2. **Spring** (Season 2) and **Fall** (Season 4) have comparable demand, with 26.56% and 26.15%, respectively.
3. **Winter** (Season 1) shows the lowest demand for bicycle rentals, contributing only 16.83% to the total. This trend indicates that warmer seasons (Spring and Summer) tend to have higher bicycle rental activity, likely due to favorable weather conditions, while colder seasons like Winter exhibit significantly lower activity.

### Clutering Analysis: How is the demand's pattern between casual and registered users across different seasons?
1. **Cluster 0**, which includes **Summer** (cnt = 208.3) and **Winter** (cnt = 198.9), reflects **moderate** bike rental activity.
2. **Cluster 1** (**Spring**) has the **lowest average** bike rentals (cnt = 111.1) compared to other clusters, likely indicating reduced cycling activity during this season. In contrast.
3. **Cluster 2** (**Fall**) shows the **highest average** bike rentals (cnt = 236.0), suggesting Fall is the most active season for bike usage. This pattern might be influenced by seasonal factors such as weather and user preferences for outdoor activities.
