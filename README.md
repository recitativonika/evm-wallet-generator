# Mass-generates EVM compatible wallet

mass-generates EVM compatible mnemonic phrases and their corresponding public keys, while automatically saving the private keys to a text file.

## • Installation & how to run?

```bash
git clone https://github.com/recitativonika/evm-wallet-generator.git
cd evm-wallet-generator
pip install -r requirements.txt
python generate.py
```

# Example Usage

When you run the script, it will prompt you to enter the number of mnemonic phrases to generate:
```bash
Enter the number of Ethereum mnemonic phrases to generate: 5
```
The script will generate the specified number of mnemonic phrases, along with their corresponding private keys and public keys, saving them to a file named evm_keys.txt. The output in the text file will look like this:
```bash
Mnemonic Phrase: apple banana cherry date elder flower grape hat igloo jack kite lemon, Private Key: 0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef, Public Key: 0xB3bC7D8F9C0BaA9B199C3D0D1B5FfA2A144E12D4
Mnemonic Phrase: dog elephant frog giraffe horse iguana jaguar kangaroo lion monkey, Private Key: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890, Public Key: 0xA4A5B6C7D8E9F0A1B2C3D4E5F6A7B8C9D0E1F2A
...
```
# Important Notes:

File Handling: The script saves the mnemonic phrases, private keys, and public keys to evm_keys.txt. You can change the filename in the script if desired.
Security: Ensure proper handling of private keys and mnemonic phrases. Never expose or share them in public or unsecured environments.
Key Management: Consider implementing secure storage mechanisms and key management solutions for real applications.

This script efficiently generates Ethereum mnemonic phrases, private keys, and public keys while automatically saving the private keys to a text file. Enjoy generating your keys!
