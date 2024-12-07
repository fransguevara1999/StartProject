# StartProject

StartProject es una aplicación diseñada para automatizar la creación de estructuras de proyectos. Esta herramienta utiliza Flask para exponer un servicio REST que permite generar estructuras personalizadas y multiplataforma de manera rápida y eficiente.

## **Características**
- Genera estructuras predeterminadas o personalizadas.
- Multiplataforma (Windows, MacOS y Linux).
- Extensible para integrarse con herramientas y flujos de trabajo.

## **Requisitos**
1. Python 3.7 o superior.
2. Dependencias en `requirements.txt`.

## **Cómo ejecutar**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/fransguevara1999/StartProject.git
   cd StartProject


# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate

# Activar el entorno virtual (Linux/Mac)
source venv/bin/activate


pip install -r requirements.txt


python project_service.py


URL: http://127.0.0.1:5000/create_project
Método: POST
Cuerpo (Body):
json
Copiar código


Body:
{
    "path": "C:/ruta/del/proyecto",
    "structure": {
        "data": ["raw", "processed"],
        "notebooks": ["exploracion.ipynb"],
        "src": ["__init__.py", "main.py"]
    }
}

CURL:
curl -X POST http://127.0.0.1:5000/create_project \
-H "Content-Type: application/json" \
-d '{
    "path": "C:/ruta/del/proyecto",
    "structure": {
        "data": ["raw", "processed"],
        "notebooks": ["exploracion.ipynb"],
        "src": ["__init__.py", "main.py"]
    }
}'


Estructura Predeterminada :
mi_proyecto/
│
├── data/                   # Datos brutos y procesados
│   ├── raw/                # Datos sin procesar
│   ├── processed/          # Datos procesados
│
├── notebooks/              # Notebooks Jupyter para experimentación
│   └── exploracion.ipynb   # Notebook de exploración de datos
│
├── src/                    # Código fuente
│   ├── __init__.py         # Hace que `src` sea un paquete
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_serving.py
│   └── utils.py
│
├── tests/                  # Pruebas automáticas
│   └── test_model.py       # Pruebas del modelo
│
├── models/                 # Modelos entrenados
│   └── modelo_final.h5     # Modelo guardado
│
├── outputs/                # Resultados y gráficas
│   ├── figures/            # Gráficas generadas
│   └── logs/               # Logs de entrenamiento
│
├── .gitignore              # Archivos/carpetas a ignorar por Git
├── environment.yml         # Archivo de entorno para Anaconda
├── README.md               # Descripción del proyecto
└── requirements.txt        # Dependencias del proyecto


