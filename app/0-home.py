import streamlit as st


st.write(f"# {(translate('abstract.title'))}")

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

cols = st.columns(3)
with cols[0]:
    st.metric("📊 Projects", "1,238+")
with cols[1]:
    st.metric("📦 Products", "3")
with cols[2]:
    st.metric("🔧 Technologies", "8")

cols2 = st.columns(3)
with cols2[0]:
    st.metric("📊 Data Sources", "3")

# with cols[1]:
#     st.metric("🏛️ Federal States", "16")
# with cols[2]:
#     st.metric("📍 Districts", "107")

st.markdown("### 🎯 KEY FINDING")
st.warning("""
**By 2024, only 0.44 GW of the planned 3.38 GW capacity is operational.**

At the current trajectory, Germany will miss its 10 GW target by 2030 unless urgent action is taken to accelerate implementation.

**Implementation rate has stalled:** 85.7% (2022) → 65% (2023) → 13% (2024)
""")
