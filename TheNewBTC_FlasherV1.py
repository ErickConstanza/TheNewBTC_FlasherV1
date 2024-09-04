from bitcoinlib.wallets import Wallet, WalletError
from bitcoinlib.services.services import Service
import logging
from datetime import datetime

# Constants
FEE = 4  # Fee in satoshis
DEBUG = False
NETWORK = 'bitcoin'

def setup_logging(log_level=logging.DEBUG, log_file=None):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    bitcoinlib_logger = logging.getLogger('bitcoinlib')
    bitcoinlib_logger.setLevel(log_level)
    bitcoinlib_logger.propagate = True

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"debug_{current_time}.log"
setup_logging(log_level=logging.INFO, log_file=filename)

def check_transaction(wallet, txid):
    try:
        tx = wallet.gettransaction(txid)
        if tx:
            logging.info("Transaction found in wallet:")
            logging.info(tx.info())
            return True
        else:
            return False
    except Exception as e:
        logging.exception(f"Error checking transaction: {e}", e)
        return False

def update_wallet_data(wallet):
    logging.info(f"Updating wallet {wallet.name}")
    wallet.scan(scan_gap_limit=10)
    wallet.utxos_update()
    logging.info(f"DONE Updating wallet {wallet.name}")

def print_wallet_balance(wallet, service, name=""):
    balance_satoshi = wallet.balance()
    balance_btc = satoshi_to_btc(balance_satoshi)
    logging.info(f"Wallet {name} balance after scan: {balance_satoshi} satoshi")
    logging.info(f"Wallet {name} balance after scan: {balance_btc:.8f} BTC")
    addresses = [key.address for key in wallet.keys()]
    total_balance = 0
    for address in addresses:
        address_info = service.getbalance(address)
        logging.info(f"Wallet: {name}, Address: {address}, Balance: {address_info} satoshi")
        total_balance += address_info
    logging.info(f"Total balance for wallet {name} from service: {total_balance} satoshi")
    logging.info("")

def print_wallet_transaction(wallet):
    for t in wallet.transactions():
        logging.info(t.info())
        logging.info(f"Wallet {wallet.name} - Transaction {t.txid} - Status: {t.status}")

def satoshi_to_btc(satoshi):
    return satoshi / 100000000

def btc_to_satoshi(btc):
    return int(btc * 100000000)

def main():
    # Get user input for private key and addresses
    private_key = input("Enter the sender's private key: ")
    recipient_address = input("Enter the recipient address: ")

    # Create or load the wallet
    try:
        wallet = Wallet.create(name='imported_wallet', network=NETWORK)
        wallet.import_key(private_key)
        logging.info("Wallet created and key imported from private key.")
        logging.info(f"Wallet network is {wallet.network.name}")
        logging.info(f"Sender Wallet address is {wallet.get_key().address}")
    except WalletError as e:
        logging.error("Failed to create or load wallet. Error: " + str(e))
        return

    # Service for the network
    try:
        service = Service(network=NETWORK)
    except Exception as e:
        logging.error(f"Failed to create service for network {NETWORK}. Error: {e}")
        return

    # Update wallet data
    update_wallet_data(wallet)
    print_wallet_balance(wallet, service, wallet.name)

    # Get user input for amount to send
    amount_btc = float(input("Enter the amount of BTC you want to send: "))
    amount_satoshi = btc_to_satoshi(amount_btc)

    # Send transaction
    logging.info(f"Sending {amount_btc} BTC from {wallet.get_key().address} to {recipient_address}")
    outputs = [(recipient_address, amount_satoshi)]
    try:
        tx = wallet.send(outputs, fee=FEE, network=NETWORK, offline=DEBUG)
        logging.info(f"Transaction sent. TXID: {tx.txid}")
        check_transaction(wallet, tx.txid)
    except WalletError as e:
        logging.error(f"Error sending transaction: {e}")

if __name__ == "__main__":
    main()
