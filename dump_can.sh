# Copy Input Kafka Database and clean for reading
mkdir -p ./data
cp -r $1 ./data/kafka-logs
rm ./data/kafka-logs/*.csv
rm -r ./data/kafka-logs/data
rm ./data/kafka-logs/cleaner-offset-checkpoint
rm ./data/kafka-logs/recovery-point-offset-checkpoint
rm ./data/kafka-logs/meta.properties
rm ./data/kafka-logs/test.log
rm ./data/kafka-logs/replication-offset-checkpoint
# Launch Kafka environment and configure, wait until up
docker-compose up --build --wait
sleep 5
# Dump data from the kafka log in nova / candump format
python3 ./software/consumer/kafka_can_consumer.py -t tra -a earliest


