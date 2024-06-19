# Airbnb

## Guía

### 1. Crear y activar entorno virtual

```sh
python -m venv venv

# linux
source venv/bin/activate

# windows
.\venv\Scripts\activate
```

### 2. Instalar dependencias

```sh
pip install -r requirements.txt
```

### 3. Crear en la raíz del proyecto un `.env` y completar los siguientes datos:

```
DB_NAME=
DB_PORT=
DB_HOST=
DB_USER=
DB_PASSWORD=
```

### 4. Dirigirse al directorio `project`

```sh
cd project
```

### 5. Hacer las migraciones en nuestra base de datos

```sh
python manage.py migrate
```

### 6. Levantar servidor con django

```sh
python manage.py runserver
```

### 7. Ingresar a la url `127.0.0.1:8000` o `localhost:8000`
