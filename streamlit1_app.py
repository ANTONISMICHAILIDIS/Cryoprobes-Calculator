import streamlit as st
import pandas as pd
import numpy as np

def calculate_probes(tumor_length, tumor_width, tumor_height, margin_required, probe_type):
    """
    Calculate the number of cryoprobes needed for complete tumor ablation.
    """
    probe_data = {
        "Icerod": (2.5, 4),
        "Icesphere": (2, 3),
        "Iceforce": (3.5, 5)
    }
    
    if probe_type not in probe_data:
        return "Invalid probe type"
    
    iceball_min, iceball_max = probe_data[probe_type]
    d_ablation = max(tumor_length, tumor_width, tumor_height) + 2 * margin_required
    
    if iceball_max >= d_ablation:
        return 2  # Minimum two probes required
    
    n_probes = math.ceil(d_ablation / (iceball_max - 1.5))
    return max(n_probes, 2)

def main():
    st.set_page_config(page_title="Cryoablation Probe Calculator", layout="centered")
    
    st.title("Cryoablation Probe Calculator")
    st.markdown("Calculate the optimal number of cryoprobes required for renal tumor ablation based on tumor dimensions and probe characteristics.")
    
    # Sidebar for user input
    st.sidebar.header("Tumor Input Parameters")
    tumor_length = st.sidebar.number_input("Tumor Length (cm)", min_value=1.0, step=0.1)
    tumor_width = st.sidebar.number_input("Tumor Width (cm)", min_value=1.0, step=0.1)
    tumor_height = st.sidebar.number_input("Tumor Height (cm)", min_value=1.0, step=0.1)
    
    # Define margin based on tumor size
    margin_required = 1.0 if max(tumor_length, tumor_width, tumor_height) > 4 else 0.5
    st.sidebar.write(f"**Required Ablation Margin:** {margin_required} cm")
    
    probe_type = st.sidebar.selectbox("Select Cryoprobe Type", ["Icerod", "Icesphere", "Iceforce"])
    
    if st.sidebar.button("Calculate Probes"):
        n_probes = calculate_probes(tumor_length, tumor_width, tumor_height, margin_required, probe_type)
        st.success(f"Recommended Number of Probes: {n_probes}")
    
    # Display cryoprobe details
    st.subheader("Cryoprobe Information")
    st.write("Different cryoprobes create different iceball sizes. Choose the best option for optimal ablation coverage.")
    probe_df = pd.DataFrame({
        "Cryoprobe": ["Icerod", "Icesphere", "Iceforce"],
        "Iceball Size (cm)": ["2.5 × 4", "2 × 3", "3.5 × 5"],
        "Shape": ["Elliptical", "Spherical", "Hybrid"]
    })
    st.table(probe_df)
    
    # Footer
    st.markdown("---")
    st.markdown("Developed for efficient renal cryoablation planning.")

if __name__ == "__main__":
    main()
