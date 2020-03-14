#Homework number 4 titled "Big Data Inspection - NYC Taxi Trips - Part 1"
# By Grace De Geus
#---------------------------------------------


import csv
import time
from datetime import datetime

start = time.time()




#Open File to read data
fn = 'trip_data_3.csv'
f = open(fn, "r")
reader = csv.reader(f)

#Initialize variables
latitude_min = None
latitude_max = None
longitude_min = None
longitude_max = None
datetime_min = None
datetime_max = None
datetime_format = '%Y-%m-%d %H:%M:%S'
error_row = 0

#Colomn headers:
#"medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, 
#passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, 
#dropoff_latitude"
vendor_id_histogram  = {}
rate_code_histogram = {}
store_and_fwd_flag_histogram = {}
passenger_count_histogram = {}
passenger_perhour_histogram = {}
passenger_perhour_histogram2 = {}

row_total = 0

#For Item number 8
#f1 = open('datetime_data_item8.csv','w')
#writer1 = csv.writer(f1, delimiter=',',lineterminator='')

#For Item number 9
f2 = open('every_thousandth_row.csv','w')
writer2 = csv.writer(f2, delimiter=',',lineterminator='')
writer2.writerow("")
f2.close()

#For Item number 9
f2 = open('every_thousandth_row.csv','a')
writer2 = csv.writer(f2, delimiter=',',lineterminator='\n')

#enumerate gives us two iterator items i - row count and row which is data list
for i, row in enumerate(reader):
    medallion = row[0]
    hack_license = row[1]
    vendor_id = row[2]
    rate_code = row[3]
    store_and_fwd_flag = row[4]
    pickup_datetime = row[5]
    dropoff_datetime = row[6]
    passenger_count = row[7]
    trip_time_in_secs = row[8]
    trip_distance = row[9]
    pickup_longitude = row[10]
    pickup_latitude = row[11]
    dropoff_longitude = row[12]
    dropoff_latitude = row[13]
    
    #Write header to file for Item 2 and 9
    if row_total == 0:
        writer2.writerow(row)
        
    #Skip the header
    if row_total > 0: 
        #Histograms (distinct values) of all applicable fields          
        if vendor_id not in vendor_id_histogram.keys():
            vendor_id_histogram[vendor_id] = 1
        else:
            vendor_id_histogram[vendor_id] += 1
        
        if rate_code not in rate_code_histogram.keys():
            rate_code_histogram[rate_code] = 1
        else:
            rate_code_histogram[rate_code] += 1
            
        if store_and_fwd_flag not in store_and_fwd_flag_histogram.keys():
            store_and_fwd_flag_histogram[store_and_fwd_flag] = 1
        else:
            store_and_fwd_flag_histogram[store_and_fwd_flag] += 1
        
        if passenger_count not in passenger_count_histogram.keys():
            passenger_count_histogram[passenger_count] = 1
        else:
            passenger_count_histogram[passenger_count] += 1
        
        
        
        #Initialize min/max data
        if row_total == 1: 
            #Item number 1, assuming the first pickup is the beginning of the timeframe, and the last dropoff is the end
            try:
                datetime_min = datetime.strptime(pickup_datetime, datetime_format)
            except : 
                error_row += 1
                
            try:
                datetime_max = datetime.strptime(dropoff_datetime, datetime_format)
            except : 
                error_row += 1
                
            print("Item number 3:")
            print(row)
            
            #Latitude and Longitude, initialize to pickup data, start comparison to dropoff data
            
            #Minimums
            good_pickup_latitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_latitude = round(float(pickup_latitude),2)
            except : 
                error_row += 1
            if good_pickup_latitude != None :
                if good_pickup_latitude >= 39 and good_pickup_latitude <= 41 :
                    latitude_min = pickup_latitude
                    
            good_pickup_latitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_latitude = round(float(pickup_latitude),2)
            except : 
                error_row += 1
            if good_pickup_latitude != None :
                if good_pickup_latitude >= 39 and good_pickup_latitude <= 41 :
                    if dropoff_latitude < latitude_min:
                        latitude_min = dropoff_latitude
            
            good_pickup_longitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_longitude = round(float(pickup_longitude),2)
            except : 
                error_row += 1
            if good_pickup_longitude != None :
                if good_pickup_longitude >= -75 and good_pickup_longitude <= -73:       
                    longitude_min = pickup_longitude
            
            
            good_pickup_longitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_longitude = round(float(pickup_longitude),2)
            except : 
                error_row += 1
            if good_pickup_longitude != None :
                if good_pickup_longitude >= -75 and good_pickup_longitude <= -73: 
                    if dropoff_longitude < longitude_min:
                        longitude_min = dropoff_longitude
                        
            #Maximums
            good_pickup_latitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_latitude = round(float(pickup_latitude),2)
            except : 
                error_row += 1
            if good_pickup_latitude != None :
                if good_pickup_latitude >= 39 and good_pickup_latitude <= 41 :
                    latitude_max = pickup_latitude
                    
            good_pickup_latitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_latitude = round(float(pickup_latitude),2)
            except : 
                error_row += 1
            if good_pickup_latitude != None :
                if good_pickup_latitude >= 39 and good_pickup_latitude <= 41 :
                    if dropoff_latitude < latitude_max:
                        latitude_max = dropoff_latitude
            
            good_pickup_longitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_longitude = round(float(pickup_longitude),2)
            except : 
                error_row += 1
            if good_pickup_longitude != None :
                if good_pickup_longitude >= -75 and good_pickup_longitude <= -73:       
                    longitude_max = pickup_longitude
            
            
            good_pickup_longitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_longitude = round(float(pickup_longitude),2)
            except : 
                error_row += 1
            if good_pickup_longitude != None :
                if good_pickup_longitude >= -75 and good_pickup_longitude <= -73: 
                    if dropoff_longitude < longitude_max:
                        longitude_max = dropoff_longitude

            
        else:       
            #Find passenger_count per hour for item 8
            good_datetime = None
            try :
                good_datetime = datetime.strptime(pickup_datetime, datetime_format)
            except :
                error_row += 1
            if good_datetime != None:
                good_datetime.hour
                if good_datetime.hour not in passenger_perhour_histogram.keys():
                    passenger_perhour_histogram[good_datetime.hour] = 0
                else:
                    passenger_perhour_histogram[good_datetime.hour] += int(passenger_count)
            
            
            #Find Datetime range For item number 1
            good_datetime = None
            try :
                good_datetime = datetime.strptime(pickup_datetime, datetime_format)
            except :
                error_row += 1
            if good_datetime != None:
                if good_datetime < datetime_min:
                    datetime_min = good_datetime
            
            good_datetime = None
            try :
                good_datetime = datetime.strptime(dropoff_datetime, datetime_format)
            except :
                error_row += 1
            if good_datetime != None:
                if good_datetime > datetime_max:
                    datetime_max = good_datetime

          
            #Latitude and Longitude manipulation - sanity check for locations in NYC ~40 degrees N by -74 degrees W
            good_pickup_longitude = None
            #Sanitize for non-numeric values
            try : 
                good_pickup_longitude = round(float(pickup_longitude),2)
            except : 
                error_row += 1
            key = pickup_longitude
            if good_pickup_longitude != None :
                if good_pickup_longitude >= -75 and good_pickup_longitude <= -73:
                    #Capture min and max for pickup_longitude     
                    if key < longitude_min:
                        longitude_min = key
                    elif key > longitude_max:
                        longitude_max = key
                else:
                    good_pickup_longitude = None
                    
            good_pickup_latitude = None
            try : 
                good_pickup_latitude = round(float(pickup_latitude),2)
            except : 
                error_row += 1
            key = pickup_latitude
            if good_pickup_latitude != None :
                if good_pickup_latitude >= 39 and good_pickup_latitude <= 41 :
                    #Capture min and max for pickup_latitude
                    if key < latitude_min:
                        latitude_min = key
                    elif key > latitude_max:
                        latitude_max = key
                else:
                    good_pickup_latitude = None
                    
            good_dropoff_longitude = None
            try : 
                good_dropoff_longitude = round(float(dropoff_longitude),2)
            except : 
                error_row += 1
            key = dropoff_longitude
            if good_dropoff_longitude != None :
                if good_dropoff_longitude >= -75 and good_dropoff_longitude <= -73:
                    #Capture min and max for dropoff_longitude    
                    if key < longitude_min:
                        longitude_min = key
                    elif key > longitude_max:
                        longitude_max = key
                else:
                    good_dropoff_longitude = None
                    
            good_dropoff_latitude = None
            try : 
                good_dropoff_latitude = round(float(dropoff_latitude),2)
            except : 
                error_row += 1
            key = dropoff_latitude
            if good_dropoff_latitude != None :
                if good_dropoff_latitude >= 39 and good_dropoff_latitude <= 41 :            
                    #Capture min and max for dropoff_latitude
                    if key < latitude_min:
                        latitude_min = key
                    elif key > latitude_max:
                        latitude_max = key
                else:
                    good_dropoff_latitude = None
    
    if row_total > 0 and row_total % 1000 == 0:
        writer2.writerow(row)        
    row_total += 1

f.close()
#f1.close()
f2.close()

print("Item number 1:")
print(datetime_min)
print(datetime_max)

print("Item number 8:")
print(passenger_perhour_histogram)

fn = 'every_thousandth_row.csv'
f = open(fn, "r")
reader = csv.reader(f)

for i, row in enumerate(reader):
    #Find passenger_count per hour for item 10
    pickup_datetime = row[5]
    good_datetime = None
    try :
        good_datetime = datetime.strptime(pickup_datetime, datetime_format)
    except :
        error_row += 1
    if good_datetime != None:
        good_datetime.hour
        if good_datetime.hour not in passenger_perhour_histogram2.keys():
            passenger_perhour_histogram2[good_datetime.hour] = 0
        else:
            passenger_perhour_histogram2[good_datetime.hour] += int(passenger_count)


print("Item number 10:")
print(passenger_perhour_histogram2)


print("Item number 5:")
print("The minimum latitude is " + str(latitude_min))
print("The maxmimum pickup latitude is " + str(latitude_max))

print("The minimum dropoff longitude is " + str(longitude_min))
print("The maxmimum dropoff longitude is " + str(longitude_max))

print("Item number 6:")
print(vendor_id_histogram)
print(rate_code_histogram)
print(store_and_fwd_flag_histogram)
print(passenger_count_histogram)



print(time.time() - start) 
f.close()
#f1.close()

