#!/bin/bash
# Ingest Ofcom Technical Parameters
DATA_DIR="$HOME/Signalmapper_Project/data"
mkdir -p $DATA_DIR
echo "📡 Downloading Ofcom TxParams..."
curl -L "https://www.ofcom.org.uk/__data/assets/file/0025/91816/txparams.csv" -o /tmp/txparams.csv
# Filter for DAB/SSDAB only (approx > 174MHz)
grep -E "DAB|SSDAB" /tmp/txparams.csv > $DATA_DIR/ofcom_dab.csv
echo "✅ Data stored in $DATA_DIR/ofcom_dab.csv"
