def hitung_huruf(string_input):
    # menggunakan metode len()untuk menghitung total karakter 
    total_karakter = len(string_input)
    return total_karakter

# contoh penggunaan
teks="hahaha!"
jumlah= hitung_huruf(teks)
print(f"jumlah total karakter dalam'{teks}' adalah: {jumlah}")