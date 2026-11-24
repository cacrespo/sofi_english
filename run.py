#!/usr/bin/env python3
"""Script de inicio local para sofi_english."""

import uvicorn

if __name__ == "__main__":
    print("Iniciando Dandy's World English Review...")
    print("Abrí tu navegador en: http://localhost:8000")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
