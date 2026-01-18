import requests
import pandas as pd
from datetime import datetime
import os

# 1. Tentukan konstanta
FILE_NAME = "data/exchange_rates.csv"
API_URL = "https://api.frankfurter.app/latest?from=USD&to=IDR"

# 2. Extract Data dari API
response = requests.get(API_URL)
data = response.json()

rate = data['rates']['IDR']
date = data['date'] # Tanggal dari API
fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Rate USD ke IDR pada {date}: {rate}")

# 3. Transform ke DataFrame
new_data = {
    'date': [date],
    'rate_idr': [rate],
    'fetched_at': [fetch_time]
}
df_new = pd.DataFrame(new_data)

# 4. Load (Simpan/Append ke CSV)
# Cek apakah file sudah ada. Jika belum, buat folder dan filenya.
os.makedirs("data", exist_ok=True)

if os.path.exists(FILE_NAME):
    # Append tanpa header
    df_new.to_csv(FILE_NAME, mode='a', header=False, index=False)
else:
    # Buat file baru dengan header
    df_new.to_csv(FILE_NAME, mode='w', header=True, index=False)

print("Data berhasil disimpan!")