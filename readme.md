# Aplikasi Cuaca dengan Tkinter

Aplikasi sederhana ini memungkinkan Anda untuk mendapatkan informasi cuaca berdasarkan nama kota. Aplikasi menggunakan API Weatherstack untuk mengambil data cuaca aktual. Berikut adalah instruksi untuk menjalankan aplikasi ini:

## Langkah 1: API Key Weatherstack

Untuk menjalankan aplikasi ini, Anda perlu memiliki kunci API Weatherstack. Anda dapat mendaftar untuk mendapatkan kunci API di [Weatherstack](https://weatherstack.com/).

Setelah Anda mendapatkan kunci API, gantilah nilai `api_key` dalam kode dengan kunci API Anda. Temukan baris berikut dalam kode:

```python
api_key = "9fcef865b55b7d1aa2a8e9eec609a8df"  # Ganti dengan API key Anda
```

Gantilah `"9fcef865b55b7d1aa2a8e9eec609a8df"` dengan kunci API Anda.

## Langkah 2: Menjalankan Aplikasi

Anda dapat menjalankan aplikasi ini dengan menjalankan kode Python di terminal atau lingkungan pengembangan Python Anda. Pastikan Anda memiliki modul `tkinter` dan `requests` terinstal. Jika tidak, Anda dapat menginstalnya dengan perintah berikut:

```bash
pip install tkinter requests
```

Kemudian, jalankan kode dengan perintah berikut:

```bash
python nama_file.py
```

Gantilah `nama_file.py` dengan nama file tempat Anda menyimpan kode ini.

## Langkah 3: Menggunakan Aplikasi

1. Setelah Anda menjalankan aplikasi, jendela aplikasi akan muncul.
2. Masukkan nama kota yang ingin Anda cek cuacanya ke dalam kotak teks yang disediakan.
3. Klik tombol "Dapatkan Cuaca".
4. Hasil cuaca akan ditampilkan di bawah tombol dalam bentuk teks.

**Catatan:** Pastikan komputer Anda terhubung ke internet karena aplikasi ini membutuhkan koneksi internet untuk mengambil data cuaca dari API Weatherstack.
