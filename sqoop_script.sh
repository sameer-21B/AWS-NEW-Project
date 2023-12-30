#!/bin/bash
sqoop
sqoop import --connect jdbc:mysql://ecom-database-1.cxcfo1u6yrzl.ap-south-1.rds.amazonaws.com:3306/ecom_data_1 --table fact_ecom_data --username ingest_user --password FnuZIU1xlFgFov8oakB0 --split-by idx --m 5
hadoop fs -mv /user/hadoop/fact_ecom_data '/user/hadoop/fact_ecom_data_'$1
