## API con Flask y JWT

Esta es una API básica implementada en Flask que utiliza JWT (JSON Web Tokens) para la autenticación de usuarios. La API proporciona rutas para iniciar sesión y acceder a una ruta protegida.

## Características
Inicio de sesión de usuarios con generación de tokens JWT.
Ruta protegida que requiere autenticación mediante token JWT

## Requisitos
Asegúrate de tener instalado lo siguiente:

* Python 3.x
* Pip (administrador de paquetes de Python)

## Instalación 

* Clona este repositorio en tu máquina local o descarga el archivo ZIP

* Crea un entorno virtual (opcional pero se recomienda):

~ python -m venv env

* Activa el entorno virtual:

~ env\Scripts\activate

* Instala las dependencias:

~ pip install -r requirements.txt

## Configuración

Agrega las credenciales de la base de datos en la carpeta static en archivo env static/.env
Ejecuta el script sql en tu base de datos para poder guardar datos sql/init.sql

## Uso

~ python -m app.main

## pruebas

Desde la raiz utilizamos el siguiente comando para correr la pruebas

python -m unittest tests.test_main








