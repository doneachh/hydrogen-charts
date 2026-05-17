import json
import streamlit as st
from pathlib import Path
from functools import lru_cache

SUPPORTED_LANGS = {"en": "English", "de": "Deutsch"}
DEFAULT_LANG = "en"

@lru_cache(maxsize=None)          # Cache files — don't re-read on every rerun
def load_translations(lang: str) -> dict:
    path = Path(f"app/locales/{lang}.json")
    if not path.exists():
        path = Path(f"app/locales/{DEFAULT_LANG}.json")
    return json.loads(path.read_text(encoding="utf-8"))

def tr(key: str) -> str:
    """Translate a dot-notation key, e.g. t('blog.read_more')"""
    lang = st.session_state.get("lang", DEFAULT_LANG)
    translations = load_translations(lang)
    
    # Dot-notation traversal
    keys = key.split(".")
    value = translations
    for k in keys:
        value = value.get(k, key)   # Fallback to key itself if missing
        if not isinstance(value, dict):
            break
    return value if isinstance(value, str) else key
