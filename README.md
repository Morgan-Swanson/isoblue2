## Introduction
I forked this project in order to be able to read data from the public data [here](https://docs.google.com/spreadsheets/d/1tEt4c_brbIT2TtRqiGPmVYWvcfRPNQaU2D7gzUJLTaU/edit#gid=0).
The guide published [here](https://isoblue.org/docs/data/read) is outdated and the links do not work.
I built some docker and bash scripts to extract the data, which is stored in an atypical format (kafka .log files).

## How to use

1. Install python-kafka and avro
2. Download some data from the link above
3. Run dump_can.sh path-to-data-dir

## To Do

1. Get the dump_can.sh script running in a docker container, added to docker compose
2. Pull the gps data in addition to can data in the proper nova format

