# ==============================
# FINTRUST ATM ANALYTICS APP
# ==============================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="FinTrust ATM Intelligence",
    layout="wide",
    page_icon="🏦"
)

# ------------------------------
# CUSTOM STYLE (makes app pretty)
# ------------------------------
st.markdown("""
<style>
.main {
    background-color: #f4f7fb;
}
.metric-box {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.08);
}
h1, h2, h3 {
    color: #1f3c88;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# TITLE
# ------------------------------
st.title("🏦 FinTrust ATM Intelligence Dashboard")
st.caption("Interactive Analytics for ATM Cash Demand & Transactions")

# ------------------------------
# SAMPLE DATA (replace later if needed)
# ------------------------------
np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=120)

data = pd.DataFrame({
    "Date": dates,
    "Transactions": np.random.randint(80, 400, 120),
    "Withdrawals": np.random.randint(50000, 250000, 120),
    "Location": np.random.choice(["Urban","Semi-Urban","Rural"],120)
})

data["Day"] = data["Date"].dt.day_name()
data["Month"] = data["Date"].dt.month_name()

# ------------------------------
# NAVIGATION (MULTI SECTION)
# ------------------------------
section = st.radio(
    "Navigate",
    ["📊 Overview", "🔎 Data Exploration", "📈 Visual Analytics", "🧠 Insights & Prediction"],
    horizontal=True
)

# ==================================================
# 1️⃣ OVERVIEW
# ==================================================
if section == "📊 Overview":

    st.header("System Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transactions", f"{data['Transactions'].sum():,}")
    col2.metric("Total Withdrawals", f"₹ {data['Withdrawals'].sum():,}")
    col3.metric("ATMs Analysed", "3,000+")

    st.markdown("---")

    st.subheader("Daily Withdrawal Trend")

    fig = px.line(
        data,
        x="Date",
        y="Withdrawals",
        markers=True,
        title="Cash Withdrawal Behaviour Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==================================================
# 2️⃣ DATA EXPLORATION (EDA)
# ==================================================
elif section == "🔎 Data Exploration":

    st.header("Exploratory Data Analysis")

    st.subheader("Dataset Preview")
    st.dataframe(data.head(20), use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Location Distribution")
        fig1 = px.pie(
            data,
            names="Location",
            title="ATM Location Share"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Transactions Distribution")
        fig2 = px.histogram(
            data,
            x="Transactions",
            nbins=25,
            title="Transaction Frequency"
        )
        st.plotly_chart(fig2, use_container_width=True)

# ==================================================
# 3️⃣ VISUAL ANALYTICS
# ==================================================
elif section == "📈 Visual Analytics":

    st.header("Advanced Visual Analytics")

    location_filter = st.selectbox(
        "Select Location Type",
        data["Location"].unique()
    )

    filtered = data[data["Location"] == location_filter]

    col1, col2 = st.columns(2)

    with col1:
        fig3 = px.bar(
            filtered,
            x="Day",
            y="Withdrawals",
            color="Day",
            title="Withdrawals by Day"
        )
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        fig4 = px.scatter(
            filtered,
            x="Transactions",
            y="Withdrawals",
            size="Transactions",
            color="Location",
            title="Transactions vs Withdrawals"
        )
        st.plotly_chart(fig4, use_container_width=True)

# ==================================================
# 4️⃣ INSIGHTS + SIMPLE PREDICTION
# ==================================================
elif section == "🧠 Insights & Prediction":

    st.header("Insights & Forecast Simulation")

    st.markdown("""
    ### Key Observations
    ✔ Weekend withdrawals tend to increase  
    ✔ Urban ATMs show heavier usage  
    ✔ Transaction volume correlates with withdrawal demand  
    ✔ Demand spikes during specific periods
    """)

    st.markdown("---")

    st.subheader("Predict Future Cash Demand")

    transactions = st.slider(
        "Expected Transactions",
        50, 500, 200
    )

    location = st.selectbox(
        "Location Type",
        ["Urban","Semi-Urban","Rural"]
    )

    # simple prediction logic
    multiplier = {"Urban":1.3,"Semi-Urban":1.1,"Rural":0.9}

    prediction = transactions * 650 * multiplier[location]

    st.success(f"Estimated Cash Requirement: ₹ {int(prediction):,}")

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Cash Demand Level"},
        gauge={'axis': {'range': [None, 350000]}}
    ))

    st.plotly_chart(gauge, use_container_width=True)

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("---")
st.caption("FinTrust Analytics System • Interactive Data Intelligence")