# ST0263 - Topicos especiales en telemática

## Estudiante
- Maria Paulina López Salazar
- Email: mplopezs@eafit.edu.co

## Profesor
- Alvaro Enrique Ospina Sanjuan
- Email: aeospinas@eafit.edu.co

# Reto N° 1 y 2
## 1. Descripción de la actividad
Este proyecto es una implementación de una red peer-to-peer (P2P) para compartir archivos. Utiliza Flask para el servidor principal y gRPC para la comunicación entre peers.

### 1.1. Requerimientos cumplidos
- Implementación del servidor principal usando Flask.
- Gestión de usuarios (login/logout) y archivos (indexación y búsqueda).
- Implementación del servidor y cliente gRPC para la carga y descarga de archivos.

## 2. Diseño e información general
El proyecto sigue una arquitectura P2P donde los usuarios pueden compartir archivos entre ellos. La información del usuario y los archivos compartidos se gestiona a través de un servidor central implementado en Flask. La transferencia de archivos se realiza mediante gRPC.

<img src="https://i.postimg.cc/W4Hf5MZ0/telematica-drawio.png">

## 3. Ambiente de desarrollo
- Lenguaje de Programación: Python
- Librerías:  Flask, pymongo, grpc, concurrent.futures
- MongoDB para la gestión de datos

### Cómo compilar y ejecutar

Para generar los archivos gRP, deberá ejecutar:
py -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. records.proto

Para ejecutar el servidor principal (server.py), se debe asegurar que MongoDB esté corriendo y luego en una terminal ejecutar:
py server.py

Para el servidor gRPC (p_server.py) deberá ejecutar lo siguiente en otra terminal independiente:
py p_server.py

Finalmente para el cliente (p_client.py), recuerde utilizar otra terminal y ejecute:
py p_client.py

### Detalles de desarrollo y técnicos
- MongoDB se utiliza para almacenar la información de los usuarios y los archivos compartidos.
- Las direcciones IP y los puertos están configurados para ejecutarse localmente por defecto.

### Resultados o pantallazos
- Proceso de registro de un peer nuevo a la base de datos
<img src="https://i.postimg.cc/W3L7HS9L/image.png">

- Proceso de login de un peer existente en la base de datos
Caso de éxito:
<img src="https://i.postimg.cc/FHwqhyPG/image.png">
Caso fallido:
<img src="https://i.postimg.cc/CMJQRTPR/image.png">

- Proceso de registro de los archivos de un peer en el servidor
Caso de éxito:
<img src="https://i.postimg.cc/76ZSccgR/image.png">
Caso fallido:
<img src="https://i.postimg.cc/15qwLDqy/image.png">

- Proceso de buscar los archivos en los peers almacenados en el servidor
Caso de éxito:
<img src="https://i.postimg.cc/pTS5SdV9/image.png">
Caso fallido:
<img src="https://i.postimg.cc/gcfNXzyk/image.png">

- Proceso de logout
Caso de éxito:
<img src="https://i.postimg.cc/wv1QMZ7m/image.png">
Caso fallido:
<img src="https://i.postimg.cc/vT97Ln78/image.png">

- Proceso de carga de archivos entre peers
<img src="https://i.postimg.cc/d3KZFxdv/image.png">

- Proceso de descarga de archivos entre peers
<img src="https://i.postimg.cc/BnNzKWQY/image.png">

## 4. Ambiente de ejecución
### IP o nombres de dominio
- IP del servidor Flask: 127.0.0.1:5000
- IP del servidor gRPC: [::]:4999

### Guía de Usuario
- Los usuarios pueden registrarse, iniciar y cerrar sesión mediante el servidor Flask.
- Los archivos se pueden cargar y descargar usando el cliente y servidor gRPC.

1. Login (/clogin):
Método: POST
Datos requeridos: username, password y url únicamente para el registro.
Función: Autentica al usuario. Envía una petición POST con los datos de login a un servicio específico.

2. Logout (/clogout):
Método: POST
Datos requeridos: username.
Función: Cierra la sesión del usuario. Envía una petición POST con el nombre de usuario a un servicio de logout.

3. Indexar (/cindex):
Método: POST
Datos requeridos: username, files.
Función: Procesa una lista de archivos para indexarlos. Cada archivo se sube a través de un cliente gRPC.

5. Buscar (/csearch):
Método: POST
Datos requeridos: files.
Función: Busca archivos específicos. Por cada archivo, realiza una operación de descarga usando gRPC.
Funciones gRPC:

6. Métodos gRPC:
grpc_client_upload(filename): Sube archivos utilizando gRPC.
grpc_client_download(filename): Descarga archivos utilizando gRPC.

## Referencias
- https://grpc.io/docs/languages/python/basics/
- https://devjaime.medium.com/microservicios-de-python-con-grpc-3ff25126b6eb
- https://flask-es.readthedocs.io/