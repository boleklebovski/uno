"""Main client module for uno."""
from web3 import Web3
from typing import Optional

class Client:
    """Wraps a Web3 instance with convenient helpers."""

    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.w3.is_connected():
            raise ConnectionError(f"Cannot connect to {rpc_url}")

    def get_balance(self, address: str, unit: str = "ether") -> float:
        """Return the ETH balance of address in the given unit."""
        checksum = Web3.to_checksum_address(address)
        wei = self.w3.eth.get_balance(checksum)
        return float(self.w3.from_wei(wei, unit))

    def get_nonce(self, address: str) -> int:
        """Return the transaction count (nonce) for address."""
        return self.w3.eth.get_transaction_count(
            Web3.to_checksum_address(address)
        )

    def get_block(self, identifier="latest") -> dict:
        """Return block data for the given number or tag."""
        return dict(self.w3.eth.get_block(identifier))

    @property
    def chain_id(self) -> int:
        return self.w3.eth.chain_id

    @property
    def block_number(self) -> int:
        return self.w3.eth.block_number


def connect(rpc_url: str) -> Client:
    """Create and return a connected Client."""
    return Client(rpc_url)
