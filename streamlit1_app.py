import streamlit as st
import numpy as np
import pandas as pd

# -------------------------------------------------------------------
# 1. Embed your entire table data as a list of dictionaries.
#    Each dict represents one row, matching the columns in your table.
# -------------------------------------------------------------------
table_data = [
    {
        "location_distance_hilum": "UPPER POLE / ABUTT (1,1)",
        "size_mass": "1,9 x 2,1 x 2,8",
        "cryoprobes": "3 rod",
        "types_of_probes": "ROD",
        "size_ice_ball": "2,7x1,9x3,2",
        "protection": "NO",
        "complications": "NONE",
        "renal_score": "7P",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/45",
        "size_mass": "1 Χ 1,7 Χ 1,3",
        "cryoprobes": "1",
        "types_of_probes": "",
        "size_ice_ball": "1,4 Χ 2,6 Χ 2,8 ή 1,7",
        "protection": "YES/COLON SPLEEN",
        "complications": "NONE",
        "renal_score": "6x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/1,5mm",
        "size_mass": "2,1 x 2,5 x 2,8",
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_ice_ball": "2,8 x 2,7 x 3,5",
        "protection": "NONE",
        "complications": "NONE",
        "renal_score": "5p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    # ----------------------------------------------------------------
    #  Continue adding all rows from your table here...
    #  or load them from a CSV/Excel if you prefer.
    # ----------------------------------------------------------------
]

# Convert the data to a DataFrame for easy display
df_table = pd.DataFrame(table_data)

# -------------------------------------------------------------------
# 2. Title and Intro
# -------------------------------------------------------------------
st.title("Renal Cryoablation Treatment Planning")
st.markdown("""
This application provides treatment recommendations for **renal cryoablation** based on patient and tumor characteristics.

Below, you can **browse** the existing cases from the large table, and/or **input** new parameters in the sidebar to generate
a recommended plan for a new case.
""")

# -------------------------------------------------------------------
# 3. Display the big table in the main interface
# -------------------------------------------------------------------
st.subheader("Existing Cases from Large Table")
st.dataframe(df_table, use_container_width=True)

# -------------------------------------------------------------------
# 4. Sidebar Input Widgets (Your Original Code)
# -------------------------------------------------------------------
st.sidebar.header("Enter New Case Parameters")
age = st.sidebar.number_input("Patient Age", min_value=18, max_value=100, value=65)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
num_lesions = st.sidebar.number_input("Number of Lesions", min_value=1, max_value=5, value=1)
tumor_length = st.sidebar.number_input("Tumor Length (cm)", min_value=0.5, max_value=10.0, value=3.0)
tumor_width = st.sidebar.number_input("Tumor Width (cm)", min_value=0.5, max_value=10.0, value=2.5)
tumor_height = st.sidebar.number_input("Tumor Height (cm)", min_value=0.5, max_value=10.0, value=2.5)
renal_score = st.sidebar.number_input("Renal Complexity Score (PADUA/RENAL)", min_value=4, max_value=12, value=6)
histological_type = st.sidebar.selectbox("Histological Type", ["Clear Cell", "Papillary", "Chromophobe"])
isup_grade = st.sidebar.selectbox("ISUP Grade", ["1", "2", "3", "4"])

# -------------------------------------------------------------------
# 5. Processing Logic (Simple thresholds for demonstration)
# -------------------------------------------------------------------
def treatment_plan(length, width, height, score, grade):
    avg_size = np.mean([length, width, height])
    # Decide number of probes
    if avg_size < 2.5 and score <= 6 and grade == "1":
        probes = 2
    elif avg_size < 3.5 and score <= 8:
        probes = 3
    else:
        probes = 4

    # Hydrodissection logic
    if score >= 8 or avg_size > 3.0:
        hydro = "Yes"
        hydro_num = 1 if score < 10 else 2
        hydro_target = "Colon/Perirenal fat" if score < 10 else "Colon/Adjacent structures"
    else:
        hydro = "No"
        hydro_num = 0
        hydro_target = "N/A"

    return probes, hydro, hydro_num, hydro_target

def predict_outcomes(probes, score):
    # Simple demonstration
    recurrence_1m = 5 + (score - 6)*1.5
    recurrence_3m = 8 + (score - 6)*2.0
    complications = 4 + (probes - 2)*1.5

    # Bound between 0 and 100
    recurrence_1m = min(max(recurrence_1m, 0), 100)
    recurrence_3m = min(max(recurrence_3m, 0), 100)
    complications = min(max(complications, 0), 100)
    return recurrence_1m, recurrence_3m, complications

# -------------------------------------------------------------------
# 6. Button to Generate Plan
# -------------------------------------------------------------------
if st.sidebar.button("Compute Plan for New Case"):
    # Run logic
    probes, hydro, hydro_num, hydro_target = treatment_plan(tumor_length, tumor_width, tumor_height, renal_score, isup_grade)
    rec_1m, rec_3m, comp_rate = predict_outcomes(probes, renal_score)

    # Display results
    st.header("Recommended Treatment Plan (New Case)")
    st.write(f"**Number of Cryoprobes:** {probes}")
    st.write(f"**Hydrodissection Recommended:** {hydro}")
    if hydro == "Yes":
        st.write(f"**Number of Hydrodissection Sites:** {hydro_num}")
        st.write(f"**Target Structures for Hydrodissection:** {hydro_target}")

    st.header("Predicted Outcomes")
    st.write(f"**Estimated Recurrence/Residual Tumor at 1 Month:** {rec_1m:.1f}%")
    st.write(f"**Estimated Recurrence/Residual Tumor at 3 Months:** {rec_3m:.1f}%")
    st.write(f"**Estimated Complication Rate:** {comp_rate:.1f}%")

    st.markdown("---")
    st.subheader("Reference Data")
    st.markdown("""
    - **Recurrence/Residual Tumor Rates:**  
      ~5–10% at 1 month, ~10–15% at 3 months
    - **Complication Rates:**  
      ~4–7% for renal cryoablation
    """)
else:
    st.info("Enter parameters in the sidebar and click 'Compute Plan for New Case' to see recommendations.")
