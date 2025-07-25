# Wallet-Risk-Scoring

# 🧮 Wallet Risk Scoring System

This project calculates risk scores (0–1000) for crypto wallet addresses based on their activity in the Compound V2/V3 protocol.

## 📊 Features Used for Scoring

- **Borrow Ratio**: Amount borrowed relative to supplied.
- **Total Supplied**: Cumulative assets supplied.
- **Token Count**: Number of distinct tokens used.

Each feature is normalized and weighted:
- Borrow Ratio: 50%
- Total Supplied: 30%
- Token Count: 20%

## 🛠️ How It Works

1. Load wallet activity data from Excel.
2. Calculate borrow_ratio = total_borrow / total_supply.
3. Normalize all features.
4. Compute weighted score.
5. Scale scores between 0 and 1000.

## 📁 Files

- `wallet_risk_scoring.ipynb`: Jupyter notebook with step-by-step scoring.
- `Wallet_id.xlsx`: Raw input data (moved to `data/` folder).
- `wallet_scores.csv`: Output scores (in `output/` folder).

## Verify for the colab Link 
https://colab.research.google.com/drive/137ZnLK518FmhZVWotBafyLonD2uGgtAn?usp=sharing

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
