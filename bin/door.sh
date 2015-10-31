#!/bin/bash
#
# open/close door manually from the console
#
# written by Alexander List <alexander.list@dimsumlabs.com>
# Copyright (c) 2013
# License: Public Domain

function doorstatus {
    ds=$(cat /sys/class/gpio/gpio17/value)
    dshuman=""
    case "$ds" in
        "0")
            dshuman="closed"
            ;;
        "1")
            dshuman="open"
            ;;
        *)
            dshuman="unknown"
            ;;
    esac
    echo "Door status: $dshuman ($ds)"
}

function opendoor {
    echo 1 > /sys/class/gpio/gpio17/value
}

function closedoor {
    echo 0 > /sys/class/gpio/gpio17/value
}

function usage {
    echo "Usage: $0 {open|close|status|openclose}"
    echo ""
}

case $1 in
    "openclose")
        doorstatus
        opendoor
        doorstatus
        sleep 5
        closedoor
        doorstatus
        ;;
    "open")
        doorstatus
        opendoor
        doorstatus
        ;;
    "close")
        doorstatus
        closedoor
        doorstatus
        ;;
    "status")
        doorstatus
        ;;
    *)
        usage
        doorstatus
        ;;
esac

