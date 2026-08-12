from flask import Flask, render_template, request, jsonify
from pathlib import Path
import sqlite3
from datetime import datetime

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "solicitudes.db"

SERVICIOS = [
    {
        "id": "sst",
        "icon": "shield",
        "titulo": "Seguridad y Salud en el Trabajo",
        "resumen": "Implementación, mantenimiento y seguimiento del SG-SST de acuerdo con las necesidades de la organización.",
        "destacados": [
            "Diagnóstico y evaluación inicial",
            "Plan anual de trabajo",
            "Políticas, procedimientos, instructivos y registros",
            "Matrices de peligros y requisitos legales",
            "COPASST, Comité de Convivencia y brigada",
            "Plan de emergencias",
            "Capacitación e inspecciones",
            "Planes de mejora",
            "Preparación para auditorías y visitas"
        ]
    },
    {
        "id": "bpm",
        "icon": "food",
        "titulo": "Inocuidad y Buenas Prácticas de Manufactura",
        "resumen": "Diseño e implementación de programas BPM para establecimientos y empresas relacionadas con alimentos.",
        "destacados": [
            "Limpieza y desinfección",
            "Control integrado de plagas",
            "Manejo de residuos",
            "Abastecimiento y control de agua potable",
            "Manejo de productos químicos",
            "Mantenimiento y calibración",
            "Recepción y almacenamiento",
            "Producción, distribución y transporte",
            "Trazabilidad",
            "Muestreo y análisis",
            "Auditorías internas",
            "Quejas, reclamos y retiro de producto",
            "Control de proveedores"
        ]
    },
    {
        "id": "saneamiento",
        "icon": "clean",
        "titulo": "Planes de Saneamiento",
        "resumen": "Estructuración de programas y formatos para sostener condiciones sanitarias adecuadas y trazables.",
        "destacados": [
            "Programa de limpieza y desinfección",
            "POES",
            "Programa de control de plagas",
            "Residuos sólidos y líquidos",
            "Control de agua potable",
            "Formatos de seguimiento",
            "Capacitación para implementación",
            "Actualización frente a hallazgos de visitas"
        ]
    },
    {
        "id": "ambiental",
        "icon": "leaf",
        "titulo": "Gestión Ambiental y Sanitaria",
        "resumen": "Acompañamiento para entidades de salud y otras organizaciones que requieren control ambiental, sanitario y documental.",
        "destacados": [
            "PGIRASA",
            "Gestión de residuos peligrosos - RESPEL",
            "Residuos especiales y posconsumo",
            "Sustancias y productos químicos",
            "Limpieza, desinfección y control de plagas",
            "Agua, vertimientos y saneamiento ambiental",
            "Matriz de requisitos legales",
            "Inspecciones y seguimiento ambiental",
            "Preparación para visitas de inspección"
        ]
    },
    {
        "id": "capacitacion",
        "icon": "training",
        "titulo": "Capacitación",
        "resumen": "Programas de formación ajustados a la operación, los riesgos y los requisitos aplicables.",
        "destacados": [
            "Manipulación higiénica de alimentos",
            "Buenas Prácticas de Manufactura",
            "Manejo y segregación de residuos",
            "PGIRASA",
            "Código de colores",
            "Manejo de sustancias químicas",
            "Sistema Globalmente Armonizado",
            "Interpretación de FDS",
            "Prevención y atención de derrames",
            "Preparación para auditorías"
        ]
    },
    {
        "id": "auditorias",
        "icon": "audit",
        "titulo": "Auditorías y Cumplimiento",
        "resumen": "Revisión técnica y documental para identificar brechas, priorizar riesgos y preparar a la organización.",
        "destacados": [
            "Diagnóstico inicial",
            "Auditoría documental",
            "Inspección en campo",
            "Verificación de cumplimiento",
            "Identificación y clasificación de hallazgos",
            "Planes de acción",
            "Seguimiento a acciones correctivas",
            "Preparación para autoridades, ARL y auditorías"
        ]
    }
]

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS solicitudes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                empresa TEXT,
                email TEXT NOT NULL,
                telefono TEXT,
                servicio TEXT,
                sector TEXT,
                necesidad TEXT NOT NULL,
                creado_en TEXT NOT NULL
            )
        """)
        conn.commit()

@app.route("/")
def index():
    return render_template("index.html", servicios=SERVICIOS)

@app.route("/api/solicitudes", methods=["POST"])
def crear_solicitud():
    data = request.get_json(silent=True) or request.form

    nombre = (data.get("nombre") or "").strip()
    empresa = (data.get("empresa") or "").strip()
    email = (data.get("email") or "").strip()
    telefono = (data.get("telefono") or "").strip()
    servicio = (data.get("servicio") or "").strip()
    sector = (data.get("sector") or "").strip()
    necesidad = (data.get("necesidad") or "").strip()

    if not nombre or not email or not necesidad:
        return jsonify({
            "ok": False,
            "mensaje": "Completa nombre, correo y descripción de la necesidad."
        }), 400

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO solicitudes
            (nombre, empresa, email, telefono, servicio, sector, necesidad, creado_en)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (nombre, empresa, email, telefono, servicio, sector, necesidad, datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()

    return jsonify({
        "ok": True,
        "mensaje": "Tu solicitud fue registrada correctamente. Nos pondremos en contacto contigo."
    })

@app.route("/portal")
def portal():
    return render_template("portal.html")

# Inicializa la base local también cuando la aplicación se ejecuta con Gunicorn.
init_db()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
