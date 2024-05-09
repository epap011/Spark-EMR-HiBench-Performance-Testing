cd ~/HiBench

./bin/workloads/ml/rf/prepare/prepare.sh
./bin/workloads/micro/sort/prepare/prepare.sh
./bin/workloads/sql/join/prepare/prepare.sh

./bin/workloads/ml/rf/spark/run.sh
./bin/workloads/micro/sort/spark/run.sh
./bin/workloads/sql/join/spark/run.sh

cat /home/hadoop/HiBench/report/hibench.report