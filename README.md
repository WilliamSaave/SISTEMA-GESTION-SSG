# Asesoría Integral - Sistema de Gestión SSG

Primera versión funcional del sitio web público desarrollado en Python + Flask.

## Qué incluye

- Página pública responsive.
- Inicio, servicios, metodología, casos reales, sectores, normatividad y contacto.
- Servicios ampliados mediante ventanas modales.
- Formulario de solicitud de asesoría.
- Registro local de solicitudes en SQLite.
- Página base para futuro Portal de Clientes.
- Diseño adaptable a escritorio, tablet y celular.
- No se muestran precios.

## Servicios incluidos

- Seguridad y Salud en el Trabajo (SG-SST)
- Buenas Prácticas de Manufactura (BPM)
- Planes de saneamiento
- Gestión ambiental y sanitaria
- Capacitación
- Auditorías y cumplimiento

## Casos reales incluidos

- Empresa con sistema SG-SST y saneamiento: mantenimiento SG-SST y plan de saneamiento.
- Empresa de empaque y distribución de alimentos frescos: implementación por fases de BPM.
- Establecimiento del sector gastronómico: plan de saneamiento y plan de emergencias.
- Empresa del sector de alimentos: plan de capacitación en manipulación higiénica de alimentos.

Por confidencialidad, los casos se muestran sin nombres de clientes ni precios, con enfoque exclusivo en el alcance y las actividades ejecutadas.

## Imagen principal

El sitio incluye `static/img/hero-induccion-restaurante.svg`, una ilustración de una inducción a personal de restaurante relacionada con SG-SST, BPM, inocuidad y cumplimiento.

## Instalación local

1. Tener Python 3.10 o superior.
2. Crear un entorno virtual.
3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar:

```bash
python app.py
```

5. Abrir `http://127.0.0.1:5000`.

## Base de datos

Al iniciar la aplicación se crea `data/solicitudes.db`. La tabla `solicitudes` almacena los formularios enviados desde la página.

## Estructura

```text
app.py
render.yaml
requirements.txt
templates/
  index.html
  portal.html
static/
  css/style.css
  js/main.js
  img/hero-induccion-restaurante.svg
data/
```

## Publicación en Render

El proyecto ya incluye `render.yaml` y Gunicorn.

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

> Nota: SQLite sirve para la demostración inicial. Para producción y conservación permanente de solicitudes se recomienda migrar a PostgreSQL.

## Próxima fase

El botón **Portal clientes** ya tiene una ruta `/portal`. Desde ahí se puede continuar con autenticación, empresas, usuarios y roles, proyectos, actividades, documentos, evidencias, hallazgos, planes de acción, indicadores y notificaciones.
