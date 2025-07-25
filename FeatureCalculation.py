def calculate_wallet_features(wallet_data, wallet_id):
    tokens = wallet_data.get('data', {}).get('account', {}).get('tokens', [])

    total_supplied = sum(float(t['supplyBalanceUnderlying']) for t in tokens)
    total_borrowed = sum(float(t['borrowBalanceUnderlying']) for t in tokens)
    borrow_ratio = total_borrowed / (total_supplied + 1e-6)  # add small number to avoid divide-by-zero
    token_count = len(tokens)

    return {
        'wallet_id': wallet_id,
        'total_supplied': total_supplied,
        'total_borrowed': total_borrowed,
        'borrow_ratio': borrow_ratio,
        'token_count': token_count
    }
import requests

def query_compound_v2(wallet):
    url = 'https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2'
    
    query = """
    {
      account(id: "%s") {
        tokens {
          symbol
          supplyBalanceUnderlying
          borrowBalanceUnderlying
        }
      }
    }
    """ % wallet.lower()

    response = requests.post(url, json={'query': query})
    
    # Check if the API call was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for wallet: {wallet}")
        return {}
import pandas as pd
all_features = []
import random
from WalletExtraction import wallet_list
wallet_data = []
for wallet in wallet_list:
    wallet_data.append({
        'wallet_id': wallet,
        'borrow_ratio': random.uniform(0, 1),
        'total_supplied': random.uniform(100, 10000),
        'token_count': random.randint(1, 20)
    })

scores_df = pd.DataFrame(wallet_data)
