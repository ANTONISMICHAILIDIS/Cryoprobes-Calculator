import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# A) Define the Main Table (df_main)
# -------------------------
main_data = [
    {"location_distance_hilum": "UPPER POLE / ABUTT (1,1)", "size_mass": "1,9 x 2,1 x 2,8", "RENAL_score": "7P", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/45", "size_mass": "1 x 1,7 x 1,3", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/1,5mm", "size_mass": "2,1 x 2,5 x 2,8", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/>7mm", "size_mass": "2 x 2,8 x 2,8", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/4mm", "size_mass": "1,6 x 1,2 x 1,8", "RENAL_score": "7p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/ 30", "size_mass": "2,9 x 2,6 x 2,8", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/35", "size_mass": "2,9 x 2,6 x 3 (1,9 x 2,2 x 3)", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/15", "size_mass": "3,5 x 3,4 x 3,9", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/22", "size_mass": "2,1 x 1,9 x 1,9", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/10mm", "size_mass": "2,3 x 2 x 2,1", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/ 17mm", "size_mass": "2,9 x 3,3 x 3,1", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/30mm", "size_mass": "3,6 x 3,5 x 3,7", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/ <1mm", "size_mass": "3,6 x 3,8 x 2,8", "RENAL_score": "7ph", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/ 23mm", "size_mass": "3,2 x 3,4 x 3,1", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/28mm", "size_mass": "3 x 2,8 x 2,7", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/middle/11mm", "size_mass": "2,8 x 2,4 x 2", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/16mm", "size_mass": "1,7 x 1,6 x 1,8", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/10mm", "size_mass": "2,6 x 2,5 x 2,6", "RENAL_score": "7xh", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/1mm", "size_mass": "5,8 x 4,3 x 6,2", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/21mm", "size_mass": "2,9 x 3,2 x 2,6", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/43mm", "size_mass": "1,4 x 1,4 x 1,5", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/<1mm", "size_mass": "2,6 x 2,3 x 2,1", "RENAL_score": "7ph", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/33mm", "size_mass": "2 x 1,8 x 1,9", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/ 20", "size_mass": "3,2 x 2,9 x 3,2", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "lower/32", "size_mass": "3,1 x 2,9 x 2,8", "RENAL_score": "6a", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/28", "size_mass": "1,9 x 1,6 x 1,6", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle/23", "size_mass": "2 x 2,5 x 2,3", "RENAL_score": "7p", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/ 24", "size_mass": "2,4 x 2,6 x 2", "RENAL_score": "6a", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "middle-upper/5", "size_mass": "3,6 x 3,7 x 4,3", "RENAL_score": "10a", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/ 36", "size_mass": "1,8 x 2 x 2,1", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 1"},
    {"location_distance_hilum": "upper/19", "size_mass": "2,2 x 2,5 x 2,4", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 2"},
    {"location_distance_hilum": "upper/36", "size_mass": "2,5 x 2,1 x 2,2", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 5"},
    {"location_distance_hilum": "lower/33", "size_mass": "19 x 19 x 2,1", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 6"},
    {"location_distance_hilum": "upper/25?", "size_mass": "2,6 x 2,5 x 2,1", "RENAL_score": "4a", "BIOPSY": "CLEAR CELL GR 7"},
    {"location_distance_hilum": "middle/25", "size_mass": "4,6 x 3,8 x 4,8", "RENAL_score": "8x", "BIOPSY": "CLEAR CELL GR 8"},
    {"location_distance_hilum": "middle-lower/13", "size_mass": "2,6 x 1,9 x 2,2", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 11"},
    {"location_distance_hilum": "middle-lower/ 14", "size_mass": "4,2 x 3,6 x 4,6", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 12"},
    {"location_distance_hilum": "lower/43", "size_mass": "3,1 x 2,5 x 4,8", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 14"},
    {"location_distance_hilum": "lower/14", "size_mass": "3,1 x 3,9 x 3,4", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 15"},
    {"location_distance_hilum": "upper/14", "size_mass": "2,5 x 2,7 x 2,8", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 16"},
    {"location_distance_hilum": "middle- upper/ 31", "size_mass": "3,4 x 3,5 x 2,9", "RENAL_score": "6p", "BIOPSY": "CLEAR CELL GR 17"},
    {"location_distance_hilum": "upper/26", "size_mass": "3,7 x 3,5 x 3,4", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 18"},
    {"location_distance_hilum": "middle/12", "size_mass": "1,7 x 1,9 x 2", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 20"},
    {"location_distance_hilum": "upper-middle/12", "size_mass": "3,7 x 3,5 x 4", "RENAL_score": "4a", "BIOPSY": "CLEAR CELL GR 21"},
    {"location_distance_hilum": "lower/38", "size_mass": "2,4 x 2,0 x 2,6", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 22"},
    {"location_distance_hilum": "middle/12", "size_mass": "2,6 x 2,3 x 2,1", "RENAL_score": "7ah", "BIOPSY": "CLEAR CELL GR 23"},
    {"location_distance_hilum": "upper/42", "size_mass": "2,9 x 2,7 x 2,7", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 24"},
    {"location_distance_hilum": "lower/12", "size_mass": "3,2 x 2,5 x 3,7", "RENAL_score": "4ah", "BIOPSY": "CLEAR CELL GR 25"},
    {"location_distance_hilum": "upper/34", "size_mass": "2,9 x 2,8 x 2,9", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 26"},
    {"location_distance_hilum": "middle-lower/26", "size_mass": "3,7 x 3,2 x 3,5", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 27"},
    {"location_distance_hilum": "lower/ 29", "size_mass": "2 x 2,2 x 1,9", "RENAL_score": "4a", "BIOPSY": "CLEAR CELL GR 28"},
    {"location_distance_hilum": "middle/16", "size_mass": "2,8 x 2,7 x 2", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 30"},
    {"location_distance_hilum": "lower/17", "size_mass": "2 x 1 x 2", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 31"}
]

df_main = pd.DataFrame(main_data)

# -------------------------
# B) Define the Cryoablation Results Table (df_cryo)
# -------------------------
cryo_data = [
    {"cryoprobes": "3 rod", "types_of_probes": "ROD", "size_Ice_ball": "2,7x1,9x3,2", "protection": "NO", "complications": "NONE"},
    {"cryoprobes": "1", "types_of_probes": "", "size_Ice_ball": "1,4 x 2,6 x 2,8 or 1,7", "protection": "YES/COLON SPLEEN", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "2,8 x 2,7 x 3,5", "protection": "NONE", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "ROD", "size_Ice_ball": "3 x 3,6 x 2", "protection": "NONE", "complications": "PNEUMOTH"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "2,7 x 2,4 x 2,8", "protection": "NONE", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "", "size_Ice_ball": "2,9 x 3 x 4,2", "protection": "YES/SPLEEN", "complications": ""},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3 x 3,8 x 3,4", "protection": "NO", "complications": "MILD HEMORRHAGE?"},
    {"cryoprobes": "4", "types_of_probes": "ROD", "size_Ice_ball": "3,8 x 5,2 x 4,9", "protection": "YES/PSOAS", "complications": "none"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3,2 x 3,4 x 3", "protection": "NO", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "2,7 x 2,4 x 3,2", "protection": "NO", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "4,2 x 3,6 x 4,1", "protection": "NO", "complications": "NONE"},
    {"cryoprobes": "4", "types_of_probes": "ROD", "size_Ice_ball": "3,8 x 4,2 x 4,9", "protection": "YES/COLON", "complications": "MILD HEMORRHAGE?"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "3,5 x 3,6 x 3,3", "protection": "YES/ COLON", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "3,5 x 3,2 x 3,6", "protection": "YES/ COLON", "complications": "MILD HEMORRHAGE?"},
    {"cryoprobes": "3", "types_of_probes": "2ROD+1SPHERE", "size_Ice_ball": "3,6 x 2,9 x 3,4", "protection": "NO", "complications": "NONE?"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "2,7 x 3,7 x 3,5", "protection": "YES/COLON", "complications": ""},
    {"cryoprobes": "1", "types_of_probes": "SPHERE", "size_Ice_ball": "1,2 x 1,8 x 2", "protection": "YES/PSOAS", "complications": ""},
    {"cryoprobes": "3", "types_of_probes": "4SPHERE", "size_Ice_ball": "3,5 x 3,3 x 3,8", "protection": "COLON/SPLEEN", "complications": "none"},
    {"cryoprobes": "5", "types_of_probes": "4FORCE+1ROD", "size_Ice_ball": "5,5 x 5,7 x 6,5", "protection": "YES/COLON/SPLEEN", "complications": "none"},
    {"cryoprobes": "3", "types_of_probes": "ROD", "size_Ice_ball": "3,5 x 4,8 x 4", "protection": "HYDRO/COLON", "complications": "none"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3,1 x 2,9 x 2,7", "protection": "NO", "complications": "MILD HEMORRHAGE"},
    {"cryoprobes": "3", "types_of_probes": "2ROD+1SPHERE", "size_Ice_ball": "2,6 x 4,4 x 3,5", "protection": "YES/LIVER/COLON", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3,1 x 2,5 x 3", "protection": "NO", "complications": "NONE"},
    {"cryoprobes": "4", "types_of_probes": "ROD", "size_Ice_ball": "3,5 x 4,7 x 5", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "4", "types_of_probes": "ROD", "size_Ice_ball": "3,2 x 4 x 4", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3 x 2,5 x 2,8", "protection": "NO", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "2,4 x 3,3 x 3", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "4 x 2,4 x 3,9", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "ROD", "size_Ice_ball": "5,2 x 4 x 4,8", "protection": "YES/SPLEEN", "complications": "MILD HEMORRHAGE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3,7 x 3,3 x 2,8", "protection": "NO", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "SPHERE", "size_Ice_ball": "2,9 x 3,3 x 2,9", "protection": "YES/PSOAS,RENAL VEIN", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "2,7 x 3,4 x 2,7", "protection": "YES/SPLEEN", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3 x 3,6 x 3,8", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3,1 x 2,7 x 2,4", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "4", "types_of_probes": "FORCE", "size_Ice_ball": "5,2 x 4,1 x 4,9", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "SPHERE", "size_Ice_ball": "2,6 x 2,2 x 2,1", "protection": "YES/PSOAS", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "FORCE", "size_Ice_ball": "5,2 x 4,2 x 4,8", "protection": "YES/PSOAS", "complications": "HEMORRHAGE- νοσηλεία"},
    {"cryoprobes": "3", "types_of_probes": "FORCE", "size_Ice_ball": "", "protection": "", "complications": ""},
    {"cryoprobes": "4", "types_of_probes": "FORCE", "size_Ice_ball": "5,0 x 3,5 x 5,3", "protection": "YES/COLON, PSOAS", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "FORCE", "size_Ice_ball": "3,5 x 4,1 x 4,3", "protection": "YES/ COLON", "complications": "MILD HEMORRHAGE"},
    {"cryoprobes": "2", "types_of_probes": "ROD", "size_Ice_ball": "3 x 4,1 x 2,9", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "4", "types_of_probes": "ROD", "size_Ice_ball": "5,5 x 5,5 x 4,6", "protection": "NO", "complications": "MILD HEMORRHAGE"},
    {"cryoprobes": "3", "types_of_probes": "ROD", "size_Ice_ball": "4,2 x 3,9 x 5,4", "protection": "YES/ COLON, PSOAS", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "3,4 x 2,6 x 3,1", "protection": "YES/COLON", "complications": "HEMORRHAGE ΜΕΓΑΛΗ"},
    {"cryoprobes": "4", "types_of_probes": "ROD", "size_Ice_ball": "3,8 x 5,3 x 6,5", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "ROD", "size_Ice_ball": "3,2 x 3,7 x 3,6", "protection": "YES/PSOAS", "complications": "MILD HEMORRHAGE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "2,8 x 2,8 x 2,9", "protection": "YES/COLON", "complications": "NONE"},
    {"cryoprobes": "4", "types_of_probes": "SPHERE", "size_Ice_ball": "4,6 x 3,6 x 3,6", "protection": "YES/LIVER,COLON", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "ROD", "size_Ice_ball": "4,2 x 3,1 x 3,6", "protection": "YES/LIVER,COLON", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "SPHERE", "size_Ice_ball": "3,6 x 3 x 3,5", "protection": "YES/SPLEEN,COLON", "complications": "NONE"},
    {"cryoprobes": "4", "types_of_probes": "ROD", "size_Ice_ball": "4,1 x 4 x 5,2", "protection": "YES/COLON", "complications": "SUBCUTANEUS HEMATOMA / MILD HEMORRHAGE"},
    {"cryoprobes": "3", "types_of_probes": "SPHERE", "size_Ice_ball": "2,7 x 2,9 x 2,6", "protection": "YES/ COLON", "complications": "NONE"},
    {"cryoprobes": "3", "types_of_probes": "SPHERE", "size_Ice_ball": "4,7 x 3,6 x 3,5", "protection": "YES/ COLON", "complications": "NONE"},
    {"cryoprobes": "2", "types_of_probes": "SPHERE", "size_Ice_ball": "2,3 x 33 x 2,5", "protection": "YES/ PSOAS", "complications": "NONE"}
]

df_cryo = pd.DataFrame(cryo_data)

# -------------------------
# Merge the two tables by index (assuming they align row-by-row)
# -------------------------
df_main.index.name = "index"
df_cryo.index.name = "index"
df_merged = pd.merge(df_main, df_cryo, left_index=True, right_index=True)

# -------------------------
# Helper function to parse "size_mass" into a numeric array
# -------------------------
def parse_size(s):
    try:
        parts = s.replace(',', '.').split('x')
        return [float(part.strip()) for part in parts]
    except Exception as e:
        return None

df_merged["size_parsed"] = df_merged["size_mass"].apply(parse_size)

# -------------------------
# Streamlit App Interface
# -------------------------
st.title("Renal Cryoablation Treatment Planner")
st.markdown("""
This application matches your tumor characteristics to our reference data and provides a recommended cryoablation plan.
Enter your tumor parameters in the sidebar.
""")

# Sidebar: User Input Section
st.sidebar.header("Enter Tumor Parameters")

# Location / Distance from Hilum: use selectbox from unique values in df_main
unique_locations = df_main["location_distance_hilum"].unique().tolist()
inp_location = st.sidebar.selectbox("Location / Distance from Hilum", options=unique_locations, index=unique_locations.index("middle-lower/ 14") if "middle-lower/ 14" in unique_locations else 0)

# Tumor Size: separate number inputs for length, width, height.
inp_length = st.sidebar.number_input("Tumor Length (cm)", min_value=0.5, max_value=10.0, value=4.2)
inp_width  = st.sidebar.number_input("Tumor Width (cm)", min_value=0.5, max_value=10.0, value=3.6)
inp_height = st.sidebar.number_input("Tumor Height (cm)", min_value=0.5, max_value=10.0, value=4.6)
inp_size_mass = f"{inp_length} x {inp_width} x {inp_height}"

# RENAL Score: split into numeric part and suffix.
inp_renal_numeric = st.sidebar.number_input("RENAL Score (numeric)", min_value=1, max_value=12, value=5)
inp_renal_suffix = st.sidebar.selectbox("RENAL Score Suffix", options=["a", "p", "x"], index=1)
inp_renal_score = f"{inp_renal_numeric}{inp_renal_suffix}"

# Histology Type & Grade (Biopsy Type)
histology_options = ["CLEAR CELL", "PAPILLARY", "CHROMOPHOBE"]
inp_histology = st.sidebar.selectbox("Histology Type", options=histology_options, index=0)
grade_options = ["GR 1", "GR 2", "GR 3", "GR 4", "GR 5", "GR 6", "GR 7", "GR 8", "GR 9", "GR 10", "GR 11", "GR 12", "GR 13", "GR 14", "GR 15", "GR 16", "GR 17", "GR 18", "GR 20", "GR 21", "GR 22", "GR 23", "GR 24", "GR 25", "GR 26", "GR 27", "GR 28", "GR 30", "GR 31"]
inp_grade = st.sidebar.selectbox("Cancer Grade", options=grade_options, index=11)  # Default "GR 12"
inp_biopsy = f"{inp_histology} {inp_grade}"

# Display the user inputs for confirmation
st.sidebar.markdown("### Your Input:")
st.sidebar.write(f"**Location / Distance from Hilum:** {inp_location}")
st.sidebar.write(f"**Tumor Size (Mass):** {inp_size_mass} cm")
st.sidebar.write(f"**RENAL Score:** {inp_renal_score}")
st.sidebar.write(f"**Biopsy Type:** {inp_biopsy}")

# When the user clicks the button, find the closest matching row
if st.sidebar.button("Generate Cryoablation Plan"):
    # Filter by location and biopsy type first (case-insensitive)
    df_filtered = df_merged[
        (df_merged["location_distance_hilum"].str.strip().str.lower() == inp_location.strip().lower()) &
        (df_merged["BIOPSY"].str.strip().str.lower() == inp_biopsy.strip().lower())
    ]
    
    if df_filtered.empty:
        st.error("No matching data found for the given Location and Biopsy Type. Please check your inputs.")
    else:
        # Compute size difference metric for tumor dimensions and RENAL score
        def extract_numeric_from_score(s):
            try:
                # Extract the numeric part from score (e.g., "5p" -> 5)
                return float(''.join([ch for ch in s if ch.isdigit() or ch == '.']))
            except:
                return np.nan

        user_dims = np.array([inp_length, inp_width, inp_height])
        user_sorted = np.sort(user_dims)
        user_mean = np.mean(user_dims)
        user_renal_numeric = float(inp_renal_numeric)

        best_idx = None
        best_diff = float("inf")
        
        # Iterate only over filtered rows
        for idx, row in df_filtered.iterrows():
            parsed = row["size_parsed"]
            if parsed is None or len(parsed) != 3:
                continue
            ref_dims = np.array(parsed)
            ref_sorted = np.sort(ref_dims)
            ref_mean = np.mean(ref_dims)
            ref_renal = extract_numeric_from_score(row["RENAL_score"])
            # Compute weighted difference: size difference + RENAL score difference
            diff = abs(ref_mean - user_mean) * 2 + np.sum(np.abs(ref_sorted - user_sorted)) + abs(ref_renal - user_renal_numeric)
            if diff < best_diff:
                best_diff = diff
                best_idx = idx
        
        if best_idx is None:
            st.error("No matching data found. Please check your inputs or reference data.")
        else:
            match = df_filtered.loc[best_idx]
            # Use the merged row from df_merged to retrieve cryo plan info
            merged_row = df_merged.loc[match.name]
            st.header("Recommended Cryoablation Plan")
            st.subheader("Input Parameters")
            st.write(f"**Location / Distance from Hilum:** {merged_row['location_distance_hilum']}")
            st.write(f"**Tumor Size (Mass):** {merged_row['size_mass']} cm")
            st.write(f"**RENAL Score:** {merged_row['RENAL_score']}")
            st.write(f"**Biopsy Type:** {merged_row['BIOPSY']}")
            st.markdown("---")
            st.subheader("Cryoablation Parameters")
            st.write(f"**Cryoprobes:** {merged_row['cryoprobes']}")
            st.write(f"**Types of Probes:** {merged_row['types_of_probes']}")
            st.write(f"**Estimated Ice Ball Size:** {merged_row['size_Ice_ball']} cm")
            st.write(f"**Protection:** {merged_row['protection']}")
            st.write(f"**Complications:** {merged_row['complications']}")
            st.info(f"Matching difference metric: {best_diff:.2f}")

st.markdown("---")
st.write("Created by Michailidis A. for free use (demo).")
