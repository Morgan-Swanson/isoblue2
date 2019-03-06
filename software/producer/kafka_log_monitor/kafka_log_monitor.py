#!/usr/bin/env python

import io
import os
import sys
import time

import avro
import avro.schema
import avro.io

from kafka import KafkaProducer

from time import sleep

schema_path = '/opt/schema/d_ls.avsc'
isoblue_id_path = '/opt/id'

topic = 'debug'
gps_log_dir = '/media/sda1/kafka-logs/gps-0/'
tra_log_dir = '/media/sda1/kafka-logs/tra-0/'
imp_log_dir = '/media/sda1/kafka-logs/imp-0/'

def get_size(start_path=None):

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

if __name__ == "__main__":

    # create kafka producer
    producer = KafkaProducer(bootstrap_servers='localhost')

    # load avro schema and setup encoder
    try:
        f_s = open(schema_path)
        schema = avro.schema.parse(f_s.read())
        f_s.close()
    except IOError:
        print('cannot open schema file')
        sys.exit()

    try:
        f_id = open(isoblue_id_path)
        isoblue_id = f_id.read().strip('\n')
        f_id.close()
    except IOError:
        print('cannot open isoblue_id file')
        sys.exit()

    timestamp = None

    while True:
        if os.path.isdir(gps_log_dir):
            gps_log_size = get_size(gps_log_dir)
        else:
            gps_log_size = 0

        if os.path.isdir(tra_log_dir):
            tra_log_size = get_size(tra_log_dir)
        else:
            tra_log_size = 0

        if os.path.isdir(imp_log_dir):
            imp_log_size = get_size(imp_log_dir)
        else:
            imp_log_size = 0

        # create the datum
        datum = {}
        datum['timestamp'] = int(time.time())
        datum['gpslogsize'] = gps_log_size
        datum['tralogsize'] = tra_log_size
        datum['implogsize'] = imp_log_size

#        print int(time.time()), gps_log_size, tra_log_size, imp_log_size

        dls_datum = avro.io.DatumWriter(schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)

        # write to the datum
        dls_datum.write(datum, encoder)
        # produce the message to Kafka
        dls_buf = bytes_writer.getvalue()
        producer.send(topic, key='dls:' + isoblue_id, value=dls_buf)

        datum = {}
        dls_datum = None

        sleep(60)

