"""
one_package.py — Part 1: one package description, typed in.

A Streamlit app that asks for a single package description, parses it with the
`packaging_parser` module, and shows each level of packaging plus the total number of
units inside.

This is the smallest possible Streamlit app that does real work, and it exists to
teach one thing: a Streamlit script runs **top to bottom on every interaction**.
When the page first opens, the text box is empty — and your code still runs. So
the work has to sit behind a guard: only parse when there is something to parse.

Run it:  Run and Debug -> "Streamlit Run: Current File"   (see README Reference #1)
Test it: pytest tests/test_streamlit.py -k one_package
"""

import streamlit as st
from packaging_parser import calc_total_units, get_unit, parse_packaging

# --- The page ---------------------------------------------------------------------
#
# These two lines are GIVEN to you, in this app only. Read them: st.title draws the
# heading, and st.text_input draws the box AND RETURNS whatever is in it. On the
# very first run, before anyone has typed, that is an empty string — and the rest
# of this script runs anyway. See README Reference #2 and #3.

st.title("Process One Package")

package_data = st.text_input(
    "Enter package data:",
    key="package_data",
    placeholder="12 eggs in 1 carton / 3 cartons in 1 box",
)

# --- The work ---------------------------------------------------------------------
if package_data:
    package = parse_packaging(package_data)

    total = calc_total_units(package)
    unit = get_unit(package)

    for level in package:
        for name, quantity in level.items():
            st.info(f"{name} ➡️ {quantity}")

    st.success(f"Total 📦 Size: {total} {unit}")
