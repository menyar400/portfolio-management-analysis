# Portfolio Management Project

## 🎯 Overview
Constructed a diversified 10-stock portfolio (600 TND) using Modern Portfolio Theory and Markowitz optimization, achieving a **2.84% return** over a 6-day holding period with a **Sharpe ratio of 1.2**. This project demonstrates end-to-end portfolio construction—from broker selection and macroeconomic analysis to performance evaluation.

---

## 📊 Key Achievements
- **Strategic Broker Selection**: Negotiated transaction fees down to 2 basis points per trade with BH Invest
- **Comprehensive Stock Screening**: Analyzed 70+ stocks, filtered to 20, and selected top 10 using weighted scoring models
- **Portfolio Optimization**: Implemented Markowitz efficient frontier with Sharpe ratio maximization
- **Automated Technical Analysis**: Python scripts generating MACD, RSI, and Bollinger Bands for optimal entry/exit timing
- **Risk Management**: Multi-layered approach including stop-loss strategies, scenario analysis, and portfolio rebalancing
- **Top Performance**: 5.05% gain on best-performing stock

---

## 📁 Project Structure
```
portfolio-management-analysis/
├── data/
│   └── portfolio_workbook.xlsx      # Main Excel analysis workbook
├── code/
│   └── technical_analysis.py        # Python automation scripts
├── reports/
│   └── final_report.pdf             # Detailed project documentation
├── presentation/
│   └── project_presentation.pptx    # Executive summary slides
└── README.md                         # Project overview (this file)
```

---

## 🔬 Methodology

### Phase 0: Broker Selection
- Evaluated multiple brokerage platforms based on fees, platform reliability, and execution quality
- Selected **BH Invest** as primary broker
- Successfully negotiated transaction commission fees down to **2 basis points per trade**, significantly reducing portfolio costs

### Phase 1: Macroeconomic & Sectorial Analysis
- Assessed macroeconomic environment and market conditions
- Conducted sector-level analysis across multiple industries
- Established screening criteria for stock selection based on economic outlook

### Phase 2: Stock Screening & Fundamental Analysis
- **Initial Universe**: 70+ stocks across diverse sectors
- **First Filter**: Narrowed to 20 stocks using weighted scoring model
- **Fundamental Analysis**: Comprehensive evaluation of 20 finalists across:
  - **Profitability**: ROE (Return on Equity), Net Profit Margin
  - **Liquidity**: Current Ratio
  - **Solvency**: Debt-to-Equity Ratio
  - **Valuation**: P/E Ratio, Dividend Yield
  - **Growth**: EPS (Earnings Per Share), DPS (Dividends Per Share)
- **Final Selection**: Top 10 stocks based on comprehensive weighted scores

 ### Phase 3: Historical Data & Risk Assessment
- Compiled 10 years of daily returns for all 20 finalist stocks
- Constructed covariance matrix for Markowitz optimization (capturing correlations and volatilities)

### Phase 4: Portfolio Optimization (Markowitz Model)
- Implemented Modern Portfolio Theory using Excel Solver
- Optimized portfolio weights to maximize Sharpe ratio
- **Final Allocation**: 10 stocks with risk-optimized weights

### Phase 5: Performance Monitoring & Rebalancing
- Built an Excel dashboard 
- Monitored daily performance against market benchmarks
- Conducted scenario analysis under various market conditions
- Developed systematic rebalancing strategy to maintain optimal risk profile

### Phase 6: Technical Analysis Automation
- Generated Technical indicators using Python (`pandas`, `matplotlib`)
- **MACD (Moving Average Convergence Divergence)**: Trend-following momentum indicator
- **RSI (Relative Strength Index)**: Overbought/oversold identification
- **Bollinger Bands**: Volatility-based entry/exit signals

---

## 🛠️ Technologies & Tools

**Excel** (Primary Tool)
- Advanced formulas and financial functions
- Solver add-in for portfolio optimization
- Interactive dashboards with dynamic charts
- Data validation and conditional formatting

**Python**
- `pandas` – Data manipulation and time-series analysis
- `matplotlib` – Visualization of technical indicators and signals

**Financial Frameworks**
- Modern Portfolio Theory (MPT)
- Markowitz Mean-Variance Optimization
- Sharpe Ratio Maximization
- Technical Analysis (MACD, RSI, Bollinger Bands)

---

## 📈 Results

| Metric | Value |
|--------|-------|
| **Total Return** | 2.84% (6-day period) |
| **Sharpe Ratio** | 1.2 |
| **Best Performer** | 5.05% gain |
| **Portfolio Size** | 549.14 TND (9 stocks) |
| **Transaction Costs** | 2 bps per trade |
| **Risk Management** | Multi-layered downside protection |

---

## 📂 Files Description

### `data/portfolio_workbook.xlsx`
**The centerpiece of this project** – A comprehensive Excel workbook containing:
- Macroeconomic and sectorial analysis
- 70+ stock initial screening with weighted scoring methodology
- In-depth fundamental analysis of 20 finalist stocks
- 10 years of historical daily returns
- Markowitz optimization model
- Portfolio rebalancing analysis
- Return evaluation and performance attribution
- Performance dashboard with visualizations
  
### `code/technical_analysis.py`
Python scripts for technical analysis, including MACD, RSI, and Bollinger Bands calculations for optimal entry/exit timing.

### `reports/final_report.pdf`
Comprehensive documentation covering methodology, analytical process, findings, and return evaluation with supporting evidence.

### `presentation/project_presentation.pptx`
Executive summary presentation highlighting key methodology, results, and strategic insights.

---

## 🎓 Academic Context
This project was completed as part of the **Financial Markets** course at **Tunis Business School** (August 2025 - January 2026).

---

## 📧 Contact
**Menyare Zitouni**  
📩 menyare.zitouni12@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/menyare-zitouni-236785299)  
📍 Tunis, Tunisia

---

## 📝 License
This project is available for educational and portfolio demonstration purposes.

---

*Built with Excel, Python, and a passion for quantitative finance* 📊
