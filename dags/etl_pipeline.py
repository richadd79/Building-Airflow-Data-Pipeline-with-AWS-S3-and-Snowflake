from airflow import DAG
from datetime import datetime, timedelta
from create_table_sql import *
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator


default_args = {
    'owner':'etl_data_pipelines',
    'retries':1,
    'retry_delay':timedelta(minutes=5)
}



# LOAD CSV DATA INTO TABLES
with DAG(
    default_args=default_args,
    dag_id='load_s3_data_to_snowflake_dwh',
    description='s3_snowflake_data_pipeline',
    start_date=datetime(2023, 3, 10),
    schedule_interval='@daily',
    catchup=False
) as dag:
    create_users_table = SnowflakeOperator(
        task_id='create_users_table',
        sql=users_create_table,
        snowflake_conn_id='snowflake_default'
    )
    create_date_table = SnowflakeOperator(
        task_id='create_date_table',
        sql=date_create_table,
        snowflake_conn_id='snowflake_default'
    )
    create_event_table = SnowflakeOperator(
        task_id='create_event_table',
        sql=event_create_table,
        snowflake_conn_id='snowflake_default'
    )
    create_listing_table = SnowflakeOperator(
        task_id='create_listing_table',
        sql=listing_create_table,
        snowflake_conn_id='snowflake_default'
    )
    create_category_table = SnowflakeOperator(
        task_id='create_category_table',
        sql=category_create_table,
        snowflake_conn_id='snowflake_default'
    )
    create_venue_table = SnowflakeOperator(
        task_id='create_venue_table',
        sql=venue_create_table,
        snowflake_conn_id='snowflake_default'
    )
    copy_into_users_table = S3ToSnowflakeOperator(
        task_id="copy_into_users_table",
        snowflake_conn_id='snowflake_default',
        s3_keys=['allusers_pipe.csv'],
        table='users',
        stage='users_stage',
        file_format="(type = 'CSV',field_delimiter = '|')"
    )
    copy_into_date_table = S3ToSnowflakeOperator(
        task_id="copy_into_date_table",
        snowflake_conn_id='snowflake_default',
        s3_keys=['date2008_pipe.csv'],
        table='date',
        stage='s3_stage',
        file_format="(type = 'CSV',field_delimiter = '|')"
    )
    copy_into_event_table = S3ToSnowflakeOperator(
        task_id="copy_into_event_table",
        snowflake_conn_id='snowflake_default',
        s3_keys=['allevents_pipe.csv'],
        table='event',
        stage='s3_stage',
        file_format="(type = 'CSV',field_delimiter = '|')"
    )
    copy_into_listing_table = S3ToSnowflakeOperator(
        task_id="copy_into_listing_table",
        snowflake_conn_id='snowflake_default',
        s3_keys=['listings_pipe.csv'],
        table='listing',
        stage='s3_stage',
        file_format="(type = 'CSV',field_delimiter = '|')"
    )
    copy_into_category_table = S3ToSnowflakeOperator(
        task_id="copy_into_category_table",
        snowflake_conn_id='snowflake_default',
        s3_keys=['category_pipe.csv'],
        table='category',
        stage='s3_stage',
        file_format="(type = 'CSV',field_delimiter = '|')"
    )
    copy_into_venue_table = S3ToSnowflakeOperator(
        task_id="copy_into_venue_table",
        snowflake_conn_id='snowflake_default',
        s3_keys=['venue_pipe.csv'],
        table='venue',
        stage='s3_stage',
        file_format="(type = 'CSV',field_delimiter = '|')"
    )

create_users_table >> create_date_table >> create_event_table >> create_listing_table >> create_category_table >> create_venue_table >> copy_into_users_table >>  copy_into_date_table >> copy_into_event_table >> copy_into_listing_table >> copy_into_category_table >> copy_into_venue_table



