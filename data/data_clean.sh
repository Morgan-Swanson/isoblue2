rm -r ./kafka-logs
cp -r $1 ./kafka-logs
cd kafka-logs
rm *.csv
rm -r data

