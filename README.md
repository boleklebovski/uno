# uno

A lightweight Python toolkit for interacting with Ethereum-compatible chains.

## Features
- Connect to any EVM node via RPC
- Fetch balances, nonces, and transaction receipts
- Sign and send raw transactions
- ERC-20 token utilities

## Install
```bash
pip install -r requirements.txt
```

## Quick start
```python
from uno import connect
w3 = connect("https://mainnet.base.org")
print(w3.eth.block_number)
```
