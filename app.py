import streamlit as st

st.set_page_config(page_title="How Many Data Centers Does the World Need?", layout="centered")

st.markdown(
    """
    <style>
    [data-testid="stMetricValue"] { font-size: 3rem; }
    [data-testid="stMetricLabel"] p { font-size: 1.2rem; }
    .compare { font-size: 1.8rem; font-weight: 600; margin-top: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("How Many Data Centers Does the World Need?")

# --- The world today ---
st.header("The world today (real numbers)")
c1, c2 = st.columns(2)
c1.metric("Total data centers", "~11,800")
c1.caption("US ~5,400")
c2.metric("Hyperscale data centers", "1,360")
c3, c4 = st.columns(2)
c3.metric("Total capacity", "~100 GW")
c4.metric("World population", "8.2 billion")

st.divider()

# --- Calculator ---
st.header("Calculator")
people_bn = st.slider("People to give AI to (billions)", 0.5, 8.2, 8.2, 0.1)

LEVELS = {
    "Light (2 watts per person: chat, translation, study)": 2,
    "Standard (10 watts)": 10,
    "Heavy (25 watts: rich-country level)": 25,
}
level = st.radio("How much AI per person", list(LEVELS.keys()), index=1)
watts = LEVELS[level]

# --- Results ---
CENTER_MW = 100
COST_PER_GW_BN = 12
TODAY_AI_GW = 40

gw = people_bn * 1e9 * watts / 1e9          # watts -> GW
centers = gw * 1000 / CENTER_MW
cost_bn = gw * COST_PER_GW_BN
times = gw / TODAY_AI_GW

st.header("Results")
r1, r2 = st.columns(2)
r1.metric("AI power needed", f"{gw:,.0f} GW")
r2.metric("Big AI data centers needed", f"{centers:,.0f}")
st.caption("1 center = 100 MW")
st.metric("Building cost", f"${cost_bn:,.0f} billion  (${cost_bn / 1000:,.1f} trillion)")
st.caption("At $12 billion per GW")

st.markdown(
    f'<div class="compare">That is about {times:,.1f} times today\'s AI capacity (40 GW).</div>',
    unsafe_allow_html=True,
)

st.divider()
st.caption("Rough estimates for thinking, not engineering numbers.")
