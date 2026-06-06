import streamlit as st
import pandas as pd
import plotly.express as px

# MUST be first Streamlit command
st.set_page_config(
    page_title="Titanic AI Dashboard",
    page_icon="🚢",
    layout="wide"
)

st.markdown(
    """
    <style>

    /* ===== GLOBAL DARK BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #b3e5ff, #80d8ff, #4fc3f7, #29b6f6);
    background-size: 400% 400%;
    animation: oceanWave 10s ease infinite;
}

/* Ocean wave animation */
@keyframes oceanWave {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

    /* ===== GLASS CARD STYLE ===== */
    div.block-container {
        padding: 2rem;
    }

    .glass {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 20px;
    }

    /* ===== SIDEBAR GLASS EFFECT ===== */
    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* ===== HEADINGS ===== */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 600;
    }

    /* ===== BUTTONS ===== */
    .stButton>button {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
    }

    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.02);
        transition: 0.2s;
    }

    /* ===== DATAFRAME GLASS LOOK ===== */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
    }
    [data-testid="stHeader"] {
    background: transparent;
}
@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.05);}
    100% {transform: scale(1);}
}

    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("🚢 Titanic AI Dashboard")


page = st.sidebar.radio(
    "Navigate:",
    ["🏠 Overview", "📊 Analysis", "💡 Insights"]
)

# Load Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Title
# st.title("🚢 Titanic Data Storytelling App")
st.markdown("""
<h1 style='text-align:center;
color:#FF6F00;
animation: pulse 2s infinite;'>
🚢 Titanic Data Storytelling App
</h1>
""", unsafe_allow_html=True)


st.subheader("✨ Exploring Survival Patterns with Data")

st.snow()

# Dataset Introduction
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.header("📖 Dataset Introduction")

st.write("""
The Titanic dataset contains information about passengers who traveled on the Titanic ship.

This dataset includes:
- Passenger Age
- Gender
- Passenger Class
- Ticket Fare
- Survival Status

The objective is to understand what factors affected passenger survival.
""")

# Dataset Preview

st.markdown("## 📊 Dataset Preview")
st.info("Below is a preview of the dataset used for analysis")

st.dataframe(df.head())

st.markdown('</div>', unsafe_allow_html=True)

# Dataset Shape
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.header("📏 Dataset Size")

st.write("Rows and Columns:", df.shape)
st.markdown('</div>', unsafe_allow_html=True)

# Missing Values
st.header("🧹 Missing Value Analysis")

st.write(df.isnull().sum())
# -----------------------------
# DATA CLEANING
# -----------------------------
# Drop Cabin column (too many missing values)
df = df.drop("Cabin", axis=1)

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop duplicate rows
df = df.drop_duplicates()

st.header("🧼 After Cleaning Data Info")



st.write("Missing values after cleaning:")
st.write(df.isnull().sum())
import plotly.express as px

st.header("📊 Survival Count Analysis")
st.markdown('<div class="glass">', unsafe_allow_html=True)

fig1 = px.histogram(
    df,
    x="Survived",
    color="Survived",
    title="Survival Count (0 = Not Survived, 1 = Survived)"
)

st.plotly_chart(fig1, use_container_width=True)

st.write("""
### Observation:
Most passengers did not survive the Titanic disaster.
The number of deaths is higher than survival count.
""")
st.markdown('</div>', unsafe_allow_html=True)
st.header("👩‍🦰 Gender vs Survival Analysis")

fig2 = px.histogram(
    df,
    x="Sex",
    color="Survived",
    barmode="group",
    title="Survival Based on Gender"
)
st.plotly_chart(fig2, use_container_width=True)
st.write("""
### Observation:
Females had a much higher survival rate compared to males.
This shows that gender played an important role in survival.
""")
st.header("🎟️ Passenger Class vs Survival")

fig3 = px.histogram(
    df,
    x="Pclass",
    color="Survived",
    barmode="group",
    title="Survival Based on Passenger Class (1 = High Class, 3 = Low Class)"
)
st.plotly_chart(fig3, use_container_width=True)
st.write("""
### Observation:
Passengers in 1st class had the highest survival rate.
Passengers in 3rd class had the lowest survival rate.
This shows that passenger class strongly affected survival chances.
""")
st.header("🎂 Age Distribution of Passengers")

fig4 = px.histogram(
    df,
    x="Age",
    nbins=30,
    title="Passenger Age Distribution"
)

st.plotly_chart(fig4, use_container_width=True)
st.write("""
### Observation:
Most passengers were between 20 and 40 years old.
There were fewer children and elderly passengers.
""")
st.header("💰 Fare Distribution of Passengers")

fig5 = px.box(
    df,
    y="Fare",
    title="Fare Distribution (Ticket Prices)"
)

st.plotly_chart(fig5, use_container_width=True)
st.write("""
### Observation:
Most passengers paid low fares.
A few passengers paid very high fares, which shows class differences.
""")
st.header("📌 Final Insights")

st.write("""
1. Female passengers had higher survival rates compared to males.
2. First-class passengers had better chances of survival.
3. Most passengers were between 20–40 years old.
4. Ticket fares varied widely, showing economic differences.
5. Survival was strongly influenced by gender and passenger class.
""")
st.header("🏁 Conclusion")

st.success("""
The Titanic dataset analysis shows that survival was not random.

Key factors such as gender, passenger class, and socio-economic status played a major role.

Women and upper-class passengers had higher survival chances compared to others.
""")
