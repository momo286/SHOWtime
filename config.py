from tabs.bitcoin import BitcoinPrice, Bitcoind
from tabs.sysinfo import SystemStats, DiskUsage

import os

# Add any tabs you want to be visible here
tabs = [ # Track a running Bitcoin node
         #Bitcoind({"host": "http://127.0.0.1:8332",
         #          "username": "bitcoinrpc",
         #          # Read the password from a file
         #          "password": "passwordhere" }),
        
         # A Bitcoin price ticker
         BitcoinPrice(),
         
         # Displays CPU, RAM usage and uptime
         SystemStats(),
         
         # Displays disk usage
         DiskUsage() ]
