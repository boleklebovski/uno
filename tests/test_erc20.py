"""Unit tests for ERC20Token."""
import pytest
from unittest.mock import MagicMock, patch
from uno.erc20 import ERC20Token


def make_mock_w3(name="TestToken", symbol="TST", decimals=18, supply=10**24):
    contract_mock = MagicMock()
    contract_mock.functions.name.return_value.call.return_value = name
    contract_mock.functions.symbol.return_value.call.return_value = symbol
    contract_mock.functions.decimals.return_value.call.return_value = decimals
    contract_mock.functions.totalSupply.return_value.call.return_value = supply
    contract_mock.functions.balanceOf.return_value.call.return_value = 5 * 10**18

    w3_mock = MagicMock()
    w3_mock.eth.contract.return_value = contract_mock
    return w3_mock


def test_symbol():
    w3 = make_mock_w3(symbol="UNO")
    token = ERC20Token(w3, "0x" + "a" * 40)
    assert token.symbol == "UNO"


def test_human_balance():
    w3 = make_mock_w3(decimals=18)
    token = ERC20Token(w3, "0x" + "b" * 40)
    assert token.human_balance("0x" + "c" * 40) == 5.0
