import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# A) Define the Main Table (df_main)
# -------------------------
main_data = [
    {
        "location_distance_hilum": "UPPER POLE / ABUTT (1,1)",
        "size_mass": "1,9 x 2,1 x 2,8",
        "RENAL_score": "7P",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/45",
        "size_mass": "1 x 1,7 x 1,3",
        "RENAL_score": "6x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/1,5mm",
        "size_mass": "2,1 x 2,5 x 2,8",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/>7mm",
        "size_mass": "2 x 2,8 x 2,8",
        "RENAL_score": "4x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/4mm",
        "size_mass": "1,6 x 1,2 x 1,8",
        "RENAL_score": "7p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/ 30",
        "size_mass": "2,9 x 2,6 x 2,8",
        "RENAL_score": "5a",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/35",
        "size_mass": "2,9 x 2,6 x 3 (1,9 x 2,2 x 3)",
        "RENAL_score": "6x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/15",
        "size_mass": "3,5 x 3,4 x 3,9",
        "RENAL_score": "4x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/22",
        "size_mass": "2,1 x 1,9 x 1,9",
        "RENAL_score": "5a",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/10mm",
        "size_mass": "2,3 x 2 x 2,1",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/ 17mm",
        "size_mass": "2,9 x 3,3 x 3,1",
        "RENAL_score": "5x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/30mm",
        "size_mass": "3,6 x 3,5 x 3,7",
        "RENAL_score": "5x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/ <1mm",
        "size_mass": "3,6 x 3,8 x 2,8",
        "RENAL_score": "7ph",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/ 23mm",
        "size_mass": "3,2 x 3,4 x 3,1",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/28mm",
        "size_mass": "3 x 2,8 x 2,7",
        "RENAL_score": "4p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/middle/11mm",
        "size_mass": "2,8 x 2,4 x 2",
        "RENAL_score": "6x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/16mm",
        "size_mass": "1,7 x 1,6 x 1,8",
        "RENAL_score": "5a",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/10mm",
        "size_mass": "2,6 x 2,5 x 2,6",
        "RENAL_score": "7xh",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/1mm",
        "size_mass": "5,8 x 4,3 x 6,2",
        "RENAL_score": "5x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/21mm",
        "size_mass": "2,9 x 3,2 x 2,6",
        "RENAL_score": "6x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/43mm",
        "size_mass": "1,4 x 1,4 x 1,5",
        "RENAL_score": "4p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/<1mm",
        "size_mass": "2,6 x 2,3 x 2,1",
        "RENAL_score": "7ph",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/33mm",
        "size_mass": "2 x 1,8 x 1,9",
        "RENAL_score": "4p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/ 20",
        "size_mass": "3,2 x 2,9 x 3,2",
        "RENAL_score": "4p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "lower/32",
        "size_mass": "3,1 x 2,9 x 2,8",
        "RENAL_score": "6a",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/28",
        "size_mass": "1,9 x 1,6 x 1,6",
        "RENAL_score": "6x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle/23",
        "size_mass": "2 x 2,5 x 2,3",
        "RENAL_score": "7p",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/ 24",
        "size_mass": "2,4 x 2,6 x 2",
        "RENAL_score": "6a",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "middle-upper/5",
        "size_mass": "3,6 x 3,7 x 4,3",
        "RENAL_score": "10a",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/ 36",
        "size_mass": "1,8 x 2 x 2,1",
        "RENAL_score": "4x",
        "BIOPSY": "CLEAR CELL GR 1"
    },
    {
        "location_distance_hilum": "upper/19",
        "size_mass": "2,2 x 2,5 x 2,4",
        "RENAL_score": "4x",
        "BIOPSY": "CLEAR CELL GR 2"
    },
    {
        "location_distance_hilum": "upper/36",
        "size_mass": "2,5 x 2,1 x 2,2",
        "RENAL_score": "4p",
        "BIOPSY": "CLEAR CELL GR 5"
    },
    {
        "location_distance_hilum": "lower/33",
        "size_mass": "19 x 19 x 2,1",
        "RENAL_score": "4x",
        "BIOPSY": "CLEAR CELL GR 6"
    },
    {
        "location_distance_hilum": "upper/25?",
        "size_mass": "2,6 x 2,5 x 2,1",
        "RENAL_score": "4a",
        "BIOPSY": "CLEAR CELL GR 7"
    },
    {
        "location_distance_hilum": "middle/25",
        "size_mass": "4,6 x 3,8 x 4,8",
        "RENAL_score": "8x",
        "BIOPSY": "CLEAR CELL GR 8"
    },
    {
        "location_distance_hilum": "middle-lower/13",
        "size_mass": "2,6 x 1,9 x 2,2",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 11"
    },
    {
        "location_distance_hilum": "middle-lower/ 14",
        "size_mass": "4,2 x 3,6 x 4,6",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 12"
    },
    {
        "location_distance_hilum": "lower/43",
        "size_mass": "3,1 x 2,5 x 4,8",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 14"
    },
    {
        "location_distance_hilum": "lower/14",
        "size_mass": "3,1 x 3,9 x 3,4",
        "RENAL_score": "4x",
        "BIOPSY": "CLEAR CELL GR 15"
    },
    {
        "location_distance_hilum": "upper/14",
        "size_mass": "2,5 x 2,7 x 2,8",
        "RENAL_score": "5x",
        "BIOPSY": "CLEAR CELL GR 16"
    },
    {
        "location_distance_hilum": "middle- upper/ 31",
        "size_mass": "3,4 x 3,5 x 2,9",
        "RENAL_score": "6p",
        "BIOPSY": "CLEAR CELL GR 17"
    },
    {
        "location_distance_hilum": "upper/26",
        "size_mass": "3,7 x 3,5 x 3,4",
        "RENAL_score": "4p",
        "BIOPSY": "CLEAR CELL GR 18"
    },
    {
        "location_distance_hilum": "middle/12",
        "size_mass": "1,7 x 1,9 x 2",
        "RENAL_score": "5a",
        "BIOPSY": "CLEAR CELL GR 20"
    },
    {
        "location_distance_hilum": "upper-middle/12",
        "size_mass": "3,7 x 3,5 x 4",
        "RENAL_score": "4a",
        "BIOPSY": "CLEAR CELL GR 21"
    },
    {
        "location_distance_hilum": "lower/38",
        "size_mass": "2,4 x 2,0 x 2,6",
        "RENAL_score": "4p",
        "BIOPSY": "CLEAR CELL GR 22"
    },
    {
        "location_distance_hilum": "middle/12",
        "size_mass": "2,6 x 2,3 x 2,1",
        "RENAL_score": "7ah",
        "BIOPSY": "CLEAR CELL GR 23"
    },
    {
        "location_distance_hilum": "upper/42",
        "size_mass": "2,9 x 2,7 x 2,7",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 24"
    },
    {
        "location_distance_hilum": "lower/12",
        "size_mass": "3,2 x 2,5 x 3,7",
        "RENAL_score": "4ah",
        "BIOPSY": "CLEAR CELL GR 25"
    },
    {
        "location_distance_hilum": "upper/34",
        "size_mass": "2,9 x 2,8 x 2,9",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 26"
    },
    {
        "location_distance_hilum": "middle-lower/26",
        "size_mass": "3,7 x 3,2 x 3,5",
        "RENAL_score": "5a",
        "BIOPSY": "CLEAR CELL GR 27"
    },
    {
        "location_distance_hilum": "lower/ 29",
        "size_mass": "2 x 2,2 x 1,9",
        "RENAL_score": "4a",
        "BIOPSY": "CLEAR CELL GR 28"
    },
    {
        "location_distance_hilum": "middle/16",
        "size_mass": "2,8 x 2,7 x 2",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 30"
    },
    {
        "location_distance_hilum": "lower/17",
        "size_mass": "2 x 1 x 2",
        "RENAL_score": "5p",
        "BIOPSY": "CLEAR CELL GR 31"
    }
]

df_main = pd.DataFrame(main_data)

# -------------------------
# B) Define the Cryoablation Results Table (df_cryo)
# -------------------------
cryo_data = [
    {
        "cryoprobes": "3 rod",
        "types_of_probes": "ROD",
        "size_Ice_ball": "2,7x1,9x3,2",
        "protection": "NO",
        "complications": "NONE"
    },
    {
        "cryoprobes": "1",
        "types_of_probes": "",
        "size_Ice_ball": "1,4 x 2,6 x 2,8 or 1,7",
        "protection": "YES/COLON SPLEEN",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "2,8 x 2,7 x 3,5",
        "protection": "NONE",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3 x 3,6 x 2",
        "protection": "NONE",
        "complications": "PNEUMOTH"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "2,7 x 2,4 x 2,8",
        "protection": "NONE",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "",
        "size_Ice_ball": "2,9 x 3 x 4,2",
        "protection": "YES/SPLEEN",
        "complications": ""
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3 x 3,8 x 3,4",
        "protection": "NO",
        "complications": "MILD HEMORRHAGE?"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,8 x 5,2 x 4,9",
        "protection": "YES/PSOAS",
        "complications": "none"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3,2 x 3,4 x 3",
        "protection": "NO",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,7 x 2,4 x 3,2",
        "protection": "NO",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "4,2 x 3,6 x 4,1",
        "protection": "NO",
        "complications": "NONE"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,8 x 4,2 x 4,9",
        "protection": "YES/COLON",
        "complications": "MILD HEMORRHAGE?"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,5 x 3,6 x 3,3",
        "protection": "YES/ COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,5 x 3,2 x 3,6",
        "protection": "YES/ COLON",
        "complications": "MILD HEMORRHAGE?"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "2ROD+1SPHERE",
        "size_Ice_ball": "3,6 x 2,9 x 3,4",
        "protection": "NO",
        "complications": "NONE?"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "2,7 x 3,7 x 3,5",
        "protection": "YES/COLON",
        "complications": ""
    },
    {
        "cryoprobes": "1",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "1,2 x 1,8 x 2",
        "protection": "YES/PSOAS",
        "complications": ""
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "4SPHERE",
        "size_Ice_ball": "3,5 x 3,3 x 3,8",
        "protection": "COLON/SPLEEN",
        "complications": "none"
    },
    {
        "cryoprobes": "5",
        "types_of_probes": "4FORCE+1ROD",
        "size_Ice_ball": "5,5 x 5,7 x 6,5",
        "protection": "YES/COLON/SPLEEN",
        "complications": "none"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,5 x 4,8 x 4",
        "protection": "HYDRO/COLON",
        "complications": "none"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3,1 x 2,9 x 2,7",
        "protection": "NO",
        "complications": "MILD HEMORRHAGE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "2ROD+1SPHERE",
        "size_Ice_ball": "2,6 x 4,4 x 3,5",
        "protection": "YES/LIVER/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3,1 x 2,5 x 3",
        "protection": "NO",
        "complications": "NONE"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,5 x 4,7 x 5",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,2 x 4 x 4",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3 x 2,5 x 2,8",
        "protection": "NO",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,4 x 3,3 x 3",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "4 x 2,4 x 3,9",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "ROD",
        "size_Ice_ball": "5,2 x 4 x 4,8",
        "protection": "YES/SPLEEN",
        "complications": "MILD HEMORRHAGE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3,7 x 3,3 x 2,8",
        "protection": "NO",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,9 x 3,3 x 2,9",
        "protection": "YES/PSOAS,RENAL VEIN",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,7 x 3,4 x 2,7",
        "protection": "YES/SPLEEN",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3 x 3,6 x 3,8",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3,1 x 2,7 x 2,4",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "FORCE",
        "size_Ice_ball": "5,2 x 4,1 x 4,9",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,6 x 2,2 x 2,1",
        "protection": "YES/PSOAS",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "FORCE",
        "size_Ice_ball": "5,2 x 4,2 x 4,8",
        "protection": "YES/PSOAS",
        "complications": "HEMORRHAGE- νοσηλεία"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "FORCE",
        "size_Ice_ball": "",
        "protection": "",
        "complications": ""
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "FORCE",
        "size_Ice_ball": "5,0 x 3,5 x 5,3",
        "protection": "YES/COLON, PSOAS",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "FORCE",
        "size_Ice_ball": "3,5 x 4,1 x 4,3",
        "protection": "YES/ COLON",
        "complications": "MILD HEMORRHAGE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3 x 4,1 x 2,9",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "ROD",
        "size_Ice_ball": "5,5 x 5,5 x 4,6",
        "protection": "NO",
        "complications": "MILD HEMORRHAGE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "ROD",
        "size_Ice_ball": "4,2 x 3,9 x 5,4",
        "protection": "YES/ COLON, PSOAS",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3,4 x 2,6 x 3,1",
        "protection": "YES/COLON",
        "complications": "HEMORRHAGE ΜΕΓΑΛΗ"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,8 x 5,3 x 6,5",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "ROD",
        "size_Ice_ball": "3,2 x 3,7 x 3,6",
        "protection": "YES/PSOAS",
        "complications": "MILD HEMORRHAGE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,8 x 2,8 x 2,9",
        "protection": "YES/COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "4,6 x 3,6 x 3,6",
        "protection": "YES/LIVER,COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "ROD",
        "size_Ice_ball": "4,2 x 3,1 x 3,6",
        "protection": "YES/LIVER,COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "3,6 x 3 x 3,5",
        "protection": "YES/SPLEEN,COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "4",
        "types_of_probes": "ROD",
        "size_Ice_ball": "4,1 x 4 x 5,2",
        "protection": "YES/COLON",
        "complications": "SUBCUTANEUS HEMATOMA / MILD HEMORRHAGE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,7 x 2,9 x 2,6",
        "protection": "YES/ COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "3",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "4,7 x 3,6 x 3,5",
        "protection": "YES/ COLON",
        "complications": "NONE"
    },
    {
        "cryoprobes": "2",
        "types_of_probes": "SPHERE",
        "size_Ice_ball": "2,3 x 33 x 2,5",
        "protection": "YES/ PSOAS",
        "complications": "NONE"
    }
]

df_cryo = pd.DataFrame(cryo_data)

# -------------------------
# Merge the two tables by index (assuming they are aligned row-by-row)
# -------------------------
df_main.index.name = "index"
df_cryo.index.name = "index"
df_merged = pd.merge(df_main, df_cryo, left_index=True, right_index=True)

# -------------------------
# Helper function to parse "size_mass" into a numeric array
# -------------------------
def parse_size(s):
    try:
        # Replace comma with dot and split on "x"
        parts = s.replace(',', '.').split('x')
        return [float(part.strip()) for part in parts]
    except:
        return None

df_merged["size_parsed"] = df_merged["size_mass"].apply(parse_size)

# -------------------------
# Streamlit App Interface
# -------------------------
st.title("Renal Cryoablation Treatment Planner")
st.markdown("""
This application matches your tumor dimensions to our reference data and provides a recommended cryoablation plan.
Please enter your tumor dimensions below.
""")

# Sidebar input for tumor dimensions
st.sidebar.header("Enter Tumor Dimensions (cm)")
inp_length = st.sidebar.number_input("Tumor Length", min_value=0.5, max_value=10.0, value=3.7)
inp_width  = st.sidebar.number_input("Tumor Width", min_value=0.5, max_value=10.0, value=3.2)
inp_height = st.sidebar.number_input("Tumor Height", min_value=0.5, max_value=10.0, value=3.0)

# When the user clicks the button, find the closest matching row
if st.sidebar.button("Find Recommended Plan"):
    user_dims = np.array([inp_length, inp_width, inp_height])
    user_sorted = np.sort(user_dims)
    user_mean = np.mean(user_dims)

    best_idx = None
    best_diff = float("inf")

    for idx, row in df_merged.iterrows():
        parsed = row["size_parsed"]
        if parsed is None or len(parsed) != 3:
            continue
        ref_dims = np.array(parsed)
        ref_sorted = np.sort(ref_dims)
        ref_mean = np.mean(ref_dims)
        # Compute difference: weighted sum of mean difference and absolute differences in sorted dimensions
        diff = abs(ref_mean - user_mean) * 2 + np.sum(np.abs(ref_sorted - user_sorted))
        if diff < best_diff:
            best_diff = diff
            best_idx = idx

    if best_idx is None:
        st.error("No matching data found. Please check your inputs or the reference data.")
    else:
        match = df_merged.loc[best_idx]
        st.header("Recommended Cryoablation Plan")
        st.write(f"**Location / Distance from Hilum:** {match['location_distance_hilum']}")
        st.write(f"**Tumor Size (Mass):** {match['size_mass']} cm")
        st.write(f"**RENAL Score:** {match['RENAL_score']}")
        st.write(f"**Biopsy Type:** {match['BIOPSY']}")
        st.write("---")
        st.subheader("Cryoablation Parameters")
        st.write(f"**Cryoprobes:** {match['cryoprobes']}")
        st.write(f"**Types of Probes:** {match['types_of_probes']}")
        st.write(f"**Estimated Ice Ball Size:** {match['size_Ice_ball']} cm")
        st.write(f"**Protection:** {match['protection']}")
        st.write(f"**Complications:** {match['complications']}")
        st.info(f"Matching difference metric: {best_diff:.2f}")

st.markdown("---")
st.write("Created by Michailidis A. for free use (demo).")
