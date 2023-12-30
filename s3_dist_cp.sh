#! /bin/bash
"s3-dist-cp --s3Endpoint=s3.ap-south-1.amazonaws.com --src=hdfs:///user/hadoop/ --dest=s3://emr-hdfs-bkp/ecom_data_fact/ --dest=hdfs:///user/hadoop/"
s3-dist-cp --s3Endpoint=s3.ap-south-1.amazonaws.com --src=hdfs:///user/hadoop/ --dest=s3://emr-hdfs-bkp/