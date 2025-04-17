import requests
para = 'usd'
def fiyat_cekme(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids':coin,
        'vs_currencies': para
    }
    oku = requests.get(url,params=params)
    data = oku.json()
    return data[coin][para]

portfoy  = {
    'bitcoin': 4,
    'ethereum': 2,
    'solana':0
}

kasa_degeri = 0

for coin,miktar in portfoy.items():
    fiyat = fiyat_cekme(coin)
    deger = fiyat*miktar
    kasa_degeri += deger
print(f"Toplam kasa değeri: {kasa_degeri}{para}")



