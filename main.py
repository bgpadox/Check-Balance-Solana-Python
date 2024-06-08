from solana.rpc.api import Client
from solders.pubkey import Pubkey

solana_client = Client("https://api.mainnet-beta.solana.com")

address = "ENTER YOUR ADDRESS"

pubkey = Pubkey.from_string(address)

balance_result = solana_client.get_balance(pubkey)

balance_in_sol = balance_result.value / 1_000_000_000

print(f"Balance: {balance_in_sol} SOL")