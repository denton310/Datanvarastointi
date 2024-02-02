create database if not exists iot;
use iot;


create external table if not exists smart (
device_id string,
date_time string,
A3_16_dB_level float,
A3_16_Vais_CO2 float,
A3_16_Vais_Rel_HUM float,
A3_16_Vais_TEMP float,
BME280_AirP float,
BME280_Hum float,
BME280_temp float,
MH_Z16_CO2 float,
Ref_light float,
SP30_CO2 float,
SP30_ethanol float,
SP30_H2 float,
SP30_TVOC float
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile 
location 'smart';

load data local inpath 'smart.csv' OVERWRITE into table smart;
