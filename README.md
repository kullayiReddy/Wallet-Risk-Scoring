# Wallet-Risk-Scoring

# 💼 Wallet Risk Scoring From Scratch

## 🧠 Overview

This project focuses on calculating risk scores for Ethereum wallets based on their interactions with the Compound V2 DeFi lending protocol. Given a list of wallet addresses, we retrieve their on-chain transaction data, engineer meaningful features, and compute a **risk score from 0 to 1000** for each wallet. This scoring helps assess the financial behavior and reliability of each wallet from a risk perspective.

---

## 🧾 Problem Statement

> You are given 100 wallet addresses. Your goal is to analyze their activity on the Compound V2 protocol and assign each wallet a **risk score (0–1000)** based on parameters derived from transaction history.

---

## 🔍 Data Collection

- Wallet addresses were sourced from [this spreadsheet](https://docs.google.com/spreadsheets/d/1ZzaeMgNYnxvriYYpe8PE7uMEblTI0GV5GIVUnsP-sBs/edit?usp=sharing).
- Used the **Covalent API** to fetch:
  - Lending and borrowing transactions
  - Supplied and borrowed amounts
  - Token types interacted with

---

## ⚙️ Feature Engineering

The following features were extracted or derived:

| Feature              | Description |
|----------------------|-------------|
| `total_supplied`     | Total amount the wallet has supplied to the protocol |
| `total_borrowed`     | Total borrowed amount |
| `borrow_ratio`       | Ratio = total_borrowed / (total_supplied + ε) |
| `token_count`        | Number of unique tokens interacted with |
| `borrow_ratio_scaled` | Normalized value of `borrow_ratio` |
| `supplied_scaled`     | Normalized value of `total_supplied` |
| `tokens_scaled`       | Normalized value of `token_count` |

---

## 📊 Scoring Method

1. **Min-Max Normalization** was applied to key features (`borrow_ratio`, `total_supplied`, `token_count`) to bring them to a 0–1 scale.
2. A **weighted risk score** was calculated using:
   ```python
   weighted_score = 0.5 * borrow_ratio_scaled + 0.3 * supplied_scaled + 0.2 * tokens_scaled


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
