# Grace De Geus Homework 4

1. What time range does your data cover?  How many rows are there total?
	The time range of this dataset covers from  to  . This was determined by finding the first (minimum) pickup time and the last (maximum) dropoff time for the whole month.
```
	#Item number 1, assuming the first pickup is the beginning of the timeframe, and the last dropoff is the end
            try:
                datetime_min = datetime.strptime(pickup_datetime, datetime_format)
            except : 
                error_row += 1
                
            try:
                datetime_max = datetime.strptime(dropoff_datetime, datetime_format)
            except : 
                error_row += 1
```				
There are a total of  rows in the csv file. This was calculated simply by incrementing a counter for every row processed in the main loop.
    `row_total += 1`
2. What are the field names?  Give descriptions for each field.
The field names are as follows: 
- medallion = Is the identifier for the cab itself
- hack_license =  Allows someone to drive a taxicab, this gives the driver permission
- vendor_id = Identification of some sort, couldn't find a definition
- rate_code = Determines what rate is charged for the fare, it determines the pricing
- store_and_fwd_flag = Indicates whether the trip record was held in vehicle memory before sending to the vendor
- pickup_datetime = When the fare was picked up
- dropoff_datetime = When the fare was dropped off
- passenger_count = Number of passengers per fare
- trip_time_in_secs = The duration of the fare
- trip_distance = The distance of the fare in miles
- pickup_longitude = Location of fare pickup, longitude
- pickup_latitude = Location of fare pickup, latitude
- dropoff_longitude = Location of the fare dropoff, longitude
- dropoff_latitude = Location of the fare dropoff, latitude
This is determined by printing the first row consumed by the script

3. Give some sample data for each field.
	- medallion = FE7B354FEB67B9C94BD34EA54469691C
	- hack_license = 2C78614ADC9C602EC70D65CCB4E63B14
	- vendor_id = CMT
	- rate_code = 1 
	- store_and_fwd_flag = N 
	- pickup_datetime = 2013-03-01 00:00:04 
	- dropoff_datetime = 2013-03-01 00:19:03 
	- passenger_count = 1
	- trip_time_in_secs = 1138
	- trip_distance = 14.30
	- pickup_longitude = -73.776703 
	- pickup_latitude = 40.645164 
	- dropoff_longitude = -73.913925 
	- dropoff_latitude = 40.772614 

4. What MySQL data types would you need to store each of the fields?
	- medallion = varchar
	- hack_license = varchar
	- vendor_id = varchar
	- rate_code = int 
	- store_and_fwd_flag = varchar 
	- pickup_datetime = datetime 
	- dropoff_datetime = datetime 
	- passenger_count = int
	- trip_time_in_secs = int
	- trip_distance = decimal
	- pickup_longitude = decimal 
	- pickup_latitude = decimal 
	- dropoff_longitude = decimal 
	- dropoff_latitude = decimal 

5. What is the geographic range of your data (min/max - X/Y)?
I assumed that only valid lat and long data was within 1 degree of the real coordinates of NYC.
Minimum is 39.516666, -74.5
Maximum is 40.5, -73.5
  ![Map of lat and long](/map.png)
Note: I also seemed to get this wrong after much effort and ran out of time.
6. What are the distinct values for each field? (If applicable)
    - vendor_id = CMT, VTS
    - rate_code = 1, 2, 5, 3, 4, 6, 0, 210, 9, 7, 8, 17
    - store_and_fwd_flag = N, Y
    - passenger_count = 1, 2, 4, 3, 5, 6, 0, 9, 7, 255

7. For other numeric types besides lat and lon, what are the min and max values?
    - The minimum rate code is 0
    - The maximum rate code is 9
    - The minimum passenger count is 0
    - The maximum passenger count is 9 
    - The minimum trip time is 0
    - The maximum trip time is 9
    - The minimum trip distance is .00 
    - The maximum trip distance is 98.80
	Note: I honestly just didn't have time to sanitize this data and look into it.
	
8. Create a chart which shows the average number of passengers each hour of the day.
  ![Graph of all passenger data](/passenger.png)
  
9. Create a new CSV file which has only one out of every thousand rows.
This file is included in the repository, titled every_thousandth_row.csv.

10. Repeat step 8 with the reduced dataset and compare the two charts.
![Graph of subset of passenger data](/passenger.png)

Overall the charts look very similar, the popularity of taxis appears to be consistent accross the month. The highest demand is between 19:00 and 20:00, with a dip around 16:00 every day. Similarly, in the morning hours, there is a consistent drop from midnight to 5:00, where the traffic begins to pick up again, presumably due to morning commuter traffic.