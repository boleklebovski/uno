"""ERC-20 token helpers for uno."""
from web3 import Web3
from web3.contract import Contract

ERC20_ABI = [
    {"inputs":[],"name":"name","outputs":[{"type":"string"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"symbol","outputs":[{"type":"string"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"decimals","outputs":[{"type":"uint8"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"totalSupply","outputs":[{"type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"type":"uint256"}],"stateMutability":"view","type":"function"},
]


class ERC20Token:
    """Read-only interface for an ERC-20 token."""

    def __init__(self, w3: Web3, address: str):
        self.w3 = w3
        self.address = Web3.to_checksum_address(address)
        self.contract: Contract = w3.eth.contract(address=self.address, abi=ERC20_ABI)

    @property
    def name(self) -> str:
        return self.contract.functions.name().call()

    @property
    def symbol(self) -> str:
        return self.contract.functions.symbol().call()

    @property
    def decimals(self) -> int:
        return self.contract.functions.decimals().call()

    @property
    def total_supply(self) -> int:
        return self.contract.functions.totalSupply().call()

    def balance_of(self, holder: str) -> int:
        """Return the raw token balance for holder (in smallest unit)."""
        return self.contract.functions.balanceOf(
            Web3.to_checksum_address(holder)
        ).call()

    def human_balance(self, holder: str) -> float:
        """Return the token balance scaled by decimals."""
        raw = self.balance_of(holder)
        return raw / (10 ** self.decimals)
