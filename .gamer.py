# import
import subprocess, os, platform, time

#variaveis de sistema
limpar = os.system("clear")
sistema = platform.system()
arquitetura = platform.machine()

# Dicionário com os nomes corrigidos para o YAY do CachyOS
apps = {
    1: "steam",
    2: "discord",
    3: "vlc",
    4: "wine-cachyos wine-cachyos-opt wine-staging wine-gecko wine-mono", # Pacotão Wine
    5: "winetricks",
    6: "goverlay",
    7: "lutris",
    8: "heroic-games-launcher-bin",
    9: "protonup-qt",
    10: "protontricks",
    11: "prismlauncher",
    12: "mangohud lib32-mangohud",
    13: "gamemode lib32-gamemode"
}

print("carregando codigo aguarde...")
time.sleep(2.0)
print("    atenção!!!")
time.sleep(1.0)
print("SÓ FUNCIONA EM CACHYOS FDP")
time.sleep(1.0)

print(f"""

██████╗  ██████╗ ███████╗████████╗ 
██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝ 
██████╔╝██║   ██║███████╗   ██║    
██╔═══╝ ██║   ██║╚════██║   ██║    
██║     ╚██████╔╝███████║   ██║    
╚═╝      ╚═════╝ ╚══════╝   ╚═╝    
                                   
███╗   ██╗███████╗██╗  ██╗████████╗
████╗  ██║██╔════╝╚██╗██╔╝╚══██╔══╝
██╔██╗ ██║█████╗   ╚███╔╝    ██║   
██║╚██╗██║██╔══╝   ██╔██╗    ██║   
██║ ╚████║███████╗██╔╝ ██╗   ██║   
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                   
 [+] PosNext Gamer Mode Installer
 
 [+] Installing Gamer Mode Apps...

 [+] sistema: {sistema}
 
 [+] arquitetura: {arquitetura}

 [+] {lista_gamer}
 


    """)


def instalar_apps(app):
 subprocess.run(["sudo", "yay", "-S", "--needed", "--noconfirm", app])

for app in lista_gamer:
    instalar_apps(app)
    
print(" [+] Gamer Mode Apps Installed Successfully!")

