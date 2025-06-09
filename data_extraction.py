import json
import os
from dotenv import load_dotenv
import requests
from typing import List, Dict, Any
from collections import defaultdict

# Load environment variables
load_dotenv()

# API Configuration
FMP_API_KEY = os.getenv("FMP_API_KEY")
if not FMP_API_KEY:
    raise ValueError("FMP_API_KEY environment variable is not set")

def get_jsonparsed_data(url: str) -> Dict[str, Any]:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_to_json(data: Any, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Data has been saved to {filename}")

def get_stock_list() -> List[Dict[str, Any]]:
    """
    Fetch the complete list of stocks from FMP API.
    """
    url = f"https://financialmodelingprep.com/stable/stock/list?apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def extract_symbols(stock_data: List[Dict[str, Any]]) -> List[str]:
    """
    Extract stock symbols from stock data.
    """
    return [stock['symbol'] for stock in stock_data]

def get_analyst_estimates(symbol: str, period: str = "annual", page: int = 0, limit: int = 10) -> Dict[str, Any]:
    """
    Fetch analyst estimates for a specific stock.
    """
    url = f"https://financialmodelingprep.com/stable/analyst-estimates?symbol={symbol}&period={period}&page={page}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_sma(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    """
    Fetch Simple Moving Average (SMA) technical indicator data.
    """
    url = f"https://financialmodelingprep.com/stable/technical-indicators/sma?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_ema(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/technical-indicators/ema?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_wma(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/technical-indicators/wma?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_dema(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/technical-indicators/dema?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_tema(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/technical-indicators/tema?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_rsi(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/technical-indicators/rsi?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_williams(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/technical-indicators/williams?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_adx(symbol: str, period_length: int = 10, timeframe: str = "1day") -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/technical-indicators/adx?symbol={symbol}&periodLength={period_length}&timeframe={timeframe}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_latest_news(page: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
    url = f"https://financialmodelingprep.com/stable/news/stock-latest?page={page}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_price_target_news(symbol: str, page: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Fetch price target news for a specific stock.
    """
    url = f"https://financialmodelingprep.com/stable/price-target-news?symbol={symbol}&page={page}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_historical_grades(symbol: str) -> List[Dict[str, Any]]:
    """
    Fetch historical stock grades for a specific stock.
    """
    url = f"https://financialmodelingprep.com/stable/grades-historical?symbol={symbol}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_dividends(symbol: str) -> List[Dict[str, Any]]:
    """
    Fetch dividend data for a specific stock.
    """
    url = f"https://financialmodelingprep.com/stable/dividends?symbol={symbol}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_custom_dcf(symbol: str) -> Dict[str, Any]:
    """
    Fetch custom DCF analysis for a specific stock using the FMP Custom DCF Advanced API.
    """
    url = f"https://financialmodelingprep.com/stable/custom-discounted-cash-flow?symbol={symbol}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def merge_indicators_by_date(indicators: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Merge all technical indicators by date.
    """
    merged_data = defaultdict(dict)
    
    for indicator_name, indicator_data in indicators.items():
        for data_point in indicator_data:
            date = data_point['date']
            if date not in merged_data:
                merged_data[date].update({
                    'date': date,
                    'open': data_point.get('open'),
                    'high': data_point.get('high'),
                    'low': data_point.get('low'),
                    'close': data_point.get('close'),
                    'volume': data_point.get('volume')
                })
            merged_data[date][indicator_name] = data_point.get(indicator_name)
    
    result = list(merged_data.values())
    result.sort(key=lambda x: x['date'], reverse=True)
    return result

def get_all_technical_indicators(symbol: str, period_length: int = 10000, timeframe: str = "1day") -> Dict[str, Any]:
    """
    Fetch all technical indicators for a given symbol.
    """
    indicators = {
        "sma": get_sma(symbol, period_length, timeframe),
        "ema": get_ema(symbol, period_length, timeframe),
        "wma": get_wma(symbol, period_length, timeframe),
        "dema": get_dema(symbol, period_length, timeframe),
        "tema": get_tema(symbol, period_length, timeframe),
        "rsi": get_rsi(symbol, period_length, timeframe),
        "williams": get_williams(symbol, period_length, timeframe),
        "adx": get_adx(symbol, period_length, timeframe)
    }
    return indicators

def get_historical_employee_count(symbol: str, limit: int = 100) -> List[Dict[str, Any]]:
    url = f"https://financialmodelingprep.com/stable/historical-employee-count?symbol={symbol}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_shares_float(symbol: str) -> Dict[str, Any]:
    url = f"https://financialmodelingprep.com/stable/shares-float?symbol={symbol}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_historical_market_cap(symbol: str, limit: int = 10000) -> List[Dict[str, Any]]:
    url = f"https://financialmodelingprep.com/stable/historical-market-capitalization?symbol={symbol}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_income_statement(symbol: str, limit: int = 10000, period: str = "FY") -> List[Dict[str, Any]]:
    url = f"https://financialmodelingprep.com/stable/income-statement?symbol={symbol}&limit={limit}&period={period}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_balance_sheet(symbol: str, limit: int = 10000, period: str = "FY") -> List[Dict[str, Any]]:
    url = f"https://financialmodelingprep.com/stable/balance-sheet-statement?symbol={symbol}&limit={limit}&period={period}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_cash_flow(symbol: str, limit: int = 10000, period: str = "FY") -> List[Dict[str, Any]]:
    url = f"https://financialmodelingprep.com/stable/cash-flow-statement?symbol={symbol}&limit={limit}&period={period}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_key_metrics(symbol: str, limit: int = 120) -> List[Dict[str, Any]]:
    """
    Fetch key financial metrics.
    """
    url = f"https://financialmodelingprep.com/stable/key-metrics?symbol={symbol}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_financial_ratios(symbol: str, limit: int = 120) -> List[Dict[str, Any]]:
    """
    Fetch financial ratios.
    """
    url = f"https://financialmodelingprep.com/stable/ratios?symbol={symbol}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def merge_quarterly_fundamental_data(symbol: str) -> List[Dict[str, Any]]:
    """
    Merge all quarterly financial data into a single list, combining income statement,
    balance sheet, and cash flow data for each date.
    """
    # Get all types of financial data
    income_data = get_income_statement(symbol, period='quarter')
    balance_data = get_balance_sheet(symbol, period='quarter')
    cash_flow_data = get_cash_flow(symbol, period='quarter')
    
    # Create a dictionary to store merged data by date
    merged_data = defaultdict(dict)
    
    # Process each type of data
    for data in [income_data, balance_data, cash_flow_data]:
        for item in data:
            date = item['date']
            # Add all fields from the item to the merged data
            merged_data[date].update(item)
    
    # Convert to list and sort by date in descending order
    result = list(merged_data.values())
    result.sort(key=lambda x: x['date'], reverse=True)
    return result

def get_owner_earnings(symbol: str, limit: int = 10000) -> List[Dict[str, Any]]:
    """
    Fetch owner earnings data for a company.
    """
    url = f"https://financialmodelingprep.com/stable/owner-earnings?symbol={symbol}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_enterprise_values(symbol: str, limit: int = 10000) -> List[Dict[str, Any]]:
    """
    Fetch enterprise values data for a company.
    """
    url = f"https://financialmodelingprep.com/stable/enterprise-values?symbol={symbol}&limit={limit}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def get_financial_growth(symbol: str, limit: int = 10000, period: str = "FY") -> List[Dict[str, Any]]:
    """
    Fetch comprehensive financial growth data for a company.
    """
    url = f"https://financialmodelingprep.com/stable/financial-growth?symbol={symbol}&limit={limit}&period={period}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def merge_financial_growth_data(symbol: str) -> List[Dict[str, Any]]:
    """
    Merge quarterly growth data into a single sorted list.
    """
    growth_data = get_financial_growth(symbol, period='quarter')
    growth_data.sort(key=lambda x: x['date'], reverse=True)
    return growth_data

def get_as_reported_financial_statement(symbol: str, limit: int = 10000, period: str = "quarter") -> List[Dict[str, Any]]:
    """
    Fetch comprehensive as-reported financial statements data for a company.
    """
    url = f"https://financialmodelingprep.com/stable/financial-statement-full-as-reported?symbol={symbol}&limit={limit}&period={period}&apikey={FMP_API_KEY}"
    return get_jsonparsed_data(url)

def merge_as_reported_financial_data(symbol: str) -> List[Dict[str, Any]]:
    """
    Merge all as-reported financial statements into a single sorted list.
    """
    financial_data = get_as_reported_financial_statement(symbol, period='quarter')
    financial_data.sort(key=lambda x: x['date'], reverse=True)
    return financial_data

def main():
    # Get complete stock list
    print("Fetching stock list...")
    stock_data = get_stock_list()
    save_to_json(stock_data, "stock_list.json")
    print("Stock list has been saved to stock_list.json")
    
    # Extract and save symbols
    symbols = extract_symbols(stock_data)
    save_to_json(symbols, "symbols.json")
    print("Symbols have been exported to symbols.json")
    
    # Get price target news for Apple
    symbol = "AAPL"
    print(f"\nFetching price target news for {symbol}...")
    price_target_news = get_price_target_news(symbol, limit=50)
    save_to_json(price_target_news, f"{symbol}_price_target_news.json")
    print(f"Price target news for {symbol} has been saved to {symbol}_price_target_news.json")
    
    # Get historical grades for Apple
    print(f"\nFetching historical grades for {symbol}...")
    historical_grades = get_historical_grades(symbol)
    save_to_json(historical_grades, f"{symbol}_historical_grades.json")
    print(f"Historical grades for {symbol} have been saved to {symbol}_historical_grades.json")
    
    # Get dividend data for Apple
    print(f"\nFetching dividend data for {symbol}...")
    dividend_data = get_dividends(symbol)
    save_to_json(dividend_data, f"{symbol}_dividends.json")
    print(f"Dividend data for {symbol} has been saved to {symbol}_dividends.json")
    
    # Get custom DCF analysis for Apple
    print(f"\nFetching custom DCF analysis for {symbol}...")
    dcf_data = get_custom_dcf(symbol)
    save_to_json(dcf_data, f"{symbol}_dcf_analysis.json")
    print(f"Custom DCF analysis for {symbol} has been saved to {symbol}_dcf_analysis.json")
    
    # Get historical employee count for Apple
    print(f"\nFetching historical employee count for {symbol}...")
    employee_data = get_historical_employee_count(symbol, limit=10000)
    save_to_json(employee_data, f"{symbol}_employee_count.json")
    print(f"Historical employee count for {symbol} has been saved to {symbol}_employee_count.json")
    
    # Get shares float data for Apple
    print(f"\nFetching shares float data for {symbol}...")
    shares_float_data = get_shares_float(symbol)
    save_to_json(shares_float_data, f"{symbol}_shares_float.json")
    print(f"Shares float data for {symbol} has been saved to {symbol}_shares_float.json")
    
    # Get historical market cap data for Apple
    print(f"\nFetching historical market cap data for {symbol}...")
    market_cap_data = get_historical_market_cap(symbol)
    save_to_json(market_cap_data, f"{symbol}_historical_market_cap.json")
    print(f"Historical market cap data for {symbol} has been saved to {symbol}_historical_market_cap.json")
    
    # Get and merge fundamental data for Apple
    print(f"\nFetching and merging fundamental data for {symbol}...")
    fundamental_data = merge_quarterly_fundamental_data(symbol)
    save_to_json(fundamental_data, f"{symbol}_fundamental_data.json")
    print(f"Merged fundamental data for {symbol} has been saved to {symbol}_fundamental_data.json")
    
    # Get owner earnings data
    print(f"\nFetching owner earnings data for {symbol}...")
    owner_earnings_data = get_owner_earnings(symbol)
    save_to_json(owner_earnings_data, f"{symbol}_owner_earnings.json")
    print(f"Owner earnings data for {symbol} has been saved to {symbol}_owner_earnings.json")
    
    # Get enterprise values data
    print(f"\nFetching enterprise values data for {symbol}...")
    enterprise_values_data = get_enterprise_values(symbol)
    save_to_json(enterprise_values_data, f"{symbol}_enterprise_values.json")
    print(f"Enterprise values data for {symbol} has been saved to {symbol}_enterprise_values.json")
    
    # Get and merge growth data
    print(f"\nFetching and merging growth data for {symbol}...")
    merged_growth = merge_financial_growth_data(symbol)
    save_to_json(merged_growth, f"{symbol}_financial_growth.json")
    print(f"Merged growth data for {symbol} has been saved to {symbol}_financial_growth.json")
    
    # Get and merge all as-reported financial statements
    print(f"\nFetching and merging all as-reported financial statements for {symbol}...")
    merged_as_reported = merge_as_reported_financial_data(symbol)
    save_to_json(merged_as_reported, f"{symbol}_as_reported_financial_statements.json")
    print(f"Comprehensive as-reported financial statements for {symbol} have been saved to {symbol}_as_reported_financial_statements.json")
    
    # Get all technical indicators for Apple
    print(f"\nFetching technical indicators for {symbol}...")
    technical_data = get_all_technical_indicators(symbol, period_length=10000)
    print("Merging indicators by date...")
    merged_data = merge_indicators_by_date(technical_data)
    save_to_json(merged_data, f"{symbol}_technical_indicators.json")
    print(f"Merged technical indicators for {symbol} have been saved to {symbol}_technical_indicators.json")

if __name__ == "__main__":
    main()





