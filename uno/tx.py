"""Transaction building and sending utilities for uno."""
from typing import Optional
from web3 import Web3
from web3.types import TxReceipt


class TxSender:
    """Signs and broadcasts raw transactions."""

    def __init__(self, w3: Web3, private_key: str):
        self.w3 = w3
        self.account = w3.eth.account.from_key(private_key)

    @property
    def address(self) -> str:
        return self.account.address

    def send_eth(
        self,
        to: str,
        amount_wei: int,
        gas: int = 21000,
        gas_price: Optional[int] = None,
    ) -> TxReceipt:
        """Send a plain ETH transfer and wait for the receipt."""
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        tx = {
            "to": Web3.to_checksum_address(to),
            "value": amount_wei,
            "gas": gas,
            "gasPrice": gas_price or self.w3.eth.gas_price,
            "nonce": nonce,
            "chainId": self.w3.eth.chain_id,
        }
        signed = self.account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed.raw_transaction)
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def call(self, contract_fn, gas: int = 200_000) -> TxReceipt:
        """Build, sign, and broadcast a contract function call."""
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        tx = contract_fn.build_transaction({
            "from": self.account.address,
            "nonce": nonce,
            "gas": gas,
            "gasPrice": self.w3.eth.gas_price,
        })
        signed = self.account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed.raw_transaction)
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)
