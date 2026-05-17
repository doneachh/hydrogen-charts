import PIL.Image as Image
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

import json

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

# ######################################################################
# Timeline & Development Section #######################################
# ######################################################################

st.title(tr("temporal.title"))

years = ["2021", "2022", "2023", "2024"]

# Create a line chart to show the evolution of planned vs implemented
# capacity over the years
fig = go.Figure()
fig.update_layout(title=tr("temporal.capacity_chart.chart_title"))
fig.update_xaxes(type='category')
fig.add_trace(go.Scatter(
    x=years,
    y=[0.08549, 0.31729, 0.32927, 0.62110],
    name = tr("temporal.capacity_chart.legend.planned"),
))
fig.add_trace(go.Scatter(
    x=years,
    y=[0.01830, 0.09665, 0.24047, 0.38076],
    name=tr("temporal.capacity_chart.legend implemented"),
))

st.plotly_chart(fig)
st.caption(tr("temporal.capacity_chart.caption"))

st.subheader(tr("temporal.project_status_section.title"))
st.write(tr("temporal.project_status_section.description"))

# Create expanders for each year to show insights about project status and trends
with st.expander(tr("temporal.project_status_section.yearly_accordions.2021.label"), expanded=True):
    st.write(tr("temporal.project_status_section.yearly_accordions.2021.insight"))
with st.expander(tr("temporal.project_status_section.yearly_accordions.2022.label"), expanded=True):
    st.write(tr("temporal.project_status_section.yearly_accordions.2022.insight"))
with st.expander(tr("temporal.project_status_section.yearly_accordions.2023.label"), expanded=True):
    st.write(tr("temporal.project_status_section.yearly_accordions.2023.insight"))
with st.expander(tr("temporal.project_status_section.yearly_accordions.2024.label"), expanded=True):
    st.write(tr("temporal.project_status_section.yearly_accordions.2024.insight"))

st.subheader(tr("temporal.implementation_rate_section.title"))
st.write(tr("temporal.implementation_rate_section.description"))

# Create a bar chart to show the implementation rate evolution over the years
fig = go.Figure(data=[go.Bar(
    x=list(range(2021, 2025)),
    y=[26.7, 85.7, 64.7, 66.7],
    marker_color=['crimson', 'forestgreen','lightslategray', 'lightslategray']
)])
fig.update_layout(title_text=tr("temporal.implementation_rate_section.chart.title"))

st.plotly_chart(fig)
st.caption(tr("temporal.implementation_rate_section.chart.caption"))

st.write(tr("temporal.implementation_rate_section.conclusion"))

st.divider()

# ######################################################################
# Technology & Product Distribution Section ############################
# ######################################################################

st.title(tr("technology.title"))

st.subheader(tr("technology.electrolyser_section.title"))

# Load the dataset for the distribution of electrolyser technologies
# over time and create an area chart to visualize the trends and insights

with open('app/data/technology.json') as f:
    technology = json.load(f)

# Transform the technology data into a DataFrame suitable for plotting
df = pd.DataFrame(technology).T.fillna(0).reset_index()
df['index'] = df['index'].astype(int).astype(str)
df.rename(columns={'index': 'year'}, inplace=True)

# Create an area chart to show the distribution of electrolyser
# technologies over time
fig = px.area(
    df,
    x='year',
    y=df.columns[1:],
    title=tr("technology.electrolyser_section.chart.title"),
)
fig.update_xaxes(type='category')
fig.update_layout(
    xaxis_title=tr("technology.electrolyser_section.chart.y_axis_label"),
    yaxis_title=tr("technology.electrolyser_section.chart.x_axis_label"),
    legend_title=tr("technology.electrolyser_section.chart.legend_label"),
    hovermode='x unified',
)

st.plotly_chart(fig)
st.caption(tr("technology.electrolyser_section.chart.caption"))

st.write(tr("technology.electrolyser_section.insights.overview"))
st.write(tr("technology.electrolyser_section.insights.deep_dive"))

# Load the dataset for the distribution of PtX products over time and
# create an area chart to visualize the trends and insights
with open('app/data/product-distribution.json') as f:
    product_distribution = json.load(f)

# Transform the product distribution data into a DataFrame suitable
#for plotting
df = pd.DataFrame(product_distribution).T.fillna(0).reset_index()
df['index'] = df['index'].astype(int).astype(str)
df.rename(columns={'index': 'year'}, inplace=True)

# Create an area chart to show the distribution of PtX products over time
fig = px.area(
    df,
    x='year',
    y=df.columns[1:],
    title=tr("technology.product_output_section.chart.title"),
)
fig.update_xaxes(type='category')
fig.update_layout(
    xaxis_title=tr("technology.product_output_section.chart.x_axis_label"),
    yaxis_title=tr("technology.product_output_section.chart.y_axis_label"),
    legend_title=tr("technology.product_output_section.chart.legend_label"),
    hovermode='x unified',
)

st.plotly_chart(fig)
st.caption(tr("technology.product_output_section.chart.caption"))

st.write(tr("technology.product_output_section.insight"))

st.subheader(tr("technology.cumulative_product_section.title"))
st.write(tr("technology.cumulative_product_section.description"))

# Load the dataset for the cumulative distribution of PtX products and
# create a pie chart to visualize the overall product landscape and insights
with open('app/data/total-product-distribution.json') as f:
    total_product_distribution = json.load(f)

# Create a pie chart to show the cumulative distribution of PtX products
fig = go.Figure(
    data=[go.Pie(
        labels=total_product_distribution["labels"],
        values=total_product_distribution["values"],
        hole=.3,
        hovertemplate='<b>%{label}</b><br>Share: %{value}%<extra></extra>',
    )])
fig.update_layout(
    title=tr("technology.cumulative_product_section.chart.title"),
    legend_title=tr("technology.cumulative_product_section.chart.legend_label"),
)

st.plotly_chart(fig)
st.caption(tr("technology.cumulative_product_section.chart.caption"))

st.write(tr("technology.cumulative_product_section.insights.overview"))
st.write(tr("technology.cumulative_product_section.insights.outlook"))

st.divider()

# ######################################################################
# FAQ Section #########################################################
# ######################################################################

st.title(tr("faq.title"))

with st.expander(tr("faq.questions.what_is_ptx.question")):
    st.write(tr("faq.questions.what_is_ptx.answer"))

    image_caption = "Image source: Birett, F., Goppel, G., & Toperngpong, F. (2024). PtX - Die Zukunft der Energie im Wasserstoffatlas (Version 1). Zenodo. https://doi.org/10.5281/zenodo.13960175"
    image_path = Image.open("app/files/ptx.jpg")
    st.image(image_path, caption=image_caption, width="content")

    # image_url = "https://zenodo.org/records/13960175/files/PTX%20_%20Die%20Zukunft%20der%20Energie%20groß.jpg?download=1"
    # st.image(image_url, caption=image_caption, width="content")

with st.expander(tr("faq.questions.why_it_matters.question")):
    st.write(tr("faq.questions.why_it_matters.answer"))

# with st.expander("## Electrolyser Technologies"):
#     st.image(
#         "app/files/technologies.png",
#         caption="Different electrolysis technologies used in PtX projects in Germany, ALK vs PEM vs SOEC. - Image generated by Google DeepMind's Nano Banana Pro model via Gemini 3 Pro (Feb 2026).",
#     )

with st.expander(tr("faq.questions.technical_barriers.question")):
    confusion_matrix = pd.DataFrame(
        {
            tr("faq.questions.technical_barriers.table.col_barrier_type"): [
                tr("faq.questions.technical_barriers.table.rows.1.label"),
                tr("faq.questions.technical_barriers.table.rows.2.label"),
                tr("faq.questions.technical_barriers.table.rows.3.label"),
            ],
            tr("faq.questions.technical_barriers.table.col_qualitative_weight"): [
                tr("faq.questions.technical_barriers.table.rows.1.weight"),
                tr("faq.questions.technical_barriers.table.rows.2.weight"),
                tr("faq.questions.technical_barriers.table.rows.3.weight"),
            ],
        },
    )
    st.table(confusion_matrix.reset_index(drop=True))

    st.write(tr("faq.questions.technical_barriers.paragraphs.interaction"))
    st.write(tr("faq.questions.technical_barriers.paragraphs.pem_scaling"))

    # st.image(
    #     "app/files/electrolyser-stack.png",
    #     caption="Schematic of a PEM electrolyser stack, showing the key components and their functions. - Image generated by Google DeepMind's Nano Banana Pro model via Gemini 3 Pro (Feb 2026).",
    # )

    st.write(tr("faq.questions.technical_barriers.paragraphs.grid_stress"))

with st.expander(tr("faq.questions.financing_barriers.question")):
    
    for i in range(1, 7):
        bullet = tr(f"faq.questions.financing_barriers.bullet_points.{i}")
        st.markdown(f"- {bullet}")

    st.write(tr("faq.questions.financing_barriers.paragraphs.financial_close"))
    st.write(tr("faq.questions.financing_barriers.paragraphs.pattern"))
    st.write(tr("faq.questions.financing_barriers.paragraphs.hard_stop"))
