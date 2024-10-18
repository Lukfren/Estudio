import os
import os.path
import pickle

class Gobierno:
    def __init__(self):
        self.aportes = ""

class Comercios:
    def __init__(self):
        self.qr = ""
        self.lepagaron = 0.0

class Clientes:
    def __init__(self):
        self.dni = ""
        self.saldo = 0.0
        self.pago = 0.0
        self.recupero = 0.0
        self.mes = 0
        self.estado = "S"

def programa_principal():
    abrir_archivos()
    menu()
    cerrar_archivos()

def abrir_archivos():
    global arFiGob, arLoGob, arFiCom, arLoCom, arFiCli, arLoCli
    arFiGob = "registroGob.dat"
    arFiCom = "registroCom.dat"
    arFiCli = "registroCli.dat"

    if os.path.exists(arFiGob):
        arLoGob = open(arFiGob, "r+b")
    else:
        print(f"El archivo {arFiGob} se creo")
        arLoGob = open(arFiGob, "w+b")
    if os.path.exists(arFiCom):
        arLoCom = open(arFiCom, "r+b")
    else:
        print(f"El archivo {arFiCom} se creo")
        arLoCom = open(arFiCom, "w+b")
    if os.path.exists(arFiCli):
        arLoCli = open(arFiCli, "r+b")
    else:
        print(f"El archivo {arFiCli} se creo")
        arLoCli = open(arFiCli, "w+b")

def cerrar_archivos():
    global arFiGob, arLoGob, arFiCom, arLoCom, arFiCli, arLoCli
    arLoGob.close()
    arLoCom.close()
    arLoCli.close()
    
def menu():
    print("Menu")
    print("1. Alta comercios")
    print("2. Alta clientes")
    print("3. Actualizar billetera")
    print("4. Comprar")
    print("5. Informe gobierno")
    print("6. Fin del programa")
    opc = int(input("Ingrese su opción: "))
    while opc != 6:
        match opc:
            case 1:
                alta_comercios()
            case 2:
                alta_clientes()
            case 3:
                actualizar_billetera()
            case 4:
                comprar()
            case 5:
                informe_gobierno()
        print("Menu")
        print("1. Alta comercios")
        print("2. Alta clientes")
        print("3. Actualizar billetera")
        print("4. Comprar")
        print("5. Informe gobierno")
        print("6. Fin del programa")
        opc = int(input("Ingrese su opción: "))

def alta_comercios():
    global arFiCom,arLoCom
    com = Comercios()
    os.system("cls")
    qr = str(input("Ingresar comercio:"))
    val = ver_comercio(qr)
    if val != -1:
        com.qr = qr
        print("Comercio añadido")
    else:
        print("Comercio repetido")

    print("")

def ver_comercio(par):
    global arFiCom, arLoCom
    com = Comercios()
    arLoCom.seek(0.0)
    com = pickle.load(arLoCom)
    tamreg = arLoCom.tell()
    tamarc = os.path.getsize(arFiCom)
    cantreg = tamarc//tamreg
    pri = 0
    ult = cantreg
    med = (pri+ult)//2
    arLoCom.seek(med*tamreg, 0)
    pos = arLoCom.tell()
    com = pickle.load(arLoCom)
    while com.qr != par and pri<ult:
        if com.qr > par:
            ult = med -1
        else:
            pri = med + 1
        mid = (pri+ult)//2
        arLoCom.seek(med*tamreg, 0)
        pos = arLoCom.tell()
        com = pickle.load(arLoCom)
    if com.qr == par:
        return -1
    else:
        return pos
    
def alta_clientes():
    print("")
def actualizar_billetera():
    print("")
def comprar():
    print("")

def informe_gobierno():
    print("")























programa_principal()