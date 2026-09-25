"""
process_file.py — Part 2: one file of package descriptions, uploaded.

A Streamlit app that accepts an uploaded text file with one package description
per line, shows the total for every line, and writes the parsed packages to a
JSON file in the `data/` folder — `data/packaging1.txt` in, `data/packaging1.json`
out.

New here: an uploaded file arrives as **bytes**, not text, so it has to be
decoded before it can be split into lines. And a text file usually ends with a
newline, so the last "line" is empty and must be skipped rather than parsed.

Run it:  Run and Debug -> "Streamlit Run: Current File"   (see README Reference #1)
Test it: pytest tests/test_streamlit.py -k process_file
"""

# --- The page ---------------------------------------------------------------------
#
# Less scaffolding this time. The steps are described, but which widget and which
# function does each job — and what to call the result — is now yours to work out.
# `one_package.py` is your worked example for anything structural, and README
# Reference #4 and #5 cover the two things that are new here.

import streamlit as st
import json
import os
from packaging_parser import parse_packaging, calc_total_units, get_unit

st.title("Process File of Packages")

uploaded_file = st.file_uploader("Upload package file", key="package_file")

if uploaded_file is not None:
    contents = uploaded_file.read().decode("utf-8")
    lines = contents.split('\n')

    parsed_packages = []
    total_lines_processed = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue  

        package = parse_packaging(line)
        total = calc_total_units(package)
        unit = get_unit(package)

        parsed_packages.append(package)
        total_lines_processed += 1

        st.write(f"{line} ➡️ Total 📦 Size: {total} {unit}")

    if total_lines_processed > 0:
        input_filename = uploaded_file.name 
        base_name = os.path.splitext(input_filename)[0] 
        output_path = os.path.join("data", f"{base_name}.json")

        os.makedirs("data", exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(parsed_packages, f, indent=2)

        st.success(f"{total_lines_processed} packages written to {output_path}")