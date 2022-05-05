Tableau Public Dashboard:  https://public.tableau.com/views/CitiBikesNYCdataanalysis/CitiBikeStory?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link


## Data ##

File Source: https://s3.amazonaws.com/tripdata/index.html
File Used: May 2019 Data, random sample (20%)
Description on Record: https://ride.citibikenyc.com/system-data

The data was reviewed using pandas. It originally contained 1924563 entries. 

Gender was label encoded and so was replaced with their string values as described by CitiBike for easy data handling.

No null value rows or unknown genders were removed from the data set. A true sampling of City Bike bike history would contain the surveys with bad user inputted data, as "bad" can not be defined by an analyst.


## Design Decisons ##
The visualizations are created with primarily light backgrounds and red and blue design colors. This fits with the CitiBikeNYC logo, as showing in the link below.

https://citibikenyc.com/

Additionally, most axis have been fixed for charts. This was decided on for easier visual comparison as filters are toggled to different settings. If the axis adjusts proportionally, then the human eye would be hard pressed to see the data changes on the screen. 

# Analysis #

## Demographics by Gender and User Type ##
There are far more male users (approximately 3 times more) than there are female users. 

Additionally, subscribers dominate bike usage, at about 10 times the number of subscribers to users. This is likely due to ease of use-- it is much faster for a subscriber to procure a bike than it is a customer (or at least perceived to be so). A change in marketing or pricing may be needed to adjusted to make the bikes more accessible to customers. 

In the year 2019, most users where older than 25 years old. In fact, when Unknown Gender is ignored, birth years 1987-1993 take up the top 6 spots.

## Popular Bike Usage Times ##
The heaviest travel tends to occur between 17-18 hundred hours for both starting and ending rides. For most days of the month of May, over 2,000 rides occur in this time period.

This makes sense as it is a rush hour for many, especially for those who are traveling to/from the city and are rushing home, to their main mode of transport or to their night activity, as other modes of transport (the subway, buses, and train schedules) are on tight time tables.

If you use the toggles, you would see that this phenomenon occurs for both starting stations and end stations, likely because travels are fast on average (less than 10 minutes at hour 17, on average).

## Map of Stations ##
The CitiBikeNYC stations are in the heavy trafficked areas in New York City. As the "Count of Time Station was Used" filter is adjusted to show lesser used stations, the featured stations show start explode outward into the outer boroughs of the city, with a center about roughly centering around 1003. This phenomenon occurs for both recorded starting and ending stations.

The reason for this is evident when you look at the station names. The more used stations are in popular tourist attaction areas.



## Extra Resources ##
https://datatofish.com/replace-values-pandas-dataframe/
https://datascienceparichay.com/article/pandas-random-sample-of-rows/
https://www.educba.com/tableau-dual-axis/




