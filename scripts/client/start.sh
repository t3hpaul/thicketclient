#!/bin/bash

sudo python /etc/thicketclient/client_main_polling.py <&- 1>/dev/null 2>&1 &
pid=$!
echo ${pid} > /var/run/thicketclient.pid
echo "the pid is" $pid
