# 📧 Chasky

**Chasky** es una herramienta de ciberseguridad enfocada en la **detección temprana de correos electrónicos sospechosos**.  
Utiliza algoritmos de análisis para diferenciar entre **spam, fraudes y ataques de phishing**, proporcionando alertas al usuario para reforzar la protección frente a amenazas digitales.

---

## ⚙️ Requerimientos

- SO compatible: Windows, macOS o Linux  
- Editor de código recomendado: Visual Studio Code (VSCode)  
- Python 3.11  
  - El contenedor usa python:3.11-slim, por lo que se recomienda instalar esta versión localmente.  
  - Verificar instalación:  
    python --version  
    o  
    python3 --version  
    Deberías ver algo como: Python 3.11.x  

- Pip (si no viene incluido):  
    pip --version  
    o  
    pip3 --version  
    Si no está instalado:  
    python -m ensurepip --upgrade  
    python -m pip install --upgrade pip  

---

## 📦 Dependencias de Python

El Dockerfile del contenedor incluye:  
- nltk  
- spacy  
- scikit-learn  
- transformers  
- streamlit  

Instálalas manualmente si trabajas en local:  

    pip install nltk spacy scikit-learn transformers streamlit

---

## 🐍 Entorno Virtual (Opcional pero Recomendado)

1. Crear el entorno:  
    python -m venv chasky_env  

2. Activarlo:  
   - Windows:  
     chasky_env\Scripts\activate  
   - macOS/Linux:  
     source chasky_env/bin/activate  

3. Instalar dependencias dentro del entorno:  
    pip install nltk spacy scikit-learn transformers streamlit  

   Verás (chasky_env) al inicio de tu prompt, indicando que estás en el entorno.

---

## 📂 Archivos del Proyecto

1. Entra a la VM del proyecto.  
2. Visualiza el contenido con:  
    cat chasky.py  
    cat dashboard.py  
3. Copia los archivos localmente.  
4. Avanza el código del proyecto y súbelo a este repositorio usando git.  

---
## ✅ Nota final
Si todo anda bien, se hará el merge.  
¡Buena suerte con el desarrollo! 🚀
