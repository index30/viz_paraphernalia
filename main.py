import streamlit as st
from config.const import PageId
from config.session import SessionManager
from templates.base_template import BaseTemplate
from templates.public.home import HomePage
from apps.route import Route


def init_session() -> SessionManager:
    ssm = SessionManager(
    )
    return ssm

def init_pages(ssm: SessionManager) -> list[BaseTemplate]:
    pages = [
        HomePage(page_id=PageId.HOME, title="Home", ssm=ssm)
    ]
    return pages

def init_app(ssm: SessionManager, pages: list[BaseTemplate]) -> Route:
    app = Route(ssm, pages)
    return app

if __name__ == '__main__':
    if not st.session_state.get("init_flg", False):
        ssm = init_session()
        pages = init_pages(ssm)
        app = init_app(ssm, pages)
        st.session_state["init_flg"] = True
        st.session_state["app"] = app
        st.set_page_config(page_title="viz_paraphernalia", layout="wide")

    app = st.session_state.get("app", None)
    if app is not None:
        app.render()