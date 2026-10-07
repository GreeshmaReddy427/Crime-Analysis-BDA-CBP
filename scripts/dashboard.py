import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="India Crime Analytics Dashboard",
    layout="wide"
)


# ============================================================
# PATH
# ============================================================

BASE_DIR = Path.home() / "crime_project" / "output"


# ============================================================
# LOAD IPC DATA
# ============================================================

@st.cache_data
def load_ipc():

    file = BASE_DIR / "ipc_state_year.csv"

    df = pd.read_csv(
        file,
        sep="\t",
        header=None,
        names=["StateYear", "Total_IPC"]
    )

    df[["State", "Year"]] = df["StateYear"].str.rsplit(
        ",", n=1, expand=True
    )

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Total_IPC"] = pd.to_numeric(
        df["Total_IPC"],
        errors="coerce"
    )

    return df.dropna()[[
        "State",
        "Year",
        "Total_IPC"
    ]]


# ============================================================
# LOAD PROPERTY DATA
# ============================================================

@st.cache_data
def load_property():

    file = BASE_DIR / "property_analysis.csv"

    df = pd.read_csv(
        file,
        sep="\t",
        header=None,
        names=["StateYear", "Values"]
    )

    df[["State", "Year"]] = df["StateYear"].str.rsplit(
        ",", n=1, expand=True
    )

    values = df["Values"].str.split(",", expand=True)

    df["Cases_Stolen"] = pd.to_numeric(
        values[0], errors="coerce"
    )

    df["Cases_Recovered"] = pd.to_numeric(
        values[1], errors="coerce"
    )

    df["Value_Stolen"] = pd.to_numeric(
        values[2], errors="coerce"
    )

    df["Value_Recovered"] = pd.to_numeric(
        values[3], errors="coerce"
    )

    df["Recovery_Rate"] = pd.to_numeric(
        values[4], errors="coerce"
    )

    df["Year"] = pd.to_numeric(
        df["Year"],
        errors="coerce"
    )

    return df.dropna()[[
        "State",
        "Year",
        "Cases_Stolen",
        "Cases_Recovered",
        "Value_Stolen",
        "Value_Recovered",
        "Recovery_Rate"
    ]]


# ============================================================
# LOAD AUTO THEFT DATA
# ============================================================

@st.cache_data
def load_auto():

    file = BASE_DIR / "auto_theft_analysis.csv"

    df = pd.read_csv(
        file,
        sep="\t",
        header=None,
        names=["StateYear", "Values"]
    )

    df[["State", "Year"]] = df["StateYear"].str.rsplit(
        ",", n=1, expand=True
    )

    values = df["Values"].str.split(",", expand=True)

    df["Stolen"] = pd.to_numeric(
        values[0], errors="coerce"
    )

    df["Recovered"] = pd.to_numeric(
        values[1], errors="coerce"
    )

    df["Year"] = pd.to_numeric(
        df["Year"],
        errors="coerce"
    )

    return df.dropna()[[
        "State",
        "Year",
        "Stolen",
        "Recovered"
    ]]


# ============================================================
# LOAD MURDER DATA
# ============================================================

@st.cache_data
def load_murder():

    file = BASE_DIR / "murder_analysis.csv"

    df = pd.read_csv(
        file,
        sep="\t",
        header=None,
        names=["StateYear", "Values"]
    )

    df[["State", "Year"]] = df["StateYear"].str.rsplit(
        ",", n=1, expand=True
    )

    values = df["Values"].str.split(",", expand=True)

    df["Male"] = pd.to_numeric(
        values[0], errors="coerce"
    )

    df["Female"] = pd.to_numeric(
        values[1], errors="coerce"
    )

    df["Total"] = pd.to_numeric(
        values[2], errors="coerce"
    )

    df["Year"] = pd.to_numeric(
        df["Year"],
        errors="coerce"
    )

    return df.dropna()[[
        "State",
        "Year",
        "Male",
        "Female",
        "Total"
    ]]


# ============================================================
# LOAD WOMEN DATA
# ============================================================

@st.cache_data
def load_women():

    file = BASE_DIR / "women_analysis.csv"

    df = pd.read_csv(
        file,
        sep="\t",
        header=None,
        names=["StateYear", "Values"]
    )

    df[["State", "Year"]] = df["StateYear"].str.rsplit(
        ",", n=1, expand=True
    )

    values = df["Values"].str.split(",", expand=True)

    df["Reported"] = pd.to_numeric(
        values[0], errors="coerce"
    )

    df["Chargesheeted"] = pd.to_numeric(
        values[1], errors="coerce"
    )

    df["Convicted"] = pd.to_numeric(
        values[2], errors="coerce"
    )

    df["Pending_Trial"] = pd.to_numeric(
        values[3], errors="coerce"
    )

    df["Year"] = pd.to_numeric(
        df["Year"],
        errors="coerce"
    )

    return df.dropna()[[
        "State",
        "Year",
        "Reported",
        "Chargesheeted",
        "Convicted",
        "Pending_Trial"
    ]]


# ============================================================
# LOAD ALL DATA
# ============================================================

ipc = load_ipc()
property_df = load_property()
auto = load_auto()
murder = load_murder()
women = load_women()


# ============================================================
# DATASET DICTIONARY
# ============================================================

datasets = {
    "IPC Crimes": ipc,
    "Auto Theft": auto,
    "Property Theft": property_df,
    "Murder": murder,
    "Crimes Against Women": women
}


# ============================================================
# TITLE
# ============================================================

st.title("🇮🇳 India Crime Analytics Dashboard")

st.markdown(
    """
    **Hadoop HDFS + MapReduce + Streamlit + Plotly**

    Interactive analysis of NCRB crime data.
    Use the filters in the sidebar to change the charts.
    """
)


# ============================================================
# SIDEBAR — ONLY ONE SET OF FILTERS
# ============================================================

st.sidebar.title(" Filters")

selected_dataset = st.sidebar.selectbox(
    "Select Dataset",
    list(datasets.keys())
)

df = datasets[selected_dataset]


# -----------------------------
# STATE FILTER
# -----------------------------

states = sorted(df["State"].unique())

selected_state = st.sidebar.selectbox(
    "Select State",
    ["All States"] + states
)


# -----------------------------
# YEAR FILTER
# -----------------------------

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())

selected_years = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered = df[
    (df["Year"] >= selected_years[0]) &
    (df["Year"] <= selected_years[1])
].copy()


if selected_state != "All States":

    filtered = filtered[
        filtered["State"] == selected_state
    ]


# ============================================================
# SHOW CURRENT FILTERS
# ============================================================

st.info(
    f"Dataset: **{selected_dataset}**  |  "
    f"State: **{selected_state}**  |  "
    f"Years: **{selected_years[0]} – {selected_years[1]}**"
)


# ============================================================
# NO DATA CHECK
# ============================================================

if filtered.empty:

    st.warning(
        "No data available for the selected filters."
    )

    st.stop()


# ============================================================
# IPC CRIMES
# ============================================================

if selected_dataset == "IPC Crimes":

    st.header("IPC Crime Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total IPC Crimes",
            f"{int(filtered['Total_IPC'].sum()):,}"
        )

    with col2:

        st.metric(
            "Average IPC Crimes",
            f"{int(filtered['Total_IPC'].mean()):,}"
        )

    st.markdown("---")

    # Yearly trend

    yearly = (
        filtered
        .groupby("Year", as_index=False)["Total_IPC"]
        .sum()
    )

    fig = px.line(
        yearly,
        x="Year",
        y="Total_IPC",
        markers=True,
        title="IPC Crimes Over Time"
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Total IPC Crimes",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # State chart

    state_data = (
        filtered
        .groupby("State", as_index=False)["Total_IPC"]
        .sum()
        .sort_values(
            "Total_IPC",
            ascending=False
        )
        .head(15)
    )

    fig2 = px.bar(
        state_data,
        x="State",
        y="Total_IPC",
        title="Top States by IPC Crimes"
    )

    fig2.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ============================================================
# AUTO THEFT
# ============================================================

elif selected_dataset == "Auto Theft":

    st.header(" Auto Theft Analysis")

    stolen = filtered["Stolen"].sum()
    recovered = filtered["Recovered"].sum()

    recovery_rate = (
        recovered / stolen * 100
        if stolen > 0
        else 0
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Vehicles Stolen",
            f"{int(stolen):,}"
        )

    with col2:

        st.metric(
            "Vehicles Recovered",
            f"{int(recovered):,}"
        )

    with col3:

        st.metric(
            "Recovery Rate",
            f"{recovery_rate:.2f}%"
        )

    st.markdown("---")

    yearly = (
        filtered
        .groupby("Year", as_index=False)[
            ["Stolen", "Recovered"]
        ]
        .sum()
    )

    fig = px.line(
        yearly,
        x="Year",
        y=["Stolen", "Recovered"],
        markers=True,
        title="Vehicles Stolen vs Recovered"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    state_data = (
        filtered
        .groupby("State", as_index=False)["Stolen"]
        .sum()
        .sort_values(
            "Stolen",
            ascending=False
        )
        .head(15)
    )

    fig2 = px.bar(
        state_data,
        x="State",
        y="Stolen",
        title="Top States by Auto Theft"
    )

    fig2.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ============================================================
# PROPERTY THEFT
# ============================================================

elif selected_dataset == "Property Theft":

    st.header("Property Theft Analysis")

    stolen = filtered["Cases_Stolen"].sum()
    recovered = filtered["Cases_Recovered"].sum()

    stolen_value = filtered["Value_Stolen"].sum()
    recovered_value = filtered["Value_Recovered"].sum()

    recovery_rate = (
        recovered_value / stolen_value * 100
        if stolen_value > 0
        else 0
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Cases Stolen",
            f"{int(stolen):,}"
        )

    with col2:

        st.metric(
            "Cases Recovered",
            f"{int(recovered):,}"
        )

    with col3:

        st.metric(
            "Value Recovery Rate",
            f"{recovery_rate:.2f}%"
        )

    st.markdown("---")

    yearly = (
        filtered
        .groupby("Year", as_index=False)[
            ["Cases_Stolen", "Cases_Recovered"]
        ]
        .sum()
    )

    fig = px.line(
        yearly,
        x="Year",
        y=["Cases_Stolen", "Cases_Recovered"],
        markers=True,
        title="Property Cases: Stolen vs Recovered"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    recovery = (
        filtered
        .groupby("Year", as_index=False)
        .agg(
            Value_Stolen=("Value_Stolen", "sum"),
            Value_Recovered=("Value_Recovered", "sum")
        )
    )

    recovery["Recovery_Rate"] = (
        recovery["Value_Recovered"] /
        recovery["Value_Stolen"] * 100
    )

    fig2 = px.line(
        recovery,
        x="Year",
        y="Recovery_Rate",
        markers=True,
        title="Property Value Recovery Rate"
    )

    fig2.update_layout(
        yaxis_title="Recovery Rate (%)",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ============================================================
# MURDER
# ============================================================

elif selected_dataset == "Murder":

    st.header("Murder Victim Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Male Victims",
            f"{int(filtered['Male'].sum()):,}"
        )

    with col2:

        st.metric(
            "Female Victims",
            f"{int(filtered['Female'].sum()):,}"
        )

    with col3:

        st.metric(
            "Total Victims",
            f"{int(filtered['Total'].sum()):,}"
        )

    st.markdown("---")

    yearly = (
        filtered
        .groupby("Year", as_index=False)[
            ["Male", "Female", "Total"]
        ]
        .sum()
    )

    fig = px.line(
        yearly,
        x="Year",
        y=["Male", "Female", "Total"],
        markers=True,
        title="Murder Victims Over Time"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    gender = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Victims": [
            filtered["Male"].sum(),
            filtered["Female"].sum()
        ]
    })

    fig2 = px.bar(
        gender,
        x="Gender",
        y="Victims",
        title="Male vs Female Murder Victims"
    )

    fig2.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ============================================================
# CRIMES AGAINST WOMEN
# ============================================================

elif selected_dataset == "Crimes Against Women":

    st.header("Crimes Against Women")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Cases Reported",
            f"{int(filtered['Reported'].sum()):,}"
        )

    with col2:

        st.metric(
            "Chargesheeted",
            f"{int(filtered['Chargesheeted'].sum()):,}"
        )

    with col3:

        st.metric(
            "Convicted",
            f"{int(filtered['Convicted'].sum()):,}"
        )

    with col4:

        st.metric(
            "Pending Trial",
            f"{int(filtered['Pending_Trial'].sum()):,}"
        )

    st.markdown("---")

    yearly = (
        filtered
        .groupby("Year", as_index=False)[
            [
                "Reported",
                "Chargesheeted",
                "Convicted",
                "Pending_Trial"
            ]
        ]
        .sum()
    )

    fig = px.line(
        yearly,
        x="Year",
        y=[
            "Reported",
            "Chargesheeted",
            "Convicted",
            "Pending_Trial"
        ],
        markers=True,
        title="Crimes Against Women Over Time"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    state_data = (
        filtered
        .groupby("State", as_index=False)["Reported"]
        .sum()
        .sort_values(
            "Reported",
            ascending=False
        )
        .head(15)
    )

    fig2 = px.bar(
        state_data,
        x="State",
        y="Reported",
        title="Top States by Reported Cases"
    )

    fig2.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ============================================================
# FILTERED DATA TABLE
# ============================================================

st.markdown("---")

st.subheader("Filtered Data")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "India Crime Analytics Dashboard | "
    "Hadoop HDFS + MapReduce + Streamlit + Plotly"
)
