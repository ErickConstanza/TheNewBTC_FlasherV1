# TheNewBTC_FlasherV1
This script is intended for use on the Bitcoin mainnet, and assumes the user has a valid private key and sufficient funds for the transaction.
# Bitcoin Transaction Script

This script allows you to send Bitcoin transactions using the `bitcoinlib` library. It supports creating or loading a wallet, importing a private key, and sending Bitcoin to a specified recipient address.

## Features

- **Wallet Management:** Create or load a wallet, and import a private key.
- **Service Initialization:** Interact with the Bitcoin blockchain.
- **Balance and Transaction Management:** Update wallet data, retrieve balance, and view transaction history.
- **Send Transactions:** Send Bitcoin to a specified address.

## Requirements

- Python 3.7 or later
- `bitcoinlib` library
- `requests` library (for interacting with Bitcoin services)

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `requirements.txt` file:**

    ```txt
    bitcoinlib
    requests
    ```

## Usage

1. **Run the script:**
    ```sh
    python main.py
    ```

2. **Follow the prompts:**
   - **Enter the sender's private key:** Input the private key for the wallet from which funds will be sent.
   - **Enter the recipient address:** Input the Bitcoin address where you want to send the funds.
   - **Enter the amount of BTC to send:** Specify the amount of Bitcoin you want to transfer.

## Script Details

- **Logging:** Logs are generated to track the process and errors. By default, they are saved to a file named `debug_<timestamp>.log` in the current directory.
- **Fees:** The transaction fee is set to 4 satoshis per byte by default. Adjust the `FEE` variable in the script if needed.

## Example

To send Bitcoin, follow these steps:

1. **Start the script:**
    ```sh
    python main.py
    ```

2. **Input your details when prompted:**
    ```
    Enter the sender's private key: L1dqg82TnSTF16eJ6Fa5Pkxz6Sg29oRJWGonUshGYUywA4zo17eH
    Enter the recipient address: bc1q85lulzvgtmtexrm9072d02d85aa2k0c43age5u
    Enter the amount of BTC you want to send: 0.0001
    ```

3. **The script will process the transaction and provide a confirmation or error message.**

## Notes

- **Network Compatibility:** This script is configured for the Bitcoin mainnet. Ensure you have sufficient funds and the correct network settings for your transactions.
- **Private Key Security:** Keep your private key secure. Exposure of your private key can compromise the security of your funds.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details, contact @erickconstanza

---

For more details, refer to the [bitcoinlib documentation](https://bitcoinlib.org/) or the [Bitcoin network documentation](https://bitcoin.org/en/developer-documentation).

