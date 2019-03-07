#!/bin/sh

qmicli -p -d /dev/cdc-wdm0 --wds-start-network=Broadband --client-no-release-cid
dhclient wwan0
