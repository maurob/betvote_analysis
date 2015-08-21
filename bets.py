import urllib, json

address = [
    "1MKxXQvNjS78WaeZniUBKB5hbGwDSPzBTt", # SCIOLI
    "1J6LQKpcYTN5EEs9Ly1sEmNbWx6MFZ4NVT", # MACRI
    "1NbYpjej4tUG1LoXNcaHXEAv2BrNaE3Qn8", # MASSA
    "14ABDAcQ5vXQkKpmNHZfzEb8Ki1Thrr7gy", # DEL CANO 
    "15idxQtkbpox9xKDQGxqjoqiqpWMEeTwgJ", # STOLBIZER
    "1KnApPxStmyPds8ngsbPm8KFDRB2Rcvt9r", # SAA
    ]

addresses_query = "|".join(address)

url = "https://blockchain.info/multiaddr?cors=true&api_code=0fe3c82d-156d-405e-b8d4-eff695003036&active="+addresses_query
order = [3, 5, 0, 1, 2, 4]

satoshi = 100000000
profit = 0.8

paso = [39.8, 34.9, 18.7, 3.31, 3.51, 2.11]

def balance(data):
    return [data['addresses'][i]['total_received'] for i in order]

def sat_one(value):
    return 1 if value < 1 else round(value, 2)

def bet(balance):
    N = len(address)
    total_balance_candidates = sum(balance)
    return [sat_one((total_balance_candidates / b * profit) / (N / 100 * p)) for b, p in zip(balance, paso)]

def getJSON(url):
    response = urllib.request.urlopen(url);
    read_data = response.read()
    return json.loads(read_data.decode())