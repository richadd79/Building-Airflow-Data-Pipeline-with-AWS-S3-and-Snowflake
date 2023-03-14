# Building Airflow Data Pipeline with AWS S3 and Snowflake

# Introduction
This project sought to build a scheduling data ppipeline to load data from S3 Bucket to modern data warehouse platform Snowflake.
To ochestrate such a data pipeline between S3 and Snowflake, Apache Airflow an open-source workflow management 
platform is used to author and manage this pipleine while installed on Docker.



# Dataset
The datasets used for this project is here [Tickets_Data](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjBTU1lBTWl0VExvVHg1aUxzNUFZYVRrM2xHUXxBQ3Jtc0tsaExOMGVqYVlRR1FhTjdiQTVuU3o4NWI0RWpUQXBZNlRWYUJpTmh1SElqeGlhYmtPaUJ5UHNBX1dDYXFhSVRkVFRTRUdqcFNEM0xHQlp0anFFWW00bjJ3REtjSGZpRmdqeHhtNTNYMDZqU2p4RjVkSQ&q=https%3A%2F%2Fdocs.aws.amazon.com%2Fredshift%2Flatest%2Fgsg%2Fsamples%2Ftickitdb.zip&v=BopMJPEH6AE) courtesy of Darshil Parmer, a [Youtuber](https://www.youtube.com/@DarshilParmar) and freelance Data Engineer.


# Tools
`Python` as the main pramming language used to write the etl pipeline.

`SQL` to construct sql statements for creation of database, tables and related setup.

`S3` as the main data source storage for the datasets.

`Snowflake` as the final destination data warehouse.

`Apache Airflow` for the orchestration of the data pipeline.

`Docker` as the platform to run the airflow containers.

# Database & SCHEMA Setup

Before the ETL, firstly we need to setup the following up in Snowflake

    DATABASE : TICKETS_DB

    WAREHOUSE : TKT_DW

    SCHEMA : TKT_SCHEMA


To load S3 data into tables into Snowflake, an external stage has to be set based on a storage integration. This stage refernces the external location 
(S3 Bucket) of the data files to be loaded. Therefore, we go ahead and the setup the following


    STORAGE INTEGRATION : s3_storage_integration

    FILE FORMAT : csv_pipe_format 

    STAGE : s3_stage 
    
All these sql statements can be found inside the worksheet foler, in `ticketsDB_worksheet.sql`


# ETL Batch Processing
The ETL Pipeline was designed to schedlle and load multipe csv files in an S3 Bucket directory to tables in Snowflake Database.
With the required tables created in Snowflake DB, the ETL pipeline reads csv data from the tickets_data files in S3 Bucket,
from there programmatically processes it and loads them into 5 analytical tables in Snowflake using Python and SQL.
The Snowflake tables where the data is loaded to are: `users`, `venue`, `category`, `date`, `event`,and `listing`.


# Conclusion
This was a fun project to demonstrate how to pull and load external data on S3 into Snowflake, a modern data warehouse.
The ability to use open source technology such as Airflow and Docker to build a data pipeline is simply amazing.

