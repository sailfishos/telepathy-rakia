#!/bin/sh

export PYTHONPATH=/opt/tests/telepathy-rakia/bin/

sh /opt/tests/telepathy-rakia/bin/tools/with-session-bus.sh \
  --config-file=/opt/tests/telepathy-rakia/bin/tools/tmp-session-bus.conf -- "$@"

e=$?
    case "$e" in
        (0)
            echo "PASS"
            ;;
        (*)
            echo "FAIL: ($e)"
            ;;
    esac

exit $e

