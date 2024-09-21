import secrets
from mnemonic import Mnemonic
from eth_account import Account

def generate_mnemonic():
    # Generate a 12-word mnemonic phrase
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=128)  # 128 bits for a 12-word phrase
    return mnemonic_phrase

def mnemonic_to_keypair(mnemonic_phrase):
    # Generate the private key from the mnemonic phrase
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic_phrase)
    private_key = account.key.hex()
    public_key = account.address  # Get the corresponding public key/address
    return private_key, public_key

def mass_generate_mnemonics(num_mnemonics):
    mnemonic_keypairs = []
    
    for _ in range(num_mnemonics):
        mnemonic_phrase = generate_mnemonic()
        private_key, public_key = mnemonic_to_keypair(mnemonic_phrase)
        mnemonic_keypairs.append((mnemonic_phrase, private_key, public_key))
    
    return mnemonic_keypairs

def save_keys_to_file(mnemonic_keypairs, filename):
    with open(filename, 'w') as f:
        for mnemonic_phrase, private_key, public_key in mnemonic_keypairs:
            f.write(f" Mnemonic Phrase: {mnemonic_phrase}\n Private Key: {private_key}\n Public Key/address: {public_key}\n {"-" * 62}\n")

def main():
    # Input the number of mnemonics to generate
    num_mnemonics = int(input("Enter the number of EVM compatible mnemonic phrases to generate: "))
    
    # Generate mnemonics, private keys, and public keys
    mnemonic_keypairs = mass_generate_mnemonics(num_mnemonics)
    
    # Specify the output file name
    filename = "evm_keys.txt"
    
    # Save keys to a file
    save_keys_to_file(mnemonic_keypairs, filename)
    
    print(f"{num_mnemonics} EVM compatible mnemonic phrases have been generated and saved to '{filename}'.")

if __name__ == "__main__":
    main()
