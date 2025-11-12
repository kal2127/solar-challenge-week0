import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Solar Investment Strategy Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DATA SIMULATION (Based on your final report findings) ---
# NOTE: In a real application, you would load your cleaned dataframes here.
@st.cache_data
def load_data():
    # Simulate the final ranking table based on your report's findings
    ranking_data = {
        'Rank': [1, 2, 3],
        'Country': ['Benin', 'Togo', 'Sierra Leone'],
        'GHI Mean (W/m²)': [240.56, 223.86, 201.96],
        'WS Coeff (Cooling)': [-1.12, -0.98, -0.85],
        'Soiling Loss (%)': [4.85, 3.90, 6.15],
        'SII Score': [95, 88, 72] # Simulated Final Index Score
    }
    df_ranking = pd.DataFrame(ranking_data).set_index('Rank')

    return df_ranking

df_ranking = load_data()


# --- 3. PAGE FUNCTIONS ---

def overview_page():
    """Displays the final recommendation and key results."""
    st.title("Final Strategic Recommendation")
    st.markdown("""
    This dashboard synthesizes the analysis of raw energy potential, operational efficiency, and maintenance risks to provide a data-driven investment ranking.
    """)

    st.subheader("1. Final Solar Investment Ranking (SII Score)")
    st.markdown("""
    The Solar Investment Index (SII) score combines GHI, Wind Mitigation (WS Coeff), and Soiling Loss into a single metric. Benin is the clear top choice.
    """)

    # Display Ranking Table
    st.dataframe(df_ranking, use_container_width=True)

    # Display the final bar chart image
    st.subheader("2. Final Investment Index Visualization")
    final_chart_path = 'image_43fe7c.png'
    if os.path.exists(final_chart_path):
        st.image(final_chart_path, caption='Solar Investment Index (SII) - Final Ranking', use_column_width=True)
    else:
        st.warning(f"Image not found: {final_chart_path}. Please place the file in the same directory as this script.")

def deep_dive_page():
    """Displays supporting visualization evidence."""
    st.title("Supporting Analytical Evidence")
    st.markdown("Use the selection boxes to view the underlying data that informed the final ranking.")

    # Select box for the variable/metric
    analysis_type = st.selectbox(
        "Select Key Metric Visualization:",
        ["Raw Potential (GHI Boxplot)", "Operational Efficiency (TModA vs WS)"]
    )

    if analysis_type == "Raw Potential (GHI Boxplot)":
        st.subheader("GHI Distribution by Country (Raw Energy Potential)")
        st.markdown("This visualization confirms the statistical differences in Global Horizontal Irradiance, demonstrating Benin's superior raw solar resource.")
        
        # Display the GHI Boxplot image
        ghi_boxplot_path = 'image_2501c1.jpg'
        if os.path.exists(ghi_boxplot_path):
            st.image(ghi_boxplot_path, caption='GHI Boxplot Comparison', use_column_width=True)
        else:
            st.warning(f"Image not found: {ghi_boxplot_path}. Please place the file in the same directory.")

    elif analysis_type == "Operational Efficiency (TModA vs WS)":
        st.subheader("TModA vs. Wind Speed (WS) Scatter Plot")
        st.markdown("This plot illustrates the negative correlation: as wind speed increases, the module temperature (and thus efficiency loss) decreases. This is the foundation of the Wind Mitigation Score.")
        
        # Display the TModA vs WS Scatter Plot image
        scatter_plot_path = 'image_26725f.png'
        if os.path.exists(scatter_plot_path):
            st.image(scatter_plot_path, caption='Module Temperature vs. Wind Speed', use_column_width=True)
        else:
            st.warning(f"Image not found: {scatter_plot_path}. Please place the file in the same directory.")

# --- 4. NAVIGATION ---
st.sidebar.title("MoonLight Energy Solutions")
st.sidebar.header("Solar Investment Dashboard")

# Radio button for page selection
page = st.sidebar.radio("Select Dashboard View:", ["Overview", "Deep Dive/Analysis"])

if page == "Overview":
    overview_page()
elif page == "Deep Dive/Analysis":
    deep_dive_page()

st.sidebar.markdown("---")
st.sidebar.info("Data simulated based on Final Report findings. Images must be saved in the same directory as the script.")