from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Sofía English Adventure - Dandy's World",
    description="Sitio de práctica interactivo de Inglés para 3° grado (hurlingham.xyz)",
    version="1.0.0",
)

# Mount static files
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Templates
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Página principal interactiva con Dandy's World."""
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
async def health():
    """Health check para proxies inversos y monitoreo."""
    return {"status": "ok", "app": "sofi_english", "domain": "english.hurlingham.xyz"}


@app.get("/pdf")
async def download_pdf():
    """Descarga o visualización directa del PDF de 15 páginas."""
    pdf_path = BASE_DIR / "static" / "Repaso_Ingles_Sofia_3er_Grado.pdf"
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="Repaso_Ingles_Sofia_3er_Grado.pdf",
    )
