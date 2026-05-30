# uno

A lightweight Python toolkit for interacting with Ethereum-compatible chains.

## Features
- **Client**: Connect to any EVM node, get balances, nonces, block data
- **ERC20Token**: Inspect token metadata and balances
- **TxSender**: Sign and broadcast ETH transfers and contract calls
- **GasHelper**: EIP-1559 fee suggestions and gas estimation
- **CLI**: `uno balance <addr>` and `uno block [number]`

## Install
```bash
pip install -e .
```

## Quick start
```python
from uno import connect
from uno.erc20 import ERC20Token
from uno.gas import GasHelper

w3_client = connect("https://mainnet.base.org")
print(f"Block: {w3_client.block_number}")
print(f"Balance: {w3_client.get_balance('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045')} ETH")

gas = GasHelper(w3_client.w3)
fees = gas.suggest_fees()
print(f"Base fee: {fees['base_fee_gwei']:.2f} gwei")
```

## CLI
```bash
uno --rpc https://mainnet.base.org balance 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
uno block
uno block 12345678
```

## Requirements
- Python >= 3.10
- web3 >= 6.15.0
