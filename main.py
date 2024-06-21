import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache
def load_data():
    df = sns.load_dataset("tips")
    return df


tips = load_data()

st.sidebar.title("YDL 2024 Sidebar!")
st.sidebar.write("Hello, YDL!")

smokers = st.sidebar.checkbox("Smokers only")

days = list(tips["day"].unique())
day_choice = st.sidebar.multiselect(
    "Day",
    days,
    days,
)

time_choice = st.sidebar.selectbox(
    "Time",
    list(tips["time"].unique()),
)

if smokers:
    tips = tips[tips["smoker"] == "Yes"]

tips = tips[tips["day"].isin(day_choice)]

tips = tips[tips["time"] == time_choice]

top_n = st.sidebar.slider("Top n", 1, len(tips), len(tips))

a = st.sidebar.slider("A", 1, 10, 5)
b = st.sidebar.slider("B", 1, 10, 5)

st.markdown(f"${a} + {b} = {a+b}$")
st.markdown(f"${a} ^ {b} = {a**b}$")

st.write("This is a simple example of a Streamlit app.")

st.write("Here is a histplot of the total bill.")
fig = plt.figure()
plt.title("Total Bill")
sns.histplot(tips["total_bill"])
st.pyplot(fig)

# draw a plot of total bill vs tip
st.write("Here is a scatter plot of total bill vs tip.")
fig = plt.figure()
plt.title("Total Bill vs Tip")
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="smoker")
st.pyplot(fig)

# show the data (head)
st.write("Here is the data.")
if top_n > 10:
    st.write("Please select a smaller value for top_n.")
else:
    st.write(tips.head(top_n))
