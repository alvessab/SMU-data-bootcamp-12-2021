Tableau Public Dashboard: 

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

Additionally, all axis have been fixed for charts. This was decided on for easier visual comparison as filters are toggled to different settings. If the axis adjusts proportionally, then the human eye would be hard pressed to see the data changes on the screen. 

# Analysis #

## Demographics by Gender and User Type ##


## Popular Bike Usage Times ##


## Map of Stations ##
The Citi



## Resources ##
https://datatofish.com/replace-values-pandas-dataframe/
https://datascienceparichay.com/article/pandas-random-sample-of-rows/
https://www.educba.com/tableau-dual-axis/




