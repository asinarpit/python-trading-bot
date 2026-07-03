import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from .validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity_and_price
)

logger = logging.getLogger("trading_bot")

def place_order(client: Client, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:

    try:
        # input validations
        valid_symbol = validate_symbol(symbol)
        valid_side = validate_side(side)
        valid_type = validate_order_type(order_type)
        validate_quantity_and_price(valid_type, quantity, price)
        
        # logging pre req details
        logger.info(f"Attempting to place {valid_type} {valid_side} order for {quantity} {valid_symbol}")
        
        # construct api call arguments
        order_params = {
            "symbol": valid_symbol,
            "side": valid_side,
            "type": valid_type,
            "quantity": quantity
        }
        
        # price and timeInForce for limit order
        if valid_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"
            
        response = client.futures_create_order(**order_params)
        
        logger.info(f"Order successfully placed!! Order ID: {response.get('orderId')}")
        
        return {
            "success": True,
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty", 0),
            "avgPrice": response.get("avgPrice", 0),
            "message": "Order placed successfully."
        }

    # binance order exc
    except BinanceOrderException as e:
        logger.error(f"Binance Order Exception: {e}")
        return {"success": False, "message": str(e)}
        
    # general Binance API exc
    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e}")
        return {"success": False, "message": str(e)}
        
    except ValueError as e:
        logger.warning(f"Validation Error: {e}")
        return {"success": False, "message": str(e)}
        
    except Exception as e:
        logger.error(f"Unexpected error while placing order: {e}")
        return {"success": False, "message": f"Unexpected error: {str(e)}"}
