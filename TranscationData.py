import requests

def get_compound_data(wallet):
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

    res = requests.post(url, json={'query': query})
    return res.json()
