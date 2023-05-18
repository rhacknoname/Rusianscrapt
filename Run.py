import os
from colorama import init, Fore, Style
import subprocess

os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'

# Inisialisasi colorama
init()

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    if os.name == 'posix':  # Untuk sistem operasi berbasis Unix (Linux, macOS)
        os.system('clear')
    else:  # Untuk sistem operasi Windows
        os.system('cls')

# Fungsi untuk menampilkan header
def show_header():
    header = r"""
████████╗███████╗██████╗ ███████╗███████╗██████╗  █████╗  ██████╗████████╗
╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
   ██║   █████╗  ██████╔╝███████╗█████╗  ██████╔╝███████║██║        ██║   
   ██║   ██╔══╝  ██╔══██╗╚════██║██╔══╝  ██╔══██╗██╔══██║██║        ██║   
   ██║   ███████╗██║  ██║███████║███████╗██║  ██║██║  ██║╚██████╗   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝                                  
    """
    print(Fore.RED + header + Style.RESET_ALL)

# Fungsi untuk menampilkan menu
def show_menu():
    print(Fore.CYAN + "╔═════════════════════════════╗",Fore.GREEN+' Dev :'+Fore.WHITE+' RKun')
    print(Fore.CYAN + "║    "+Fore.LIGHTRED_EX+"1,000,000+ Doc Rusia"+Fore.CYAN+"     ║",Fore.LIGHTBLUE_EX+' Powered By:'+Fore.WHITE+' Terseract,Python3,OpenAI,Insomnia')
    print(Fore.CYAN + "╠═════════════════════════════╣"+Fore.YELLOW,' Lib:'+Fore.WHITE+' colorama,bs4,googletrans,request')
    print(Fore.CYAN + "║ "+Fore.WHITE+"1. Mulai mengambil database"+Fore.CYAN+" ║"+Fore.WHITE+'  program ini tidak mengambil top secret')
    print(Fore.CYAN + "║ "+Fore.WHITE+"2.     Lihat save file"+Fore.CYAN+"      ║",Fore.LIGHTRED_EX+' Gunakan informasi dengan bijak')
    print(Fore.CYAN + "║ "+Fore.WHITE+"3.         Keluar"+Fore.CYAN+"           ║",Fore.WHITE+' masukkan nomor untuk melihat dokumen lengkap')
    print(Fore.CYAN + "╚═════════════════════════════╝" + Style.RESET_ALL)
    print(Fore.RED+'Disc: ☢semua pengetahuan dan informasi dimiliki oleh rusia☢', Style.RESET_ALL)

# Fungsi untuk menjalankan aplikasi
def run_app():
    while True:
        clear_screen()
        show_header()
        show_menu()
        choice = input("Input: ")

        if choice == '1':
            clear_screen()
            print(Fore.GREEN + "      === Memulai pengambilan data ===\n"+Fore.CYAN+'Script ini memiliki 35 identitas palsu\njika terjadi error mungkin semua identitas palsu telah di blokir\nisi dengan identitas palsu yang baru\n')
            subprocess.run(["python", "Data.py"])

        elif choice == '2':
            clear_screen()
            print(Fore.GREEN + "=== DEKRIPSI PESAN ===")
            # Kode untuk menjalankan dekripsi pesan
            # ...

        elif choice == '3':
            clear_screen()
            print(Fore.YELLOW + "Keluar dari aplikasi." + Style.RESET_ALL)
            break

        else:
            clear_screen()
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()

        # Jeda sebelum kembali ke menu utama
        input("Tekan Enter untuk kembali ke menu utama...")
        clear_screen()

run_app()
