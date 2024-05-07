#!/bin/bash

#Download Prerequisites
sudo yum install git maven
git clone https://github.com/Intel-bigdata/HiBench

cd HiBench

mvn -Dspark=3.1 -Dscala=2.12 clean package

#Configure Hadoop
cp conf/hadoop.conf.template conf/hadoop.conf
hadoop_home="/usr/lib/hadoop"
hdfs_master=$(hdfs getconf -confKey fs.defaultFS | grep -o 'hdfs://[^"]*')
sed -i "/^hibench.hadoop.home /s|hibench.hadoop.home.*|hibench.hadoop.home $hadoop_home|" conf/hadoop.conf
sed -i "s|hibench.hdfs.master.*|hibench.hdfs.master $hdfs_master|" conf/hadoop.conf
echo "hibench.hadoop.examples.jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar" >> conf/hadoop.conf
echo "hibench.hadoop.examples.test.jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-client-jobclient.jar" >> conf/hadoop.conf

#Configure Spark
cp conf/spark.conf.template conf/spark.conf
spark_home="/usr/lib/spark"
sed -i "/^hibench.spark.home /s|hibench.spark.home.*|hibench.spark.home $spark_home|" conf/spark.conf
sed -i "s|hibench.spark.master.*|hibench.spark.master yarn|" conf/spark.conf
echo "Setup completed successfully."
