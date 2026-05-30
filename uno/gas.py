"""Gas price and estimation utilities."""
from web3 import Web3


class GasHelper:
    """Helpers for gas price queries and fee estimation."""

    def __init__(self, w3: Web3):
        self.w3 = w3

    def base_fee(self) -> int:
        """Return the base fee of the latest block in wei."""
        block = self.w3.eth.get_block("latest")
        return block.get("baseFeePerGas", 0)

    def suggest_tip(self) -> int:
        """Return the suggested max priority fee (tip) in wei."""
        return self.w3.eth.max_priority_fee

    def suggest_fees(self) -> dict:
        """Return suggested EIP-1559 fee parameters."""
        base = self.base_fee()
        tip = self.suggest_tip()
        return {
            "base_fee_wei": base,
            "max_priority_fee_wei": tip,
            "max_fee_wei": base * 2 + tip,
            "base_fee_gwei": base / 1e9,
            "max_priority_fee_gwei": tip / 1e9,
        }

    def estimate_gas(self, tx: dict) -> int:
        """Estimate gas for a transaction dict."""
        return self.w3.eth.estimate_gas(tx)
