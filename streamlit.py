import streamlit as st
import pandas as pd
import numpy as np

app = StreamlitJupyter()

with app.run():
    st.title("Notebook İçinde Streamlit 🎯")
    st.write("Bu dashboard doğrudan hücrede çalışıyor!")

    df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
    st.line_chart(df)
