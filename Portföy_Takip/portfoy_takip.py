import requests

def fiyat_cekme(coin,para):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids':coin,
        'vs_currencies': para
    }

    try:
        oku = requests.get(url, params= params)
        data = oku.json()

        if coin not in data or para not in data[coin]:
            print(f"{coin} için fiyat bilgisi alınamadı")
            return 0
        return data[coin][para]
    
    except requests.exceptions.RequestException as x:
        print(f"{coin} fiyatı çekilirken hata oluştu:{x}")
        return 0

def para_birimi():
    para = input("Lütfen para biriminizi seçiniz(TRY,USD,EUR):").strip().lower()
    
    while para not in["try","usd","eur"]:
        print("Desteklenmeyen para birimi girdiniz.")
        para = input("Lütfen şu para birimlerinden birini seçiniz-->TRY,USD,EUR:").strip().lower()
    return para

portfoy  = {
    'bitcoin': 0.5,
    'ethereum': 4,
    'solana':1
}
para = para_birimi()
kasa_degeri = 0

for coin,miktar in portfoy.items():
    fiyat = fiyat_cekme(coin,para)
    deger = fiyat*miktar
    kasa_degeri += deger
print(f"Toplam kasa değeri: {kasa_degeri}{para}")