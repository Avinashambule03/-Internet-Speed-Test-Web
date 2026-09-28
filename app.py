import streamlit as st
import speedtest
import time

st.set_page_config(
    page_title="Internet Speed Test",
    page_icon="⚡",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #000000, #16213e, #533483);
        color: white;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #00BFFF;
        margin-top: 30px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: white;
        margin-bottom: 30px;
    }

    .result {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">⚡ Internet Speed Test ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Test your internet connection speed</div>',
    unsafe_allow_html=True
)

if "tested" not in st.session_state:
    st.session_state.tested = False

if st.button("🚀 Start Test", use_container_width=True):

    st.session_state.tested = False

    status = st.empty()
    progress = st.progress(0)

    try:
        status.info("🔍 Finding the best server...")
        progress.progress(20)

        st_obj = speedtest.Speedtest()

        status.info("⬇️ Testing download speed...")
        progress.progress(45)

        download = st_obj.download() / 1_000_000

        status.info("⬆️ Testing upload speed...")
        progress.progress(75)

        upload = st_obj.upload() / 1_000_000

        progress.progress(100)

        status.success("✅ Test Completed Successfully!")

        st.markdown(
            f'<div class="result">⬇️ Download: {download:.2f} Mbps</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="result">⬆️ Upload: {upload:.2f} Mbps</div>',
            unsafe_allow_html=True
        )

        st.session_state.tested = True

    except Exception as e:
        status.error(f"❌ Test failed: {e}")