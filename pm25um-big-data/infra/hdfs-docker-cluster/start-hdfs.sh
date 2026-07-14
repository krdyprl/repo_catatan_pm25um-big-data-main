#!/bin/bash
set -e

# ensure dirs exist and correct permissions
mkdir -p /opt/hadoop/data/nameNode
mkdir -p /opt/hadoop/data/tmp
chown -R root:root /opt/hadoop/data || true

# Format NameNode only if not formatted
if [ ! -d "/opt/hadoop/data/nameNode/current" ]; then
  echo "Formatting NameNode..."
  hdfs namenode -format -force -nonInteractive
else
  echo "NameNode metadata found, skipping format."
fi

# Start NameNode in background
echo "Starting NameNode..."
hdfs namenode

# tail logs to keep container running and help debugging
# tail -F /opt/hadoop/logs/* || true


# if [ ! -d "/opt/hadoop/data/nameNode/current" ]; then
#     echo "Formatting NameNode..."
#     hdfs namenode -format -force -nonInteractive;
# fi
# hdfs namenode