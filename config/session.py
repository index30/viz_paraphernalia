import streamlit as st

class SessionManager:
    def __init__(
        self
    ) -> None:
        self._session_state = st.session_state