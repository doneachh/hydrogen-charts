import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from utils.i18n import tr, SUPPORTED_LANGS

LANG_FLAGS = {"en": "🇬🇧", "de": "🇩🇪"}

def render_language_selector():
    lang = st.radio(
        "lang",
        options=list(LANG_FLAGS.keys()),
        format_func=lambda x: LANG_FLAGS[x],
        horizontal=True,
        label_visibility="collapsed",
        key="lang"
    )
    return lang

render_language_selector()

# ######################################################################
# Abstract Section #####################################################
# ######################################################################

st.title(tr('abstract.title'))
st.subheader(tr('abstract.subtitle'))

# Metrics section for planned capacity, operational capacity, and
# ambition-implementation gap with expanders for descriptions and help text
col1, col2, col3 = st.columns(3)
with col1:
    with st.expander(tr('abstract.metrics.planned_capacity.label'), expanded=True):
        st.write(tr('abstract.metrics.planned_capacity.description'))
        st.metric(
            tr('abstract.metrics.planned_capacity.capacity_label'),
            "3.38 GW",
            chart_type="area",
        )
with col2:
    with st.expander(tr('abstract.metrics.operational_capacity.label'), expanded=True):
        st.write(tr('abstract.metrics.operational_capacity.description'))
        st.metric(
            tr('abstract.metrics.operational_capacity.capacity_label'),
            "0.44 GW",
        )
with col3:
    with st.expander(tr('abstract.metrics.ambition_impl_gap.label'), expanded=True):
        st.write(tr('abstract.metrics.ambition_impl_gap.description'))
        st.metric(
            tr('abstract.metrics.ambition_impl_gap.capacity_label'),
            "2.94 GW",
            delta="-86.9%",
            delta_color="off",
            help=tr('abstract.metrics.ambition_impl_gap.capacity_help'),
        )

# Stats section for projects, products, technologies, and data sources
cols = st.columns(3)
with cols[0]:
    st.metric(tr('abstract.stats.projects.label'), "1,238+")
with cols[1]:
    st.metric(tr('abstract.stats.products.label'), "3")
with cols[2]:
    st.metric(tr('abstract.stats.technologies.label'), "8")

cols2 = st.columns(3)
with cols2[0]:
    st.metric(tr('abstract.stats.data_sources.label'), "3")

# Key finding section with highlight and implementation rate
st.subheader(tr('abstract.key_finding.title'))
st.write(tr('abstract.key_finding.highlight'))
st.write(tr('abstract.key_finding.body'))
st.write(
    tr('abstract.key_finding.implementation_rate_label'),
    "85.7% (2022) → 65% (2023) → 13% (2024)"
)

st.divider()

# ######################################################################
# Geographic Analysis Section ##########################################
# ######################################################################
st.title(tr("geographic.title"))
st.subheader(tr("geographic.subtitle"))
st.write(tr("geographic.description"))

st.subheader(tr("geographic.distribution_section.title"))

# Load the dataset for the geographic distribution of projects
project_df = pd.read_csv("app/data/dist-ptx-nut1.csv")

# Display key statistics about the project distribution
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        tr("geographic.distribution_section.stats.total_projects.label"),
        project_df["Number of announced projects"].sum(),
    )
with col2:
    st.metric(
        tr("geographic.distribution_section.stats.average_per_state.label"),
        f"{project_df['Number of announced projects'].mean():.1f}",
    )
with col3:
    st.metric(
        tr("geographic.distribution_section.stats.max_projects_state.label"),
        f"{project_df.loc[project_df['Number of announced projects'].idxmax(), 'State name']}",
    )

project_dist_df = pd.read_csv("app/data/project-distribution.csv")

# Create a scatter map to visualize the geographic distribution of projects
fig = px.scatter_map(
    project_dist_df,
    lat="lat",
    lon="lon",
    color="projects",
    size="projects",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=15,
    zoom=4,
    template="plotly_dark",
    hover_name="NUTS_ID",
    hover_data={
        "projects": True,
        "lat": ":.2f",
        "lon": ":.2f",
    },
)
st.plotly_chart(fig)

st.subheader(tr("geographic.project_distribution_section.title"))

df_sorted = project_df.sort_values(
    "Number of announced projects",
    ascending=True,
)

# Create a horizontal bar chart to show the distribution of projects across states
fig = go.Figure(go.Bar(
    x=df_sorted["Number of announced projects"],
    y=df_sorted["State name"],
    orientation='h',
    marker=dict(
        color='mediumseagreen',
        line=dict(
            color='seagreen',
            width=1
        )
    )
))

st.plotly_chart(fig)
st.divider()

# exec(open("app/2-timeline-development.py").read())
# st.divider()

# exec(open("app/3-technology.py").read())
# st.divider()

# exec(open("app/faq.py").read())
