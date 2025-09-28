# Nama : Az-Zahra Imsawati Sugianto
# NIM : 2509116062
# Kelas : B
# Mata Kuliah : Dasar Dasar Pemrograman (Mini Project 2)

# Data panitia
data_panitia = []

# Daftar Panitia
daftar_panitia = [
    "ketua", "sekretaris", "bendahara",
    "acara", "konsumsi", "keamanan",
    "perlengkapan", "humas", "pdd"
]

# Login untuk ketua
user = {
    "username": "ketua",
    "password": "makrab123"
}

# Login hanya untuk ketua
def login_ketua():
    print("=== Login Ketua ===")
    username = input("Username: ")
    password = input("Password: ")
    if username == user["username"] and password == user["password"]:
        print("Login berhasil sebagai Ketua!")
        menu_ketua()
    else:
        print("Login gagal.")

# Menu ketua
def menu_ketua():
    while True:
        print("\n=== MENU KETUA ===")
        print("[1] Tambah Panitia")
        print("[2] Lihat Semua Panitia")
        print("[3] Hapus Panitia")
        print("[4] Tambah Tugas Panitia")
        print("[5] Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_panitia()
        elif pilihan == "2":
            lihat_semua_panitia()
        elif pilihan == "3":
            hapus_panitia()
        elif pilihan == "4":
            tambah_tugas()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

# Tambah panitia
def tambah_panitia():
    idp = input("ID Panitia: ")
    nama = input("Nama: ")
    jabatan = input("Jabatan: ")
    divisi = input("Divisi atau Jabatan: ")
    tugas_awal = input("Tugas: ")

    if not idp or not nama or not jabatan or not divisi:
        print("Semua data harus diisi.")
        return

    for p in data_panitia:
        if p["id"] == idp:
            print("ID sudah digunakan.")
            return

    if divisi not in daftar_panitia:
        print("Divisi atau jabatan tidak valid.")
        return

    data_panitia.append({
        "id": idp,
        "nama": nama,
        "jabatan": jabatan,
        "divisi": divisi,
        "tugas": [tugas_awal] if tugas_awal else [],
        "status": ["belum"] if tugas_awal else []
    })
    print("Panitia berhasil ditambahkan.")

# Lihat semua panitia
def lihat_semua_panitia():
    if not data_panitia:
        print("Belum ada data panitia.")
        return
    for p in data_panitia:
        print("\n=== Data Panitia ===")
        print("ID       :", p["id"])
        print("Nama     :", p["nama"])
        print("Jabatan  :", p["jabatan"])
        print("Divisi   :", p["divisi"])
        if p["tugas"]:
            print("Tugas:")
            i = 0
            while i < len(p["tugas"]):
                print(f"  {i+1}. {p['tugas'][i]} [{p['status'][i]}]")
                i += 1
        else:
            print("Tugas    : (Belum ada tugas)")

# Hapus panitia dengan alasan
def hapus_panitia():
    idp = input("Masukkan ID panitia yang ingin dihapus: ")
    for p in data_panitia:
        if p["id"] == idp:
            alasan = input("Masukkan alasan penghapusan panitia ini: ")
            print(f"\nPanitia dengan ID {idp} telah dihapus.")
            print(f"Alasan penghapusan: {alasan}")
            data_panitia.remove(p)
            return
    print("ID tidak ditemukan.")

# Tambah tugas ke panitia
def tambah_tugas():
    idp = input("Masukkan ID panitia: ")
    for p in data_panitia:
        if p["id"] == idp:
            tugas_baru = input("Tugas baru: ")
            if not tugas_baru:
                print("Tugas tidak boleh kosong.")
                return
            p["tugas"].append(tugas_baru)
            p["status"].append("belum")
            print("Tugas berhasil ditambahkan.")
            return
    print("ID tidak ditemukan.")

# Login dan akses panitia
def login_panitia():
    print("=== Login Panitia ===")
    nama = input("Masukkan nama Anda: ")
    password = input("Masukkan password: ")

    if password != "panitia2025":
        print("Password salah.")
        return

    for p in data_panitia:
        if p["nama"] == nama:
            print(f"\nHalo {p['nama']} dari divisi {p['divisi']}!")
            print("\n=== DATA SEMUA PANITIA ===")
            for panitia in data_panitia:
                print("\n---")
                print("ID       :", panitia["id"])
                print("Nama     :", panitia["nama"])
                print("Jabatan  :", panitia["jabatan"])
                print("Divisi   :", panitia["divisi"])
                if panitia["tugas"]:
                    print("Tugas:")
                    i = 0
                    while i < len(panitia["tugas"]):
                        print(f"  {i+1}. {panitia['tugas'][i]} [{panitia['status'][i]}]")
                        i += 1
                else:
                    print("Tugas    : (Belum ada tugas)")

            konfirmasi = input("\nIngin konfirmasi tugas Anda? (y/n): ")
            if konfirmasi == "y":
                if not p["tugas"]:
                    print("Anda belum memiliki tugas.")
                    return
                print("\nTugas Anda:")
                i = 0
                while i < len(p["tugas"]):
                    print(f"{i+1}. {p['tugas'][i]} [{p['status'][i]}]")
                    i += 1
                try:
                    no = int(input("Masukkan nomor tugas yang sudah selesai: "))
                    if 1 <= no <= len(p["tugas"]):
                        p["status"][no-1] = "selesai"
                        print("Status tugas diperbarui.")
                    else:
                        print("Nomor tugas tidak valid.")
                except ValueError:
                    print("Input harus berupa angka.")
            return

    print("Nama tidak ditemukan.")

# Menu utama
def menu_utama():
    while True:
        print("\n=== SISTEM PANITIA MAKRAB FT 25 ===")
        print("[1] Login Ketua")
        print("[2] Login Panitia")
        print("[3] Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            login_ketua()
        elif pilihan == "2":
            login_panitia()
        elif pilihan == "3":
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid.")

menu_utama()




