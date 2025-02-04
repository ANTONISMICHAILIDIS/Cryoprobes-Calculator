import streamlit as st
import pandas as pd
import numpy as np

def suggest_probes(tumor_length, tumor_width, tumor_height, margin_required):
    """
    Automatically suggests the optimal cryoprobe combination based on tumor size and required ablation margin.
    """
    probe_data = [
        {"name": "Icerod", "iceball": (2.5, 4), "shape": "Elliptical"},
        {"name": "Icesphere", "iceball": (2, 3), "shape": "Spherical"},
        {"name": "Iceforce", "iceball": (3.5, 5), "shape": "Hybrid"}
    ]
    
    d_ablation = max(tumor_length, tumor_width, tumor_height) + 2 * margin_required
    
    # If lesion is very small, use a single Icesphere probe
    if d_ablation <= 3:
        return ["Icesphere (1 probe)"]
    
    # Prefer to use at least two probes if possible
    for probe in probe_data:
        iceball_max = probe["iceball"][1]
        if iceball_max >= d_ablation:
            return [f"{probe['name']} (1 probe)"] if d_ablation <= iceball_max else [f"{probe['name']} (2 probes)"]
    
    # If no single probe can fully cover the lesion, try combining probes
    combinations = []
    for probe in probe_data:
        for secondary_probe in probe_data:
            combined_max = probe["iceball"][1] + secondary_probe["iceball"][1] - 1  # 1cm overlap
            if combined_max >= d_ablation:
                return [f"{probe['name']} + {secondary_probe['name']} (2 probes)"]
    
    # Default to using two Icesphere probes with minimum spacing of 1 cm
    return ["Icesphere (2 probes, 1cm spacing)"]

def main():
    st.set_page_config(page_title="Cryoablation Probe Calculator", layout="centered")
    
    st.title("Cryoablation Probe Calculator")
    st.markdown("Automatically suggests the optimal cryoprobes required for renal tumor ablation based on tumor dimensions.")
    
    # Sidebar for user input
    st.sidebar.header("Tumor Input Parameters")
    tumor_length = st.sidebar.number_input("Tumor Length (cm)", min_value=1.0, step=0.1)
    tumor_width = st.sidebar.number_input("Tumor Width (cm)", min_value=1.0, step=0.1)
    tumor_height = st.sidebar.number_input("Tumor Height (cm)", min_value=1.0, step=0.1)
    
    # Define margin based on tumor size
    margin_required = 1.0 if max(tumor_length, tumor_width, tumor_height) > 4 else 0.5
    st.sidebar.write(f"**Required Ablation Margin:** {margin_required} cm")
    
    if st.sidebar.button("Calculate Probes"):
        suggested_probes = suggest_probes(tumor_length, tumor_width, tumor_height, margin_required)
        st.success(f"Recommended Probes: {', '.join(suggested_probes)}")
    
    # Display cryoprobe details
    st.subheader("Cryoprobe Information")
    st.write("Different cryoprobes create different iceball sizes. The algorithm selects the best combination for optimal ablation coverage.")
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
