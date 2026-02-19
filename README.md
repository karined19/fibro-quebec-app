# Bottin Québec | Fibromyalgie, douleur chronique, proches aidants

Application Streamlit (Python 3.11+) : bottin centralisé de ressources (Québec + certaines ressources Canada).

> Outil d’orientation uniquement. Aucune information médicale personnalisée.

## Structure

- `app.py` : application Streamlit
- `data/resources.json` : données locales (JSON)
- `utils/` : validation, recherche, recommandations, export

## Installation (local)

Pré-requis: Python 3.11+

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
