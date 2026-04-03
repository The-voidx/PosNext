# imports
import subprocess, os, time, platform


os.system("clear")

sistema = platform.system()
arquitetura = platform.machine()

# Dicionário que mcontém o número ao nome real do pacote
apps = {
    1: "libreoffice-fresh",
    2: "onlyoffice-bin",
    3: "gimp photogimp-git",
    4: "wps-office",
    5: "anydesk-bin",
    6: "davinci-resolve",
    7: "cohesion-bin",
    8: "audacity",
    9: "darktable",
    10: "foliate",
    11: "inkscape",
    12: "freecad",
    13: "kicad",
    14: "kdenlive",
    15: "figma-linux-bin",
    16: "obsidian",
    17: "pinta",
    18: "logseq-desktop-bin",
    19: "standardnotes-bin",
    20: "cryptomator-bin",
    21: "freemind",
    22: "zettlr-bin",
    23: "copyq"
}

def reiniciar():
    os.system("python .developer.py")

print(f"""
______________________________________________

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
                                   
 [+] PosNext office apps Installer
 
 [+] Installing office Apps...

 [+] sistema: {sistema}
 
 [+] arquitetura: {arquitetura}

______________________________________________
[0] sair                 | [1] libreoffice
[2] onlyoffice           | [7] cohesion
[3] gimp & photogimp     | [8] audacity
[4] wps                  | [9] darktable
[5] anydesk              | [10] foliate
[6] daVinci resolve      | [11] inkscape
[12] freecad             | [13] kicad
[14] kdenlive            | [15] figma
[16] obsidian            | [17] pinta
[18] Logseq              | [19] Standard Notes
[20] Cryptomator         | [21] FreeMind 
[22] Zettlr              | [23] CopyQ
==============================================
""")

try:
    select = int(input("Digite o numero da opção escolhida de 1/23: "))
    if select in apps:
       os.system("clear")
       subprocess.run(["yay", "-S", "--needed", "--noconfirm", apps[select]])
       reiniciar()

    elif select == 0:
       os.system("clear")
       os.system("python postnext.py")

    else:
       print("Não temos essa opção")
       time.sleep(2)
       reiniciar()

except ValueError:
    print("opção errada...")
    reiniciar()

print("Boa escolha para seu workspace!")




if select in apps:
    os.system("clear")
    subprocess.run(["yay", "-S", "--needed", "--noconfirm", apps[select]])
    reiniciar()

elif select == 0:
    os.system("clear")
    os.system("python postnext.py")

else:
    print("Não temos essa opção")
    time.sleep(2)
    reiniciar()



