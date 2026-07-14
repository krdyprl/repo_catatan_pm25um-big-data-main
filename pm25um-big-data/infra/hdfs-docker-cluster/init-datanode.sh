#!/bin/bash

#!/bin/bash
set -e

# ensure datanode data dir exists
mkdir -p /opt/hadoop/data/dataNode
chown -R root:root /opt/hadoop/data || true

# wait until NameNode HTTP UI is reachable (basic check)
echo "Waiting for NameNode to be reachable..."
until curl -sSf http://namenode:9870/ >/dev/null 2>&1; do
  echo "NameNode not ready yet, sleeping 2s..."
  sleep 2
done
echo "NameNode reachable."

# Start DataNode
echo "Starting DataNode..."
hdfs datanode

# tail logs to keep container running
# tail -F /opt/hadoop/logs/* || true


# rm -rf /opt/hadoop/data/dataNode/*
# chown -R hadoop:hadoop /opt/hadoop/data/dataNode
# chmod 755 /opt/hadoop/data/dataNode
# hdfs datanode