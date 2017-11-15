#!/bin/sh

path="/usr/local/mysql/bin/"
argc=$#
ope=$1
retval=0

usage() {
    echo "Usage: $0 {start|stop|restart}"
}

judge_mysql_run() {
    [ "`netstat -tunlp|grep mysqld|wc -l`" -ne 0 ] && {
        echo "mysqld already running..."
        exit 3
    }
}

judge_mysql_run_for_stop() {
    [ ! -S /tmp/mysql3376.sock ] && {
        echo "mysqld 3376 not running..."
        retval=1
    } || {
        retval=0
    }
}

start() {
    judge_mysql_run
    echo "start..."
    echo "${path}mysqld &"
}

stop() {
    judge_mysql_run_for_stop
    [ $retval -eq 0 ] && {
        echo "stop..."
        ${path}mysqladmin -S /tmp/mysql3376.sock shutdown
    }
}

restart() {
    echo "restart..."
    stop
    sleep 2
    start
}

choose() {
    case "$ope" in
        start)
            start
            ;;
        stop)
            stop
            ;;
        restart)
            restart
            ;;
        *)
            usage
            exit 2
    esac
}

main() {
    [ $argc -lt 1 ] && {
        usage
        exit 1
    }
    choose
}

main
