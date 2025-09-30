# Chasky
Chasky es una herramienta de ciberseguridad enfocada en la detección temprana de correos electrónicos sospechosos. Utiliza algoritmos de análisis para diferenciar entre spam, fraudes y ataques de phishing, proporcionando alertas al usuario para reforzar la protección frente a amenazas digitales.

Requerimientos:
-SO: Windows, macOS o Linux
-Editor de codigo: Recomiendo Visual Studio Code(VSCode)
-Python 3.11: el contenedor usa python:3.11-slim,asi que instala esta version en tu local.
verificas la instalacion: python --version o python3 --version
#se devera ver algo como Python 3.11.x
-Instala pip(si no viene incluido): pip --version o pip3 --version
#si no viene incluido:
python -m ensurepip --upgrade
python -m pip install --upgrade pip

-Dependencias de Python
#El Dockerfile del contenedor incluye nltk,spacy,scikit-learn,transformers y streamlit
pip install nltk spacy scikit-learn trasnformers streamlit

-Entorno Virtual(Opcional pero Recomendado)
1)Crea el entorno:
python -m venv chasky_env
2)Activalo:
Windows: chasky_env\Scripts\activate
macOS/Linux: source chasky_env/bin/activate
3)Instala Dependencias Dentro:
pip install nltk spacy scikit-learn trasnformers streamlit
Nota: veras (chasky_env) al inicio de tu prompt, indicando que estas en el entorno.
4)Archivos del Proyecto
por el momento debes entrar al vm del proyecto y hacer cat a chasky.py y dashboard.py y copiarlos localmente
5)Avanza codigo del proyecto y subelo a este repositorio usando git, si todo anda bien hare el merge, buena suerte!

3
