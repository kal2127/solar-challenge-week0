import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Page Setup ----------------
st.set_page_config(page_title="Solar Energy Dashboard", layout="wide")

# ---------------- Custom CSS for Styling ----------------
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .header-bar {
            background: linear-gradient(90deg, #facc15, #fde68a);
            color: #1f2937;
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
            margin-bottom: 1.2rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        .file-header {
            background: #fef9c3;
            padding: 0.8rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            text-align: center;
            font-weight: 600;
            color: #1e3a8a;
            font-size: 20px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: gray;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown('<div class="header-bar"><h1>Solar Data Discovery</h1></div>', unsafe_allow_html=True)


# ---------------- File Upload ----------------
st.sidebar.header("📤 Upload Data Files")
uploaded_files = st.sidebar.file_uploader("Upload your CSV files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        filename = uploaded_file.name

        # File Header
        st.markdown(f'<div class="file-header">📁 {filename}</div>', unsafe_allow_html=True)

        # Dataset Overview
        st.subheader("📊 Dataset Overview")
        st.dataframe(df.head())
        st.markdown(f"**Shape:** {df.shape[0]:,} rows × {df.shape[1]} columns")

        # Summary Statistics
        st.subheader("📈 Summary Statistics")
        st.dataframe(df.describe().T)

        # Visualization
        st.sidebar.header(f"📊 Visualization Options ({filename})")
        chart_type = st.sidebar.radio(
            f"Choose chart type for {filename}:",
            ["Line Plot", "Boxplot", "Correlation Heatmap"],
            key=filename
        )

        if chart_type == "Line Plot":
            if "Timestamp" in df.columns:
                df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors='coerce')
            variable = st.sidebar.selectbox("Select variable", ["GHI", "DNI", "DHI", "Tamb", "WS"], key=f"{filename}_line")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(df["Timestamp"], df[variable], color="#f59e0b")
            ax.set_title(f"{variable} over Time ({filename})", fontsize=14)
            ax.set_xlabel("Time")
            ax.set_ylabel(variable)
            st.pyplot(fig)

        elif chart_type == "Boxplot":
            variable = st.sidebar.selectbox("Select variable", ["GHI", "DNI", "DHI", "Tamb", "WS"], key=f"{filename}_box")
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.boxplot(y=df[variable], color="#facc15", ax=ax)
            ax.set_title(f"Boxplot of {variable} ({filename})", fontsize=14)
            st.pyplot(fig)

        elif chart_type == "Correlation Heatmap":
            st.subheader(f"🔥 Correlation Heatmap ({filename})")
            selected_cols = ["GHI", "DNI", "DHI", "Tamb", "WS", "TModA", "TModB", "Precipitation"]
            selected_cols = [c for c in selected_cols if c in df.columns]
            corr = df[selected_cols].corr()
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap="YlOrRd", ax=ax)
            st.pyplot(fig)

        st.divider()  # Separate each file section visually

else:
    st.info("👈 Please upload one or more CSV files to begin visualization.")

# ---------------- Footer ----------------
st.markdown('<div class="footer">Developed by <b>Kalkidan Tesfaye</b> | MoonLight Energy Solutions ☀️</div>', unsafe_allow_html=True)
