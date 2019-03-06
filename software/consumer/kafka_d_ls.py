#!/usr/bin/env python

import io

import avro.schema
import avro.io

from kafka import KafkaConsumer

topic = 'debug'

if __name__ == "__main__":
    # avro schema path
    schema_path = '../schema/d_ls.avsc'

    # load avro schema
    schema = avro.schema.parse(open(schema_path).read())

    consumer = KafkaConsumer(topic)

    for message in consumer:
        # disregard any message that does not have heartbeat key
        key_splited = message.key.split(':')
        if key_splited[0] != 'dls':
            continue

        isoblue_id = key_splited[1]

        # setup avro decoder
        bytes_reader = io.BytesIO(message.value)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(schema)
        ls_datum = reader.read(decoder)

        timestamp = ls_datum['timestamp']
        gps_log_size = ls_datum['gpslogsize']
        tra_log_size = ls_datum['tralogsize']
        imp_log_size = ls_datum['implogsize']

        print timestamp, gps_log_size, tra_log_size, imp_log_size
