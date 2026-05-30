"""Simple CLI for uno."""
import argparse
import sys
from uno.client import connect


def cmd_balance(args):
    client = connect(args.rpc)
    bal = client.get_balance(args.address)
    print(f"{args.address}: {bal:.6f} ETH")


def cmd_block(args):
    client = connect(args.rpc)
    block = client.get_block(args.number or "latest")
    print(f"Block #{block['number']}  hash={block['hash'].hex()}  txs={len(block['transactions'])}")


def main():
    parser = argparse.ArgumentParser(prog="uno", description="Ethereum toolkit CLI")
    parser.add_argument("--rpc", default="https://mainnet.base.org", help="RPC endpoint")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_bal = sub.add_parser("balance", help="Get ETH balance")
    p_bal.add_argument("address")
    p_bal.set_defaults(func=cmd_balance)

    p_block = sub.add_parser("block", help="Show block info")
    p_block.add_argument("number", nargs="?", type=int)
    p_block.set_defaults(func=cmd_block)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
