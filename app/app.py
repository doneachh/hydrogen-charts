import streamlit as st
from utils.i18n import translate, SUPPORTED_LANGS

LANG_FLAGS = {"en": "🇬🇧", "de": "🇩🇪"}

def render_language_selector():
    lang = st.radio(
        "lang",
        options=list(LANG_FLAGS.keys()),
        format_func=lambda x: LANG_FLAGS[x],
        horizontal=True,
        label_visibility="collapsed",
        key="lang"
    )
    return lang

render_language_selector()


exec(open("app/0-home.py").read())
st.divider()

exec(open("app/1-graphical_analysis.py").read())
st.divider()

exec(open("app/2-timeline-development.py").read())
st.divider()

exec(open("app/3-technology.py").read())
st.divider()

exec(open("app/faq.py").read())
