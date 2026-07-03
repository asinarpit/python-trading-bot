import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

logger = logging.getLogger("trading_bot")

def get_binance_client():
    # env api keys
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("API keys missing")
        raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET not found")

    try:
        # testnet true for fake money
        client = Client(api_key, api_secret, testnet=True)
        client.ping()
        logger.info("Successfully connected to Binance Futures Testnet")
        
        return client
    
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error connecting to Binance: {e}")
        raise
