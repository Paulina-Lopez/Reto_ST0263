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

### Detalles de Desarrollo y Técnicos
- MongoDB se utiliza para almacenar la información de los usuarios y los archivos compartidos.
- Las direcciones IP y los puertos están configurados para ejecutarse localmente por defecto.

### Resultados o pantallazos
![postman](URL "https://i.postimg.cc/W3L7HS9L/image.png")

## 4. Ambiente de ejecución

### IP o Nombres de Dominio
- IP del servidor Flask: 127.0.0.1:5000
- IP del servidor gRPC: [::]:4999

### Guía de Usuario
- Los usuarios pueden registrarse, iniciar y cerrar sesión mediante el servidor Flask.
- Los archivos se pueden cargar y descargar usando el cliente y servidor gRPC.

## 5. Información Adicional

## Referencias
- https://grpc.io/docs/languages/python/basics/
- https://devjaime.medium.com/microservicios-de-python-con-grpc-3ff25126b6eb
- https://flask-es.readthedocs.io/