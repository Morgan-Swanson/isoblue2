cp -r $1 ./data/kafka-logs
rm ./data/kafka-logs/*.csv
rm -r ./data/kafka-logs/data
rm ./data/kafka-logs/cleaner-offset-checkpoint
rm ./data/kafka-logs/recovery-point-offset-checkpoint
rm ./data/kafka-logs/meta.properties
rm ./data/kafka-logs/test.log
rm ./data/kafka-logs/replication-offset-checkpoint
