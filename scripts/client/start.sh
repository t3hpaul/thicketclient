#!/bin/bash

python /etc/thicketclient/client/client_main_event.py <&- 1>/dev/null 2>&1 &
pid=$!
echo ${pid} > /var/run/thicketclient.pid
echo "the pid is" $pid
