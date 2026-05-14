import streamlit as st
from PIL import Image

Image.MAX_IMAGE_PIXELS = 500_000_000

st.write("# Power-to-X in Germany")



st.write("### Status Review & Analysis of the Implementation-Ambition Gap (2021-2024)")

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("Planned Capacity", expanded=True):
        st.write("All PtX projects announced between 2021 and 2024")
        st.metric("Capacity", "3.38 GW", chart_type="area")
with col2:
    with st.expander("Operational Capacity", expanded=True):
        st.write("Projects that are currently operational")
        st.metric("Capacity", "0.44 GW")
with col3:
    with st.expander("Ambition-Impl. Gap", expanded=True):
        st.write("Difference between planned and operational capacity")
        st.metric(
            "Capacity",
            "2.94 GW",
            delta="-86.9%",
            delta_color="off",
            help="Significant gap between planned and operational capacity",
        )

st.markdown("---")

cols = st.columns(3)
with cols[0]:
    st.metric("📊 Projects", "1,238+")
with cols[1]:
    st.metric("🏛️ Federal States", "16")
with cols[2]:
    st.metric("📍 Districts", "107")

cols2 = st.columns(3)
with cols2[0]:
    st.metric("📦 Products", "3")
with cols2[1]:
    st.metric("🔧 Technologies", "8")
with cols2[2]:
    st.metric("📊 Data Sources", "3")

st.markdown("---")
st.markdown("### 🎯 KEY FINDING")
st.warning("""**By 2024, only 0.44 GW of the planned 3.38 GW capacity is operational.**

At the current trajectory, Germany will miss its 10 GW target by 2030 unless urgent action is taken to accelerate implementation.

**Implementation rate has stalled:** 85.7% (2022) → 65% (2023) → 13% (2024)
""")


data = {
    "State name": [
        "Baden-Württemberg",
        "Bavaria",
        "Berlin",
        "Brandenburg",
        "Bremen",
        "Hamburg",
        "Hessen",
        "Mecklenburg-Vorpommern",
        "Lower Saxony",
        "Nordrhein-Westfalen",
        "Rheinland-Pfalz",
        "Saarland",
        "Saxony",
        "Saxony-Anhalt",
        "Schleswig-Holstein",
        "Thüringen",
    ],
    "Code": [
        "DE1",
        "DE2",
        "DE3",
        "DE4",
        "DE5",
        "DE6",
        "DE7",
        "DE8",
        "DE9",
        "DEA",
        "DEB",
        "DEC",
        "DED",
        "DEE",
        "DEF",
        "DEG",
    ],
    "projects": [8, 13, 0, 6, 9, 1, 3, 1, 19, 16, 4, 1, 6, 9, 2, 1],
}
