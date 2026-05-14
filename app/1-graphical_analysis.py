import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import pygal
import streamlit as st

plt.style.use("default")

plt.rcParams.update(
    {
        "axes.facecolor": "#e0f7f7",
        "figure.facecolor": "#ffffff",
        "axes.edgecolor": "#008080",
        "axes.labelcolor": "#006666",
        "xtick.color": "#006666",
        "ytick.color": "#006666",
        "grid.color": "#b2dfdb",
        "text.color": "#004c4c",
        "lines.color": "#00bcd4",
        "axes.prop_cycle": plt.cycler(
            color=["#00bcd4", "#009688", "#4dd0e1", "#00796b"]
        ),
    }
)


@st.cache_data
def load_germany_nuts1():
    """Load Germany NUTS1 shapefile from online source.
    Returns:
        gpd.GeoDataFrame: GeoDataFrame containing Germany NUTS1 geometries and attributes.
    """
    try:
        gdf = gpd.read_file("app/data/map.json")
        gdf = gdf[gdf["CNTR_CODE"] == "DE"].copy()
        return gdf
    except Exception as e:
        st.error(f"Could not load Germany NUTS1 shapefile from online source: {e}")
        return None


st.write("# Geographic Analysis")
st.write("""
Spatial Distribution of PtX Projects Across Germany (2021-2024)

Analysis at NUTS 1 (Federal States) and NUTS 3 (District) levels reveals strong regional concentration and significant disparities in project development."""
)

st.write("## Distribution of Announced Projects Across German NUTS1 Regions")

df = pd.read_csv("app/data/dist-ptx-nut1.csv")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Projects", df["Number of announced projects"].sum())
with col2:
    st.metric("Average per State", f"{df['Number of announced projects'].mean():.1f}")
with col3:
    st.metric(
        "Max Projects (State)",
        f"{df.loc[df['Number of announced projects'].idxmax(), 'State name']}",
    )

with st.spinner("Loading map data..."):
    germany_nuts1 = load_germany_nuts1()

if germany_nuts1 is None:
    st.error(
        "Unable to load map data. Please check your internet connection or try again later."
    )
else:
    germany_nuts1 = germany_nuts1.merge(
        df[["Code", "Number of announced projects", "State name"]],
        left_on="NUTS_ID",
        right_on="Code",
        how="left",
    )

    germany_nuts1["Number of announced projects"] = germany_nuts1[
        "Number of announced projects"
    ].fillna(0)

    fig, ax = plt.subplots(1, 1, figsize=(14, 16))

    germany_nuts1.plot(
        column="Number of announced projects",
        ax=ax,
        legend=True,
        linewidth=0.5,
        legend_kwds={
            "label": "Number of Announced Projects",
            "orientation": "horizontal",
            "shrink": 0.6,
            "pad": 0.05,
        },
    )

    for _, row in germany_nuts1.iterrows():
        if pd.notna(row["State name"]):
            centroid = row["geometry"].centroid
            projects = int(row["Number of announced projects"])
            ax.annotate(
                text=f"{row['State name']}\n({projects})",
                xy=(centroid.x, centroid.y),
                horizontalalignment="center",
                fontsize=8,
                fontweight="bold",
                bbox=dict(
                    boxstyle="round,pad=0.3",
                    facecolor="white",
                    alpha=0.7,
                    edgecolor="none",
                ),
            )

    ax.set_title(
        "Distribution of Announced Projects Across German NUTS1 Regions",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )
    ax.axis("off")

    st.pyplot(fig)

df_sorted = df.sort_values("Number of announced projects", ascending=True)

st.subheader("Project Distribution")

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
