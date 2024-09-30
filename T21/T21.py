import requests
import json
import logging
import getpass
import msvcrt
import os
import re
import six
import argparse

# Configuración de logging para errores
logging.basicConfig(filename='hibpERROR.log', format="%(asctime)s %(levelname)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.ERROR)

def PyValidation():
    try:
        if six.PY3:
            print("En efecto, es PYTHON3 :)")
            print("Presiona cualquier tecla para continuar...")
            msvcrt.getch()
            os.system('cls')
    except OSError as e:
        msg = f"Error: {e}"
        print(msg)
        logging.error(msg)
        print("Presiona cualquier tecla para continuar...")
        msvcrt.getch()
        os.system('cls')
        

# Verificar formato de correo
def Mailvalidation(email):
    patron = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(patron, email) is not None

parser = argparse.ArgumentParser(description='Verificar si un correo electrónico ha sido comprometido.')
parser.add_argument('email', type=str, help='Correo electrónico a investigar')
args = parser.parse_args()

PyValidation()

# Ingresar de forma "segura" ola apikey
while True:
    key = getpass.getpass('Ingrese la Api Key: ')
    key1 = 'ec1e2ebed1754f1b8c00f2b90aa15906'  # 'ec1e2ebed1754f1b8c00f2b90aa15906'

    if key == key1:
        print('Apikey ingresada correctamente\n')
        print("Presiona cualquier tecla para continuar...")
        msvcrt.getch()
        os.system('cls')
        break
    else:
        print("Apikey incorrecta, intente de nuevo\n")
        print("Presiona cualquier tecla para continuar...")
        msvcrt.getch()
        os.system('cls')

headers = {}
headers['content-type']= 'application/json'
headers['api-version']= '3'
headers['User-Agent']='python'

#Place that API key here
headers['hibp-api-key']=key

while True:
    email = args.email #'falso@hotmail.com'
    if Mailvalidation(email):
        break
    else:
        print("No ingreso un email valido\n")
        print("Presiona cualquier tecla para continuar...")
        msvcrt.getch()
        os.system('cls')

# Solicitud 
url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()  
    data = r.json()
    encontrados = len(data)
    if encontrados > 0:
        print(f"Los sitios en los que se ha filtrado el correo {email} son:")
        for filtracion in data:
            print(filtracion["Name"])
        msg = f"{email} Filtraciones encontradas: {encontrados}"
    else:
        msg = f"El correo {email} no ha sido filtrado"
    print(msg)
except requests.exceptions.RequestException as e:
    msg = f"Error: {e}"
    print(msg)
    logging.error(msg)
except json.JSONDecodeError as e:
    msg = f"Error: {e}"
    print(msg)
    logging.error(msg)
except Exception as e:
    msg = f"Error: {e}"
    print(msg)
    logging.error(msg)
