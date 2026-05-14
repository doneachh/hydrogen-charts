import pandas as pd
from plotly import graph_objects as go
import plotly.express as px
import streamlit as st

import json

st.write("# Technology and Product Analysis")

st.write("## What are projects built with?")

with open('app/data/technology.json') as f:
    technology = json.load(f)

df = pd.DataFrame(technology).T.fillna(0).reset_index()
df['index'] = df['index'].astype(int).astype(str)
df.rename(columns={'index': 'year'}, inplace=True)

fig = px.area(df, x='year', y=df.columns[1:], title='Elecrolyser Technology over time (2021-2024)')
fig.update_xaxes(type='category')
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Number of projects',
    hovermode='x unified',
)

st.plotly_chart(fig)
st.caption(
    "Compare the share of different electrolysis technologies in PtX projects in Germany from 2021 to 2024."
)

st.write("""
    PEM dominates the project landscape in every year, ranging from about one‑third to over half of all projects. ALK loses share over time, while SOEC, AEMWE and “other” electrolysis methods gradually appear as developers test more experimental options alongside the mature technologies.

    The data suggests that PEM has become the workhorse technology for PtX projects in Germany.  Its flexibility, fast response and falling stack costs make it attractive where projects need to follow variable wind and solar generation.  ALK still appears in a meaningful minority of projects, but its share declines as developers prioritise controllability and grid services over purely low upfront cost.  SOEC and AEMWE remain niche, reflecting their higher technical risk and the need for more demonstration experience.
""")

with open('app/data/product-distribution.json') as f:
    product_distribution = json.load(f)

df = pd.DataFrame(product_distribution).T.fillna(0).reset_index()
df['index'] = df['index'].astype(int).astype(str)
df.rename(columns={'index': 'year'}, inplace=True)

fig = px.area(df, x='year', y=df.columns[1:], title='Distribution of Product Output from 2021 to 2024')
fig.update_xaxes(type='category')
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Number of projects',
    hovermode='x unified',
)

st.plotly_chart(fig)
st.caption(
    "Compare the share of different PtX products in projects in Germany from 2021 to 2024."
)

st.write(
    "Across all four years, hydrogen clearly dominates the PtX product portfolio, rising from about 63% of projects in 2021 to over 83% in 2024. Synfuels and methanol appear every year but remain secondary, while methane and “no defined product yet” signal pilot and experimental projects rather than large‑scale deployment."
)

st.write("## Cumulative product picture")
st.write(
    "Cumulatively, almost four out of five PtX projects in Germany target hydrogen as their main product, with a smaller but persistent group exploring liquid e‑fuels, methanol, synthetic hydrocarbons and methane."
)

with open('app/data/total-product-distribution.json') as f:
    total_product_distribution = json.load(f)

fig = go.Figure(
    data=[go.Pie(
        labels=total_product_distribution["labels"],
        values=total_product_distribution["values"],
        hole=.3,
        hovertemplate='<b>%{label}</b><br>Share: %{value}%<extra></extra>',
    )])
fig.update_layout(
    title='Total Distribution of PtX Product Output (2021-2024)',
    legend_title='PtX Products',
)

st.plotly_chart(fig)
st.caption(
    "Compare the cumulative share of different PtX products in projects in Germany from 2021 to 2024."
)

st.write("""
The combination of PEM dominance and a strong bias toward hydrogen output suggests that German PtX deployments are optimised first for flexible, grid‑coupled H₂ production rather than for complex downstream synthesis routes. Liquid synfuels and methanol appear mainly in smaller project numbers, often in demonstration settings or targeting specific industrial or transport niches.

If this pattern continues, Germany’s near‑term PtX system will look like a hydrogen backbone with smaller satellites of methanol and e‑fuel projects attached to it. For sectors such as aviation or chemical feedstocks, this means that scaling synfuels will depend on how quickly these early, technology‑diverse pilot projects can be de‑risked and replicated.
""")
