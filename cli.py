import typer
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from bot.logging_config import setup_logger
from bot.client import get_binance_client
from bot.orders import place_order

# initialize typer app and console
app = typer.Typer(help="Binance Futures Testnet Trading Bot", no_args_is_help=True)
console = Console()

@app.command()
def ping():
    try:
        client = get_binance_client()
        console.print("[bold green] Successfully connected to Binance Futures Testnet![/bold green]")
    except Exception as e:
        console.print(f"[bold red] Connection Failed:[/bold red] {e}")

@app.command()
def place(
    symbol: str = typer.Option(..., "--symbol", "-s", help="Trading symbol, e.g., BTCUSDT"),
    side: str = typer.Option(..., "--side", help="Order side: BUY or SELL"),
    order_type: str = typer.Option(..., "--type", "-t", help="Order type: MARKET or LIMIT"),
    quantity: float = typer.Option(..., "--quantity", "-q", help="Order quantity"),
    price: float = typer.Option(None, "--price", "-p", help="Order price (Required for LIMIT orders)")
):

    # print req summary to terminal
    console.print("\n[bold cyan]Initiating Order Request...[/bold cyan]")
    req_table = Table(show_header=True, header_style="bold magenta")
    req_table.add_column("Symbol")
    req_table.add_column("Side")
    req_table.add_column("Type")
    req_table.add_column("Quantity")
    req_table.add_column("Price")
    
    req_table.add_row(
        symbol.upper(), 
        side.upper(), 
        order_type.upper(), 
        str(quantity), 
        str(price) if price else "N/A"
    )
    console.print(req_table)
    console.print()

    try:
        # api client (authenticated)
        client = get_binance_client()
        
        with console.status("[bold green]Sending request to Binance...[/bold green]"):
            result = place_order(client, symbol, side, order_type, quantity, price)

        if result["success"]:
            console.print("[bold green]✅ Order Success![/bold green]")
            res_table = Table(show_header=True, header_style="bold green")
            res_table.add_column("Order ID")
            res_table.add_column("Status")
            res_table.add_column("Executed Qty")
            res_table.add_column("Avg Price")
            
            res_table.add_row(
                str(result.get("orderId")),
                str(result.get("status")),
                str(result.get("executedQty")),
                str(result.get("avgPrice"))
            )
            console.print(res_table)
        else:
            console.print(f"[bold red] Order Failed:[/bold red] {result['message']}")
            console.print("[yellow]Check 'trading_bot.log' for more details.[/yellow]")

    except Exception as e:
        console.print(f"[bold red] Application Error:[/bold red] {e}")

if __name__ == "__main__":
    load_dotenv()
    setup_logger()
    app()
