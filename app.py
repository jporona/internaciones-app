from flask import Flask, render_template, request, redirect, url_for
from flask_caching import Cache
import requests

app = Flask(__name__)
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 300  # 5 minutos

cache = Cache(app)

API_URL = "http://10.0.0.71:60000/api/smc/internaciones"
POR_PAGINA = 20


@cache.cached(timeout=300, key_prefix="internaciones")
def obtener_internaciones():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


@app.route("/")
def index():
    try:
        internaciones = obtener_internaciones()
        error = None
    except requests.RequestException as e:
        internaciones = []
        error = str(e)

    total = len(internaciones)
    pagina = request.args.get("pagina", 1, type=int)
    total_paginas = max(1, (total + POR_PAGINA - 1) // POR_PAGINA)
    pagina = max(1, min(pagina, total_paginas))

    inicio = (pagina - 1) * POR_PAGINA
    fin = inicio + POR_PAGINA
    pagina_items = internaciones[inicio:fin]

    return render_template(
        "index.html",
        internaciones=pagina_items,
        total=total,
        pagina=pagina,
        total_paginas=total_paginas,
        por_pagina=POR_PAGINA,
        error=error,
    )


@app.route("/cache/limpiar")
def limpiar_cache():
    cache.delete("internaciones")
    if request.args.get("redirect"):
        return redirect(url_for("index"))
    return {"mensaje": "Cache limpiado. La próxima consulta obtendrá datos frescos."}, 200


if __name__ == "__main__":
    app.run(debug=True)
