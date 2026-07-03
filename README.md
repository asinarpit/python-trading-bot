# Python Trading Bot (Binance Futures Testnet)

This is a simplified Command Line Interface (CLI) application that places orders on the Binance Futures Testnet (USDT-M). It is built using Python, `python-binance`, `Typer` (for the CLI), and `Rich` (for enhanced terminal UI).

## 🛠️ Prerequisites
- Python 3.8+
- A Binance Futures Testnet Account
- Testnet API Key and API Secret

## 🚀 Setup Instructions

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/asinarpit/python-trading-bot.git
   cd python-trading-bot
   ```

2. **Install Dependencies**:
   It's recommended to use a virtual environment, but you can install the dependencies directly:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Copy the example environment file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```
   Open the `.env` file and replace the placeholder text with your actual Binance Testnet API credentials:
   ```env
   BINANCE_API_KEY=your_actual_api_key_here
   BINANCE_API_SECRET=your_actual_api_secret_here
   ```

## 💻 How to Run (Examples)

The application uses `Typer`, providing a clean CLI. The main command is `place`.

**1. Placing a MARKET Order:**
To place a MARKET order, you do not need to provide a price.
```bash
python cli.py place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.05
```

**2. Placing a LIMIT Order:**
To place a LIMIT order, you must provide a `--price` (or `-p`).
```bash
python cli.py place --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.1 --price 65000.50
```

**Shorthand flags are also supported:**
```bash
python cli.py place -s ETHUSDT --side BUY -t LIMIT -q 1.5 -p 3500.00
```

## 📜 Logging
All API requests, responses, and errors are securely logged to `trading_bot.log` in the root folder. You can check this file if you encounter any unexpected issues.

## 🧠 Assumptions & Notes
- The bot explicitly uses the **Binance Futures Testnet** (`testnet=True` is passed to the Binance Client). Do not use this code as-is for the live production network without changing the configuration.
- The default Time In Force for LIMIT orders is set to `GTC` (Good Till Cancelled).
