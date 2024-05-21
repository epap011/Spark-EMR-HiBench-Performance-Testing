## Setup an EMR Cluster capable or running `sparkbench` benchmark workloads



### Express Setup and Creation using aws cli

Use the `aws-sample-cluster-configuration.sh` file in order to quickly create an EMR cluster. 

> **Note**: You may need to configure appropriate security groups, ssh keys and VPC's for the EMR cluster. In our case our course instructor had already pre-configured some of that staff. 

You can also follow the manual EMR cluster creation steps using the cluster creation interface.



### Manual  Cluster Creation

> **Note**: The Amazon EMR cluster creation interface may differ slightly. 

- Go to **EMR** Service

- Select **Create a cluster**

- Amazon EMR release: `emr-6.5.0` (for spark 3.1)

- Application bundle: `Spark 3.1.2`, `Hadoop 3.2.1`, `Livy 0.7.1`, `Hive 3.1.2`
- Cluster Configuration: 
  - You can use any configuration you seem fit ( one common configuration for our experiments was `1 primary, 3 core, 8 Task-1` )
  - Cluster scaling: `Select Set cluster size manually`, on provisining check the "Spot purchasing option"

- Networking: choose VPC -> `csd543-vpc-vpc`  

- Networking: choose subnet -> `csd543-vpc-subnet-public2-us-east-1b`

> **Note**: "Default", Amazon created VPC's should also work. We were limited to the resources that we could leverage on AWS so specific VPC configuration was needed.

- Security configuration and EC2 key pair: your key-pair

- IAM roles: Service role -> `EMR_DefaultRole`

- EC2 instance profile for Amazon EMR: Instance Profile -> `EMR_EC2_DefaultRole`

- Make sure to check "Manually terminate cluster" in the Cluster termination and node replacement section.

- Select Create cluster  



## Environment setup (Hibench)  

After waiting for the cluster to become available, SSH to the primary node of the cluster **as the `hadoop` user**.  

Copy the `setup_hibench.sh` script to the machine, change its permissions ( `chmod +x ./setup_hibench.sh`) and execute it (`./setup_hibench.sh`). 

The script installs git and maven to the node, clones the HiBench repo, builds the whole repo and changes the configuration files in order for the 3 `sparkbench`  workloads picked (`micro/sort`, `ml/rf`, `sql/join` ) to execute in the cluster. 

> **Note**: The script should work on Amazon Linux 2 OS types ( default for EMR version 6.5.0 )  



## Run the 3 workloads   

Copy the `run_workloads.sh` script to the machine, change its permissions ( `chmod +x ./run_workloads.sh`) and execute it (`./run_workloads.sh`). 

The script sequentially prepares all input data on the cluster's HDFS and sequentially runs all workloads. In the end it prints the `hibench.report` file located on `~/report/HiBench`.

## Change dataset size

On `conf/hibench.conf` change hibench.scale.profile`. In our experiments we used the `gigantic` dataset size.



## Check HDFS status

Execute `hdfs dfsadmin -report` on the primary node.