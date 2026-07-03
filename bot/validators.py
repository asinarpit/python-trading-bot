def validate_symbol(symbol: str) -> str:
    # symbol should be at least 3 characters long
    if not symbol or len(symbol) < 3:
        raise ValueError("Symbol must be at least 3 characters long (e.g., BTCUSDT)")
    return symbol.upper()

def validate_side(side: str) -> str:
   # side must be BUY or SELL
    side_upper = side.upper()
    if side_upper not in ["BUY", "SELL"]:
        raise ValueError("Side must be exactly 'BUY' or 'SELL'")
    return side_upper

def validate_order_type(order_type: str) -> str:
    # order type must be MARKET or LIMIT
    order_upper = order_type.upper()
    if order_upper not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be exactly 'MARKET' or 'LIMIT'")
    return order_upper

def validate_quantity_and_price(order_type: str, quantity: float, price: float = None):
    # quantity should be greater than 0
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # if order type is limit price should be greater than 0
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("A positive price must be provided for a LIMIT order")
