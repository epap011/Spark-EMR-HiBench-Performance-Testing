# Spark-EMR-HiBench-Performance-Testing

## Setup EMR Cluster 

1. Go to EMR Service
2. Select **Create a cluster**
3. Amazon EMR release: emr-6.5.0 (for spark 3.1)
4. Application bundle: Spark 3.1.2, Hadoop 3.2.1, Livy 0.7.1, Hive 3.1.2, JupyterEnterpriseGateway 2.1.0
5. Networking: choose VPC -> csd543-vpc-vpc  
6. Networking: choose subnet -> csd543-vpc-subnet-public2-us-east-1b
7. Security configuration and EC2 key pair: your key-pair
8. IAM roles: Service role -> EMR_DefaultRole
9. EC2 instance profile for Amazon EMR: Instance Profile -> EMR_EC2_DefaultRole
10. select Create cluster  

## Environment setup (Hibench)  
ssh to the primary node of the EMR cluster you just created.  

Install git and maven  
> sudo yum install git, maven  

Clone the Hibench repo  
> git clone https://github.com/Intel-bigdata/HiBench  


## Build Hibench
cd into the Hibench folder  
> cd Hibench  

> mvn -Dspark=3.1 -Dscala=2.2 clean package  

## Setup Spark-bench
> cd Hibench (you may already be there :P)  

> cp conf/hadoop.conf.template conf/hadoop.conf  

> vim conf/hadoop.conf  

hibench.hadoop.home -> /usr/lib/hadoop  
hibench.hdfs.master -> (output of: hdfs getconf -confKey fs.defaultFS)  

> cp conf/spark.conf.template conf/spark.conf  

> vim conf/spark.conf  

hibench.spark.home -> /usr/lib/spark  

## Run Spark-bench  
> cd Hibench

> bin/workloads/micro/wordcount/prepare/prepare.sh  

> bin/workloads/micro/wordcount/spark/run.sh