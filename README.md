# Sector Volatility Analysis

This project analyzes **seven years** of historical stock data (2018–2025) to evaluate volatility and risk-adjusted returns across major market sectors. Using Python and key financial metrics such as daily returns, rolling volatility, and Sharpe Ratios, it identifies which sectors offer higher stability or better long-term performance.

## Problem Statement
Investors often struggle to assess which sectors are riskier or more resilient during changing market conditions. This project provides a data-driven framework to compare sector-level performance and inform smarter portfolio strategies.

## Objectives
- Pull and clean 7 years of daily stock price data using `yfinance`
- Map stock tickers to their corresponding sectors
- Calculate daily returns, rolling volatility, and Sharpe Ratios
- Compare sector performance over time and visualize insights

## Dataset Overview

This project uses historical daily stock price data pulled via the [yfinance](https://pypi.org/project/yfinance/) API for a 7-year period from **June 1, 2018 to June 1, 2025**.

### Sectors Analyzed:
The selected sectors represent major areas of the economy to ensure broad comparability:

- Technology
- Healthcare
- Financials
- Energy
- Consumer Discretionary
- Industrials
- Utilities
- Real Estate

### Sample Tickers Used per Sector:
| Sector              | Example Tickers         |
|---------------------|-------------------------|
| Technology          | AAPL, MSFT, NVDA        |
| Healthcare          | JNJ, PFE, UNH           |
| Financials          | JPM, BAC, WFC           |
| Energy              | XOM, CVX, COP           |
| Consumer Discretionary | AMZN, TSLA, HD       |
| Industrials         | BA, CAT, GE             |
| Utilities           | NEE, DUK, SO            |
| Real Estate         | PLD, AMT, SPG           |

The tickers are mapped to their corresponding sectors manually or via metadata from `yfinance`.


## Tools & Technologies
- **Python**, **Pandas**, **NumPy**
- **yfinance** (stock data source)
- **Matplotlib**, **Seaborn** (visualization)
- **Jupyter Notebook**

## Folder Structure
