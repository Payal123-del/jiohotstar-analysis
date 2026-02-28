import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
np.random.seed(42)


st.set_page_config(page_title="OTT Rating Dashboard", layout="wide")

# =======================
# 🎬 NETFLIX DASHBOARD
# =======================
st.header("🎬 Netflix User Rating Dashboard")

df_netflix = pd.read_excel("Netflix_Data_.xlsx")


df_netflix["Rating"] = np.random.uniform(3.8, 5.0, len(df_netflix)).round(1)
df_netflix["Year"] = pd.to_datetime(df_netflix["Month_Year"]).dt.year

year_netflix = st.selectbox("Select Netflix Year", sorted(df_netflix["Year"].unique()), key="netflix_year")

data_netflix = df_netflix[df_netflix["Year"] == year_netflix]

st.dataframe(data_netflix)

st.success(f"⭐ Highest Rating in {year_netflix} = {data_netflix['Rating'].max()}")

avg_rating_netflix = df_netflix.groupby("Year")["Rating"].mean().reset_index()

fig_netflix = px.line(
    avg_rating_netflix,
    x="Year",
    y="Rating",
    markers=True,
    title="📈 Year-wise Average Netflix Rating",
    color_discrete_sequence=["#E50914"]
)
fig_netflix.update_layout(template="plotly_dark")
st.plotly_chart(fig_netflix, use_container_width=True)

# =======================
# 📱 JIO DASHBOARD
# =======================
st.header("📱 Jio User Rating Dashboard")
df_jio = pd.read_excel("jio_data_.xlsx")
df_jio["Rating"] = np.random.uniform(3.2, 4.5, len(df_jio)).round(1)
df_jio["Year"] = pd.to_datetime(df_jio["Month_Year"]).dt.year

year_jio = st.selectbox("Select Jio Year", sorted(df_jio["Year"].unique()), key="jio_year")

data_jio = df_jio[df_jio["Year"] == year_jio]

st.dataframe(data_jio)

st.success(f"⭐ Highest Rating in {year_jio} = {data_jio['Rating'].max()}")

avg_rating_jio = df_jio.groupby("Year")["Rating"].mean().reset_index()

fig_jio = px.line(
    avg_rating_jio,
    x="Year",
    y="Rating",
    markers=True,
    title="📈 Year-wise Average Jio Rating",
    color_discrete_sequence=["#0078D7"]
)
fig_jio.update_layout(template="plotly_dark")
st.plotly_chart(fig_jio, use_container_width=True)

# =======================
# 🌟 HOTSTAR DASHBOARD
# =======================
st.header("🌟 Hotstar User Rating Dashboard")

df_hotstar = pd.read_excel("hotstar_data.xlsx")
df_hotstar["Rating"] = np.random.uniform(2.8, 4.4, len(df_hotstar)).round(1)
df_hotstar["Month_Year"] = pd.to_datetime(df_hotstar["Month_Year"])
df_hotstar["Year"] = df_hotstar["Month_Year"].dt.year

year_hotstar = st.selectbox("Select Hotstar Year", sorted(df_hotstar["Year"].unique()), key="hotstar_year")

data_hotstar = df_hotstar[df_hotstar["Year"] == year_hotstar]

st.dataframe(data_hotstar)

st.success(f"⭐ Highest Rating in {year_hotstar} = {data_hotstar['Rating'].max()}")

avg_rating_hotstar = df_hotstar.groupby("Year")["Rating"].mean().reset_index()

fig_hotstar = px.line(
    avg_rating_hotstar,
    x="Year",
    y="Rating",
    markers=True,
    title="📈 Year-wise Average Hotstar Rating",
    color_discrete_sequence=["#9B59B6"]
)
fig_hotstar.update_layout(template="plotly_dark")
st.plotly_chart(fig_hotstar, use_container_width=True)

# =======================
# 📺 JIO HOTSTAR 2025 MONTHLY DASHBOARD
# =======================
st.header("📺 Jio Hotstar 2025 Monthly Rating Dashboard")

df_jh = pd.read_excel("jiohotstar_2025_data.xlsx")
df_jh["Rating"] = np.random.uniform(3.5, 5.0, len(df_jh)).round(1)

# Rename Month Column
df_jh["Month"] = df_jh["Month_2025"]

# Month Order Fix
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
df_jh["Month"] = pd.Categorical(df_jh["Month"], categories=month_order, ordered=True)
df_jh = df_jh.sort_values("Month")

month = st.selectbox("Select Month", df_jh["Month"].unique(), key="jiohotstar_month")

data_jh = df_jh[df_jh["Month"] == month]

st.dataframe(data_jh)

st.success(f"⭐ Highest Rating in {month} = {data_jh['Rating'].max()}")

avg_rating_jh = df_jh.groupby("Month")["Rating"].mean().reset_index()

fig_jh = px.line(
    avg_rating_jh,
    x="Month",
    y="Rating",
    markers=True,
    title="📈 Month-wise Average Jio Hotstar Rating (2025)",
    color_discrete_sequence=["#00C9A7"]
)

fig_jh.update_layout(template="plotly_dark")
st.plotly_chart(fig_jh, use_container_width=True)

st.header("🏆 Overall Platform Comparison")

comparison = pd.DataFrame({
    "Platform": ["Netflix", "Jio", "Hotstar", "JioHotstar"],
    "Average Rating": [
        df_netflix["Rating"].mean(),
        df_jio["Rating"].mean(),
        df_hotstar["Rating"].mean(),
        df_jh["Rating"].mean()
    ]
})

fig_compare = px.bar(
    comparison,
    x="Platform",
    y="Average Rating",
    color="Platform",
    text_auto=".2f"
)

fig_compare.update_layout(template="plotly_dark")
st.plotly_chart(fig_compare, use_container_width=True)

#python -m streamlit run app.py