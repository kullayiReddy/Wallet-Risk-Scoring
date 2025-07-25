import pandas as pd

wallets_df = pd.read_excel("Wallet id.xlsx")
wallets_df.columns = ["wallet_id"]
wallet_list = wallets_df["wallet_id"].tolist()
