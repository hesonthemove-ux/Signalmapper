#!/bin/bash
echo "📡 Fetching Ofcom Technical Parameters..."
curl -L "https://www.ofcom.org.uk/__data/assets/file/0025/91816/txparams.csv" -o ~/Signalmapper_Project/data/ofcom_tx.csv
echo "✅ Ofcom data saved to ~/Signalmapper_Project/data/"
