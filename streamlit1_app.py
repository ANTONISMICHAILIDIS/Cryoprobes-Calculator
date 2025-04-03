import streamlit as st
import pandas as pd
import numpy as np

########################################
# 1. Define Our Two Tables
#    A) Main table: location/distance, size mass, cryoprobes, types_of_probes, RENAL score, etc.
#    B) Results table: cryoprobes, types_of_probes, size Ice ball, protection, complications
########################################

# A) Main Table (df_main)
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

# B) Results Table (df_cryo)
#   "cryoprobes", "types of probes", "size Ice ball", "protection", "complications"
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
    "complications": "MILD HEMORRAGE"
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
    "complications": "HEMORRAGE- νοσηλεία"
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

########################################
# 2. Parse the "size_mass" from df_main
#    so we can compare numeric dimensions
########################################
def parse_size_mass(size_str):
    # e.g. "3,5 x 3,4 x 3,9" -> [3.5, 3.4, 3.9]
    try:
        parts = size_str.lower().replace(',', '.').split('x')
        nums = [float(p.strip()) for p in parts]
        if len(nums) == 3:
            return nums
    except:
        pass
    return None

df_main["size_parsed"] = df_main["size_mass"].apply(parse_size_mass)

########################################
# 3. Merge the two tables on (cryoprobes, types_of_probes)
########################################

# Note: the column names in df_main are "cryoprobes" and "types_of_probes"
# but in df_cryo are "cryoprobes" and "types_of_probes" (we must ensure they're identical).
# If the columns differ slightly, rename them accordingly.

df_merged = pd.merge(
    df_main,
    df_cryo,
    left_on=["cryoprobes", "types_of_probes"],
    right_on=["cryoprobes", "types_of_probes"],
    how="left"  # left join, so we keep all rows from df_main
)

# Now df_merged has columns:
# location_distance_hilum, size_mass, cryoprobes, types_of_probes, RENAL_score, BIOPSY,
# size_parsed, size_Ice_ball, protection, complications

########################################
# 4. Streamlit App
########################################

st.title("Renal Cryoablation Lookup and Matching")

st.write("""
This app matches a user-input tumor size to the closest row in our table (df_main) 
and then shows the recommended approach from the merged data (including ice ball, protection, etc.).
""")

# Show the merged table (optional):
if st.checkbox("Show Merged Table"):
    st.dataframe(df_merged, use_container_width=True)

# Sidebar: user enters new tumor size
st.sidebar.header("Enter Tumor Size (cm)")
inp_length = st.sidebar.number_input("Length", min_value=0.5, max_value=10.0, value=3.7)
inp_width = st.sidebar.number_input("Width", min_value=0.5, max_value=10.0, value=3.2)
inp_height = st.sidebar.number_input("Height", min_value=0.5, max_value=10.0, value=3.0)

if st.sidebar.button("Find Closest Row"):
    user_vec = np.array([inp_length, inp_width, inp_height])
    user_mean = np.mean(user_vec)
    user_sorted = np.sort(user_vec)

    best_idx = None
    best_diff = 9999.0

    for idx, row in df_merged.iterrows():
        parsed = row["size_parsed"]
        if not parsed:
            continue
        arr = np.array(parsed)
        arr_sorted = np.sort(arr)
        arr_mean = np.mean(arr)

        diff_mean = abs(arr_mean - user_mean)
        diff_dims = np.sum(np.abs(arr_sorted - user_sorted))
        total_diff = diff_mean * 2.0 + diff_dims  # Weighted difference

        if total_diff < best_diff:
            best_diff = total_diff
            best_idx = idx

    if best_idx is None:
        st.error("No row matched (table might be empty or parse failed).")
    else:
        matched_row = df_merged.loc[best_idx]
        st.success("**Closest Match Found**")
        st.write(f"**Location/Distance Hilum**: {matched_row['location_distance_hilum']}")
        st.write(f"**Size Mass**: {matched_row['size_mass']}")
        st.write(f"**Cryoprobes**: {matched_row['cryoprobes']}")
        st.write(f"**Types of Probes**: {matched_row['types_of_probes']}")

        # from second table
        st.write(f"**Size Ice Ball**: {matched_row.get('size_Ice_ball','N/A')}")
        st.write(f"**Protection**: {matched_row.get('protection','N/A')}")
        st.write(f"**Complications**: {matched_row.get('complications','N/A')}")

        # Additional columns
        st.write(f"**RENAL Score**: {matched_row.get('RENAL_score','')}")
        st.write(f"**BIOPSY**: {matched_row.get('BIOPSY','')}")

        st.info(f"Calculated difference = {best_diff:.2f}. This row is your best match.")


st.write("---")
st.write("Created by Michailidis A. for free use (demo). Fill in your entire dataset for full coverage.")
