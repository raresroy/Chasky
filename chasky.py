import json

# Simulación de análisis
data = {"correos": [{"id": 1, "categoria": "spam"}, {"id": 2, "categoria": "legítimo"}]}

# Guarda datos para el dashboard
with open("resumen.json", "w") as f:
    json.dump(data, f)

print("Análisis de Chasky completado. Datos guardados.")