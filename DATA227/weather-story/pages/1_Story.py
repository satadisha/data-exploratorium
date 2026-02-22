import streamlit as st
import altair as alt
from utils.io import load_weather
from charts.charts import (
    base_theme,
    chart_hook_temp_over_time,
    chart_context_seasonality,
    chart_surprise_extremes,
    chart_explain_precip_vs_temp,
)

st.set_page_config(page_title="Story", layout="wide")

alt.themes.register("project", base_theme)
alt.themes.enable("project")

df = load_weather()

st.title("A Data Story: Seattle Weather Patterns")
st.write("**Central question:** What patterns (seasonality and extremes) show up in daily weather over time?")

st.header("1) Hook: Daily temperature over time")
st.write("Start with a simple time series to build intuition about variability and overall range.")
st.altair_chart(chart_hook_temp_over_time(df), use_container_width=True)
st.caption("Takeaway: Temperature fluctuates heavily day-to-day, suggesting strong seasonality and occasional extremes.")

st.header("2) Context: Seasonality by month")
st.write("Summarize the same signal in a way that makes month-to-month structure easy to compare.")
st.altair_chart(chart_context_seasonality(df), use_container_width=True)
st.caption("Takeaway: Summer months shift the distribution upward; winter months have lower medians and tighter ranges.")

st.header("3) Surprise: Extreme heat days")
st.write("Highlight rare events to show what the ‘tail’ of the distribution looks like, not just the average.")
st.altair_chart(chart_surprise_extremes(df), use_container_width=True)
st.caption("Takeaway: A small fraction of days drive the highest peaks—outliers that a smoothed trend can hide.")

st.header("4) Explanation: Precipitation vs temperature")
st.write("Test a plausible explanation: are the warmest days also the driest (or not)?")
st.altair_chart(chart_explain_precip_vs_temp(df), use_container_width=True)
st.caption("Takeaway: The relationship is noisy—extreme heat isn’t explained by precipitation alone, motivating subgroup exploration.")
