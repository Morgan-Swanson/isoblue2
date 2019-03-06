#!/bin/sh

curl -o /opt/tmp_pgns http://cloudradio39.ecn.purdue.edu/pgns -m 30 > /dev/null 2>&1

if [ $? != 0 ]; then
	echo 'curl failed, check network status!'
	PROCESS_NUM=$(ps -ef | grep "dhclient" | grep -v "grep" | wc -l)
	if [ $PROCESS_NUM -eq 0 ]; then
		echo 'network is down, and no dhclient running ... will try restarting the cell network'
		qmicli -p -d /dev/cdc-wdm0 --wds-start-network=Broadband --client-no-release-cid
		dhclient wwan0
    sleep 30
	fi
	exit 1
fi

diff /opt/pgns /opt/tmp_pgns > /dev/null 2>&1

if [ $? -eq 0 ]; then
	echo 'no changes in PGN list'
	rm -f /opt/tmp_pgns
else
	mv /opt/tmp_pgns /opt/pgns
	echo 'new changes in PGN list'
	for pid in `ps aux | grep --regexp="[k]afka_can_log.*\-f" | awk '{print $2}'`; do
		kill -s USR1 $pid
	done
fi
