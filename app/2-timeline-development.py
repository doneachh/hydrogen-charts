import plotly.graph_objects as go
import pygal
import streamlit as st

st.write("# Temporal Trends & Project Lifecycle")

# st.write("## How project status evolves over time")
# st.write("""
#     From 2021 to 2024, PtX projects in Germany move only slowly from early ideas into real infrastructure. Each year’s dataset shows many new announcements, but a large share remains stuck in concept, feasibility, or demo stages.
#     In 2021, 55 projects are tracked; only 5 reach the operational stage while 10 remain in feasibility studies, and almost 77% of announced capacity (65.95 MW of 85.5 MW) is still in feasibility by year end. This translates into a same‑year realisation rate of about 21.4% for capacity (0.0183 GW implemented out of 0.08549 GW planned.
#     By 2022, the picture improves for the small 2022 cohort: of the 16 projects evaluated in detail, roughly 85.7% reach implementation stages over time, but many do not disclose robust capacity figures. In capacity terms, 2022 sees 0.31729 GW planned and only 0.09665 GW realised in that year, corresponding to a same‑year realisation rate of 30.5% and covering just 7.7% of the 1.25 GW average annual additions needed for the 10 GW target.
#     The 2023 cohort is larger: 85 projects are analysed, with 34 coming only from the 2023 dataset, and project counts rise by about 36% compared to 2022. Implementation looks strong for the subset of 34 projects examined closely, where 64.7% progress to implementation, and in capacity terms 240.47 MW is realised, equal to 17.43% of the 1.38 GW/year required to reach 10 GW by 2030.
#     For 2024, 85 projects are again tracked, with 30 appearing only in the 2024 dataset; here 66.7% of these 30 projects reach implementation stages (FID, under construction, or operational). At the capacity level, 2024 stands out: 380.76 MW is realised, corresponding to 61.3% of that year’s planned 621.1 MW capacity and about 22.8% of the 1.67 GW/year required for the 2030 goal.
#     """)

line_chart = pygal.Line(style=pygal.style.TurquoiseStyle)
line_chart.title = "Annual Capacity - Ambition vs Implementation (2021-2024)"
line_chart.x_labels = [2021, 2022, 2023, 2024]
line_chart.add("Planned cap. GW", [0.08549, 0.31729, 0.32927, 0.62110])
line_chart.add("Implemented cap. GW", [0.01830, 0.09665, 0.24047, 0.38076])
render_line_chart = line_chart.render()

st.components.v1.html(render_line_chart, height=520)
st.caption(
    "Compare annulal planned and implemented PtX capacity in Germany from 2021 to 2024."
)

st.write("## Project status over time")
st.write(
    "Projects status defines six lifecycle stages: concept, feasibility, demo, FID, under construction, and operational."
)

with st.expander("2021 Projects", expanded=True):
    st.write(
        "For 2021 projects, about 77.1% of announced capacity stays in feasibility; only a modest share reaches FID, construction, or operation."
    )

with st.expander("2022 Projects", expanded=True):
    st.write(
        "For 2022 projects, concept plus feasibility still dominate (around 220 MW out of 317.29 MW), but there is a visible increase in FID and under‑construction capacity."
    )

with st.expander("2023 Projects", expanded=True):
    st.write(
        "For 2023 projects, FID capacity peaks at 181 MW and under‑construction reaches 55 MW, while operational capacity begins to appear at 4.47 MW."
    )

with st.expander("2024 Projects", expanded=True):
    st.write(
        "For 2024 projects, total tracked capacity reduces to 169.95 MW, with 118 MW in FID and 148.76 MW under construction, and 39 MW already operational; concept and feasibility categories shrink sharply."
    )

st.write("## Implementation rate")
st.write(
    "Base on projects counts and defines an implementation rate as the sahre of projects thah have moved into implementation stages"
)


colors = ['crimson', 'forestgreen','lightslategray', 'lightslategray']

fig = go.Figure(data=[go.Bar(
    x=list(range(2021, 2025)),
    y=[26.7, 85.7, 64.7, 66.7],
    marker_color=colors
)])
fig.update_layout(title_text='Implementation rate evolution (in %)')

st.plotly_chart(fig)

st.caption(
    "Despite this improvement, the capacities behind many projects are modest and a large part of national ambition remains concentrated in early‑stage, high‑capacity projects that do not progress at the same speed"
)

st.write("""
    Looking at the timelines from 2021 to 2024, a clear pattern emerges: PtX projects in Germany are easy to announce, but hard to build.
    """)

    # Early years are dominated by feasibility studies 77% of 2021 capacity remains stuck there and only a thin slice reaches construction or operation.
    # By 2023 and 2024, more capacity flows into FID and under‑construction stages, and annual realised capacity rises from 18.3 MW in 2021 to 380.76 MW in 2024.  At the same time, announced capacities for later years spike to more than 1.2 GW before being revised down to 621.1 MW in the 2024 dataset because many projects are delayed, re‑scaled, or dropped.
    # This mismatch between fast‑growing ambition and slower implementation is what the thesis describes as the ambition–implementation gap.  Germany’s target of 10 GW by 2030 requires sustained annual additions above 1 GW, but realised capacity in 2024 still reaches only 22.8% of that benchmark.
    # """)
