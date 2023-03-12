CREATE OR REPLACE DATABASE TICKETS_DB;

CREATE WAREHOUSE TKT_DW;
CREATE SCHEMA TKT_SCHEMA;

----
DROP STORAGE INTEGRATION s3_storage_integration;

-- create the storage integration for s3
CREATE STORAGE INTEGRATION s3_storage_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::your-own-account-id:role/your-snowflake-role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://bucket-name/staging/');

----
DESC INTEGRATION s3_storage_integration;

--- Create file format
CREATE OR REPLACE FILE FORMAT csv_pipe_format type = 'csv' field_delimiter = '|';

--- Create stage for all s3 csv
CREATE OR REPLACE STAGE s3_stage
storage_integration = s3_storage_integration
url = 's3://bucket-name/staging/'
file_format = csv_pipe_format;

-----
show tables;

---
show stages;

---
list @s3_stage;

----
select * from users limit 5;
select * from date limit 5;
select * from event limit 5;
select * from listing limit 5;
select * from venue limit 5;
select * from category limit 5;