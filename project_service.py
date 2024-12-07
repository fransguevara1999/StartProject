from flask import Flask, request, jsonify, abort
from pathlib import Path
import os

app = Flask(__name__)

# Estructura predeterminada del proyecto
default_project_structure = {
    "data": ["raw", "processed"],
    "notebooks": ["exploracion.ipynb"],
    "src": ["__init__.py", "data_preprocessing.py", "model_training.py", "model_serving.py", "utils.py"],
    "tests": ["test_model.py"],
    "models": ["modelo_final.h5"],
    "outputs": ["figures", "logs"],
    ".gitignore": None,
    "environment.yml": None,
    "README.md": None,
    "requirements.txt": None,
}

def validate_path(base_dir):
    """Validar que la ruta base sea válida y accesible."""
    base_path = Path(base_dir)
    if not base_path.exists():
        abort(400, f"La ruta '{base_dir}' no existe.")
    if not os.access(base_dir, os.W_OK):
        abort(400, f"No se tienen permisos de escritura en la ruta '{base_dir}'.")

def create_project_structure(base_dir, structure):
    """Crear la estructura del proyecto."""
    base_path = Path(base_dir)
    base_path.mkdir(parents=True, exist_ok=True)

    for folder, contents in structure.items():
        folder_path = base_path / folder

        # Si es una carpeta (y tiene subcarpetas o archivos)
        if isinstance(contents, list):
            folder_path.mkdir(parents=True, exist_ok=True)

            for item in contents:
                item_path = folder_path / item
                item_path.touch()

        # Si es un archivo en la raíz del proyecto
        elif contents is None:
            file_path = base_path / folder
            file_path.touch()

@app.route("/create_project", methods=["POST"])
def create_project():
    """Endpoint para crear la estructura del proyecto."""
    data = request.json
    base_dir = data.get("path")
    custom_structure = data.get("structure", default_project_structure)

    if not base_dir:
        return jsonify({"error": "La ruta 'path' es obligatoria."}), 400

    try:
        validate_path(base_dir)
        create_project_structure(base_dir, custom_structure)
        return jsonify({"message": f"Estructura del proyecto creada exitosamente en {base_dir}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
