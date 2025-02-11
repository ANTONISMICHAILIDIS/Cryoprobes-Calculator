import streamlit as st
import numpy as np
import pandas as pd

# Title and Description
st.title("Renal Cryoablation Treatment Planning")
st.markdown("""
This application provides treatment recommendations for renal cryoablation based on patient and tumor characteristics.
Please input the relevant parameters below.
""")

# Input Widgets
st.sidebar.header("Patient and Tumor Characteristics")
age = st.sidebar.number_input("Patient Age", min_value=18, max_value=100, value=65)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
num_lesions = st.sidebar.number_input("Number of Lesions", min_value=1, max_value=5, value=1)
tumor_length = st.sidebar.number_input("Tumor Length (cm)", min_value=0.5, max_value=10.0, value=3.0)
tumor_width = st.sidebar.number_input("Tumor Width (cm)", min_value=0.5, max_value=10.0, value=2.5)
tumor_height = st.sidebar.number_input("Tumor Height (cm)", min_value=0.5, max_value=10.0, value=2.5)
renal_score = st.sidebar.number_input("Renal Complexity Score (PADUA/RENAL)", min_value=4, max_value=12, value=6)
histological_type = st.sidebar.selectbox("Histological Type", ["Clear Cell", "Papillary", "Chromophobe"])
isup_grade = st.sidebar.selectbox("ISUP Grade", ["1", "2", "3", "4"])

# Processing Logic (Simplified Decision Rules)
# For demonstration purposes, we use simple thresholds derived from our retrospective analysis.

def treatment_plan(length, width, height, score, grade):
    avg_size = np.mean([length, width, height])
    # Determine probe number based on average size and renal complexity
    if avg_size < 2.5 and score <= 6 and grade == "1":
        probes = 2
    elif avg_size < 3.5 and score <= 8:
        probes = 3
    else:
        probes = 4

    # Recommend hydrodissection if the ablation margin (simulated as a function of score) is below threshold.
    # Here, we assume a lower renal score suggests a safer zone, higher score might indicate proximity to critical structures.
    if score >= 8 or avg_size > 3.0:
        hydro = "Yes"
        hydro_num = 1 if score < 10 else 2
        hydro_target = "Colon/Perirenal fat" if score < 10 else "Colon/Adjacent structures"
    else:
        hydro = "No"
        hydro_num = 0
        hydro_target = "N/A"

    return probes, hydro, hydro_num, hydro_target

# Generate treatment plan based on inputs
probes, hydro, hydro_num, hydro_target = treatment_plan(tumor_length, tumor_width, tumor_height, renal_score, isup_grade)

st.header("Recommended Treatment Plan")
st.write(f"**Number of Cryoprobes:** {probes}")
st.write(f"**Hydrodissection Recommended:** {hydro}")
if hydro == "Yes":
    st.write(f"**Number of Hydrodissection Sites:** {hydro_num}")
    st.write(f"**Target Structures for Hydrodissection:** {hydro_target}")

# Predictive outcomes based on retrospective data
def predict_outcomes(probes, score):
    # For demonstration, recurrence risk increases slightly with higher probe number and complexity score
    recurrence_1m = 5 + (score - 6) * 1.5  # baseline 5% at 1 month plus increment
    recurrence_3m = 8 + (score - 6) * 2.0  # baseline 8% at 3 months
    complications = 4 + (probes - 2) * 1.5  # baseline 4% with 2 probes

    # Bound percentages between 0 and 100%
    recurrence_1m = min(max(recurrence_1m, 0), 100)
    recurrence_3m = min(max(recurrence_3m, 0), 100)
    complications = min(max(complications, 0), 100)
    return recurrence_1m, recurrence_3m, complications

rec_1m, rec_3m, comp_rate = predict_outcomes(probes, renal_score)

st.header("Predicted Outcomes")
st.write(f"**Estimated Recurrence/Residual Tumor at 1 Month:** {rec_1m:.1f}%")
st.write(f"**Estimated Recurrence/Residual Tumor at 3 Months:** {rec_3m:.1f}%")
st.write(f"**Estimated Complication Rate:** {comp_rate:.1f}%")

# Reference Percentages from Literature
st.markdown("---")
st.subheader("Reference Data")
st.markdown("""
- **Recurrence/Residual Tumor Rates:**  
  - Literature reports recurrence rates of approximately 5–10% at 1 month and 10–15% at 3 months.
- **Complication Rates:**  
  - Reported complication rates in cryoablation range from 4% to 7%.
""")
