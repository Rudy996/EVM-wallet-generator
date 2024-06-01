from eth_account import Account
from mnemonic import Mnemonic

def generate_wallets(num_wallets):
    wallets = []
    mnemo = Mnemonic("english")
    Account.enable_unaudited_hdwallet_features()

    for _ in range(num_wallets):
        mnemonic = mnemo.generate(strength=128)
        private_key = Account.from_mnemonic(mnemonic).key.hex()
        account = Account.from_key(private_key)
        wallets.append({
            'address': account.address,
            'private_key': private_key,
            'mnemonic': mnemonic
        })

    return wallets

def save_wallets_to_file(wallets, filename):
    with open(filename, 'w') as file:
        for wallet in wallets:
            file.write(f"{wallet['address']} {wallet['private_key']} {wallet['mnemonic']}\n")

def main():
    num_wallets = int(input("Enter the number of wallets to generate: "))
    wallets = generate_wallets(num_wallets)
    save_wallets_to_file(wallets, 'wallets.txt')
    print(f"{num_wallets} wallets generated and saved to wallets.txt")

if __name__ == "__main__":
    main()
