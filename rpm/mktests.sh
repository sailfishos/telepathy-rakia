#!/bin/sh

cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<testdefinition version="1.0">
    <suite name="telepathy-rakia-tests">
        <description>Telepathy Rakia tests</description>
        <set name="telepathy-rakia-twisted-tests">
EOF

for testcase in $(cat tests/twisted/rakia-twisted-tests.list)
do
    testcase_name=$(echo $testcase|sed 's/\//_/')
    attributes="name=\"$testcase_name\""
    #insignificant=`grep "^$testcase" tests/INSIGNIFICANT || true`
    #if test -n "$insignificant"
    #then
    #    continue
    #    attributes="$attributes insignificant=\"true\""
    #fi
    cat <<EOF
        <case $attributes>
            <step>/opt/tests/telepathy-rakia/bin/runTest.sh python /opt/tests/telepathy-rakia/bin/$testcase</step>
        </case>
EOF
done

cat <<EOF
        </set>
    </suite>
</testdefinition>
EOF
