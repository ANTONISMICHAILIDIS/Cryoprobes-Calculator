import streamlit as st
import pandas as pd
import numpy as np

# ------------------------------------
# A) Define the Main Table (df_main)
# (Note: "Location / Distance from Hilum" has been removed from user inputs.)
# ------------------------------------
main_data = [
    {"size_mass": "1,9 x 2,1 x 2,8", "RENAL_score": "7P", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "1 x 1,7 x 1,3", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,1 x 2,5 x 2,8", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2 x 2,8 x 2,8", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "1,6 x 1,2 x 1,8", "RENAL_score": "7p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,9 x 2,6 x 2,8", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,9 x 2,6 x 3 (1,9 x 2,2 x 3)", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3,5 x 3,4 x 3,9", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,1 x 1,9 x 1,9", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,3 x 2 x 2,1", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,9 x 3,3 x 3,1", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3,6 x 3,5 x 3,7", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3,6 x 3,8 x 2,8", "RENAL_score": "7ph", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3,2 x 3,4 x 3,1", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3 x 2,8 x 2,7", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,8 x 2,4 x 2", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "1,7 x 1,6 x 1,8", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,6 x 2,5 x 2,6", "RENAL_score": "7xh", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "5,8 x 4,3 x 6,2", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,9 x 3,2 x 2,6", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "1,4 x 1,4 x 1,5", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,6 x 2,3 x 2,1", "RENAL_score": "7ph", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2 x 1,8 x 1,9", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3,2 x 2,9 x 3,2", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3,1 x 2,9 x 2,8", "RENAL_score": "6a", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "1,9 x 1,6 x 1,6", "RENAL_score": "6x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2 x 2,5 x 2,3", "RENAL_score": "7p", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,4 x 2,6 x 2", "RENAL_score": "6a", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "3,6 x 3,7 x 4,3", "RENAL_score": "10a", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "1,8 x 2 x 2,1", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 1"},
    {"size_mass": "2,2 x 2,5 x 2,4", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 2"},
    {"size_mass": "2,5 x 2,1 x 2,2", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 5"},
    {"size_mass": "19 x 19 x 2,1", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 6"},
    {"size_mass": "2,6 x 2,5 x 2,1", "RENAL_score": "4a", "BIOPSY": "CLEAR CELL GR 7"},
    {"size_mass": "4,6 x 3,8 x 4,8", "RENAL_score": "8x", "BIOPSY": "CLEAR CELL GR 8"},
    {"size_mass": "2,6 x 1,9 x 2,2", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 11"},
    {"size_mass": "4,2 x 3,6 x 4,6", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 12"},
    {"size_mass": "3,1 x 2,5 x 4,8", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 14"},
    {"size_mass": "3,1 x 3,9 x 3,4", "RENAL_score": "4x", "BIOPSY": "CLEAR CELL GR 15"},
    {"size_mass": "2,5 x 2,7 x 2,8", "RENAL_score": "5x", "BIOPSY": "CLEAR CELL GR 16"},
    {"size_mass": "3,4 x 3,5 x 2,9", "RENAL_score": "6p", "BIOPSY": "CLEAR CELL GR 17"},
    {"size_mass": "3,7 x 3,5 x 3,4", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 18"},
    {"size_mass": "1,7 x 1,9 x 2", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 20"},
    {"size_mass": "3,7 x 3,5 x 4", "RENAL_score": "4a", "BIOPSY": "CLEAR CELL GR 21"},
    {"size_mass": "2,4 x 2,0 x 2,6", "RENAL_score": "4p", "BIOPSY": "CLEAR CELL GR 22"},
    {"size_mass": "2,6 x 2,3 x 2,1", "RENAL_score": "7ah", "BIOPSY": "CLEAR CELL GR 23"},
    {"size_mass": "2,9 x 2,7 x 2,7", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 24"},
    {"size_mass": "3,2 x 2,5 x 3,7", "RENAL_score": "4ah", "BIOPSY": "CLEAR CELL GR 25"},
    {"size_mass": "2,9 x 2,8 x 2,9", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 26"},
    {"size_mass": "3,7 x 3,2 x 3,5", "RENAL_score": "5a", "BIOPSY": "CLEAR CELL GR 27"},
    {"size_mass": "2 x 2,2 x 1,9", "RENAL_score": "4a", "BIOPSY": "CLEAR CELL GR 28"},
    {"size_mass": "2,8 x 2,7 x 2", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 30"},
    {"size_mass": "2 x 1 x 2", "RENAL_score": "5p", "BIOPSY": "CLEAR CELL GR 31"}
]
df_main = pd.DataFrame(main_data)

# ------------------------------------
# B) Define the Cryoablation Results Table (df_cryo)
# ------------------------------------
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

# ------------------------------------
# Merge the two tables by index (assume rows are aligned)
# ------------------------------------
df_main.index.name = "index"
df_cryo.index.name = "index"
df_merged = pd.merge(df_main, df_cryo, left_index=True, right_index=True)

# ------------------------------------
# Helper function to parse "size_mass" into a numeric array
# ------------------------------------
def parse_size(s):
    try:
        # Replace commas with dots, split on "x", and convert to floats
        parts = s.replace(',', '.').split('x')
        return [float(part.strip()) for part in parts]
    except Exception as e:
        return None

df_merged["size_parsed"] = df_merged["size_mass"].apply(parse_size)

# ------------------------------------
# Streamlit App Interface
# ------------------------------------
st.title("Renal Cryoablation Treatment Planner")
st.markdown("""
This application matches your tumor characteristics to our reference data and provides a recommended cryoablation plan.
Enter your tumor parameters in the sidebar.
""")

# ---------------------------
# Sidebar: User Input Section (without Location)
# ---------------------------
st.sidebar.header("Enter Tumor Parameters")

# Tumor Size: separate number inputs for length, width, height.
inp_length = st.sidebar.number_input("Tumor Length (cm)", min_value=0.5, max_value=10.0, value=4.2)
inp_width  = st.sidebar.number_input("Tumor Width (cm)", min_value=0.5, max_value=10.0, value=3.6)
inp_height = st.sidebar.number_input("Tumor Height (cm)", min_value=0.5, max_value=10.0, value=4.6)
inp_size_mass = f"{inp_length} x {inp_width} x {inp_height}"

# RENAL Score: numeric part and suffix.
inp_renal_numeric = st.sidebar.number_input("RENAL Score (numeric)", min_value=1, max_value=12, value=5)
inp_renal_suffix = st.sidebar.selectbox("RENAL Score Suffix", options=["a", "p", "x"], index=1)
inp_renal_score = f"{inp_renal_numeric}{inp_renal_suffix}"

# Histology Type & Grade (Biopsy Type)
histology_options = ["CLEAR CELL", "PAPILLARY", "CHROMOPHOBE"]
inp_histology = st.sidebar.selectbox("Histology Type", options=histology_options, index=0)
grade_options = ["GR 1", "GR 2", "GR 3", "GR 4", "GR 5", "GR 6", "GR 7", "GR 8", "GR 9", "GR 10", "GR 11", "GR 12", "GR 13", "GR 14", "GR 15", "GR 16", "GR 17", "GR 18", "GR 20", "GR 21", "GR 22", "GR 23", "GR 24", "GR 25", "GR 26", "GR 27", "GR 28", "GR 30", "GR 31"]
inp_grade = st.sidebar.selectbox("Cancer Grade", options=grade_options, index=11)  # Default "GR 12"
inp_biopsy = f"{inp_histology} {inp_grade}"

# Display user input for confirmation
st.sidebar.markdown("### Your Input:")
st.sidebar.write(f"**Tumor Size (Mass):** {inp_size_mass} cm")
st.sidebar.write(f"**RENAL Score:** {inp_renal_score}")
st.sidebar.write(f"**Biopsy Type:** {inp_biopsy}")

# ------------------------------------
# Matching Algorithm: Find the closest reference row (based on tumor dimensions and RENAL score, filtered by biopsy type)
# ------------------------------------
if st.sidebar.button("Generate Cryoablation Plan"):
    # Filter the merged dataframe by biopsy type (case-insensitive)
    df_filtered = df_merged[
        df_merged["BIOPSY"].str.strip().str.lower() == inp_biopsy.strip().lower()
    ]
    
    if df_filtered.empty:
        st.error("No matching data found for the given Biopsy Type. Please check your inputs.")
    else:
        # Helper: extract numeric value from RENAL score (e.g., "5p" -> 5)
        def extract_numeric_from_score(s):
            try:
                return float(''.join(ch for ch in s if ch.isdigit() or ch == '.'))
            except:
                return np.nan
        
        # User tumor dimensions as a sorted numpy array and mean
        user_dims = np.array([inp_length, inp_width, inp_height])
        user_sorted = np.sort(user_dims)
        user_mean = np.mean(user_dims)
        user_renal_numeric = float(inp_renal_numeric)
        
        best_idx = None
        best_diff = float("inf")
        
        # Iterate over filtered rows and compute a weighted difference metric
        for idx, row in df_filtered.iterrows():
            parsed = row["size_parsed"]
            if parsed is None or len(parsed) != 3:
                continue
            ref_dims = np.array(parsed)
            ref_sorted = np.sort(ref_dims)
            ref_mean = np.mean(ref_dims)
            ref_renal = extract_numeric_from_score(row["RENAL_score"])
            
            # Compute difference metric:
            #   - 2x the difference in mean dimensions
            #   - Sum of absolute differences in each sorted dimension
            #   - Absolute difference in the RENAL numeric score
            diff = abs(ref_mean - user_mean)*2 + np.sum(np.abs(ref_sorted - user_sorted)) + abs(ref_renal - user_renal_numeric)
            
            if diff < best_diff:
                best_diff = diff
                best_idx = idx
        
        if best_idx is None:
            st.error("No matching data found. Please verify your tumor size or RENAL score.")
        else:
            match = df_filtered.loc[best_idx]
            st.header("Recommended Cryoablation Plan")
            st.subheader("Input Parameters")
            st.write(f"**Tumor Size (Mass):** {match['size_mass']} cm")
            st.write(f"**RENAL Score:** {match['RENAL_score']}")
            st.write(f"**Biopsy Type:** {match['BIOPSY']}")
            st.markdown("---")
            st.subheader("Cryoablation Parameters")
            st.write(f"**Cryoprobes:** {match['cryoprobes']}")
            st.write(f"**Types of Probes:** {match['types_of_probes']}")
            st.write(f"**Estimated Ice Ball Size:** {match['size_Ice_ball']} cm")
            st.write(f"**Protection:** {match['protection']}")
            st.write(f"**Complications:** {match['complications']}")
            st.info(f"Matching difference metric: {best_diff:.2f}")

st.markdown("---")
st.write("Created by Michailidis A. for free use (demo).")
