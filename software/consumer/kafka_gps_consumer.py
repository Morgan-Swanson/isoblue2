#!/usr/bin/env python

import io
import sys
import re
import struct
import argparse
import os
import json
import datetime

import avro.schema
import avro.io

from struct import *
from kafka import KafkaConsumer

topic = 'remote'

if __name__ == "__main__":

    # avro schema path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    schema_path = f"{str(dir_path)}/../schema/gps.avsc"

    # load avro schema
    schema = avro.schema.parse(open(schema_path).read())

    consumer = KafkaConsumer(topic, bootstrap_servers=["localhost:9092"], group_id=None, \
                             auto_offset_reset="earliest")

    for message in consumer: 
        key_splited = message.key.decode("utf-8").split(':')
        if key_splited[0] != 'gps':
            continue

        isoblue_id = key_splited[1]

        # setup avro decoder
        bytes_reader = io.BytesIO(message.value)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(schema)
        gps_datum = reader.read(decoder)
        time = gps_datum['object'].get('time')
        lat = gps_datum['object'].get('lat')
        lon = gps_datum['object'].get('lon')
        alt = gps_datum['object'].get('alt')
        if time and lat and lon and alt:
            dt = datetime.datetime.fromtimestamp(time)
            formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')
            payload = { "timestamp": formatted_time,
                        "gps": {"altitude": alt,
                                "latitude": lat,
                                "longitude": lon,
                                "nmea": [],
                                "utc": "" }
                       }
            print(json.dumps(payload))
