# Building ETL Pipeline using Python and Airflow

*This project is inspired by [Spotify_etl](https://github.com/sidharth1805/Spotify_etl) and acts as a practice for Apache Airflow* 


# Building ETL Pipeline

## Source
This project extract data from Singapore [4 days weather forecast API](https://beta.data.gov.sg/datasets/1456/resources/d_1efe4728b2dad26fd7729c5e4eff7802/view#resources). 

### Extract function: 
We will extract the weather forecast, along with the highest and lowest temperatures, for the current day and the next three days. This information will then be organized and placed into a Pandas Dataframe.

### Transform function:
Transform the date column to Pandas Datetime datatype. 

# Automating through Airflow