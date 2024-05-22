aws emr create-cluster \
 --name "stzagkarak-runHiBench-12" \
 --log-uri "s3://aws-logs-533267009420-us-east-1/elasticmapreduce" \
 --release-label "emr-6.5.0" \
 --service-role "arn:aws:iam::533267009420:role/EMR_DefaultRole" \
 --ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","EmrManagedMasterSecurityGroup":"sg-04ed4d88427f49361","EmrManagedSlaveSecurityGroup":"sg-06e2356105589c9ec","KeyName":"hibench_key","AdditionalMasterSecurityGroups":[],"AdditionalSlaveSecurityGroups":[],"SubnetId":"subnet-04e177d971dac2e49"}' \
 --applications Name=Hadoop Name=Hive Name=Livy Name=Spark \
 --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","Name":"Primary","InstanceType":"m5.xlarge","EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"VolumeType":"gp2","SizeInGB":32},"VolumesPerInstance":2}]}},{"BidPrice":"0.083","InstanceCount":8,"InstanceGroupType":"TASK","Name":"Task - 1","InstanceType":"m5.xlarge","EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"VolumeType":"gp2","SizeInGB":32},"VolumesPerInstance":2}],"EbsOptimized":true}},{"BidPrice":"0.083","InstanceCount":3,"InstanceGroupType":"CORE","Name":"Core","InstanceType":"m5.xlarge","EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"VolumeType":"gp2","SizeInGB":64},"VolumesPerInstance":2}]}}]' \
 --scale-down-behavior "TERMINATE_AT_TASK_COMPLETION" \
 --region "us-east-1"
