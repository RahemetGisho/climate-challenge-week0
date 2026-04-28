import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="Climate Insights | COP32",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    file_path = "../data/all_countries_integrated.csv"
    if not os.path.exists(file_path):
        st.error(f"Dataset not found at {file_path}")
        st.stop()
    df = pd.read_csv(file_path)
    df['DATE'] = pd.to_datetime(df['DATE'])
    # Standardize column names
    df.columns = [c.upper() if c.lower() == 'date' else c for c in df.columns]
    return df

df = load_data()

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/earth-element.png", width=80)
    st.title("Control Center")
    st.markdown("---")
    
    selected_countries = st.multiselect(
        "Select Countries", 
        options=sorted(df['Country'].unique()), 
        default=sorted(df['Country'].unique())
    )
    
    year_range = st.slider(
        "Observation Period", 
        int(df['DATE'].dt.year.min()), 
        int(df['DATE'].dt.year.max()), 
        (2015, 2026)
    )

    metadata_cols = ['DATE', 'COUNTRY', 'YEAR', 'DOY', 'MONTH', 'DAY']
    available_vars = [col for col in df.columns if col.upper() not in metadata_cols]
    
    selected_var = st.selectbox(
        "Select Variable to Analyze",
        options=available_vars,
        index=0 
    )
    
    st.info(f"💡 **Tip:** Analyzing **{selected_var}**. Switch variables to see regional distributions.")

mask = (df['Country'].isin(selected_countries)) & \
       (df['DATE'].dt.year >= year_range[0]) & \
       (df['DATE'].dt.year <= year_range[1])
filtered_df = df[mask]

st.title("Regional Climate Vulnerability Dashboard")
st.markdown(f"**Comparing {selected_var} across selected regions ({year_range[0]} - {year_range[1]})**")

m_col1, m_col2, m_col3, m_col4 = st.columns(4)
with m_col1:
    avg_val = filtered_df[selected_var].mean()
    st.metric(f"Avg {selected_var}", f"{avg_val:.2f}")
with m_col2:
    max_val = filtered_df[selected_var].max()
    st.metric(f"Max {selected_var}", f"{max_val:.2f}", delta="Peak")
with m_col3:
    min_val = filtered_df[selected_var].min()
    st.metric(f"Min {selected_var}", f"{min_val:.2f}")
with m_col4:
    st.metric("Total Records", f"{len(filtered_df):,}")

st.divider()

col1, col2 = st.columns([3, 2]) 

with col1:
    st.subheader(f"📈 {selected_var} Time-Series Trend")
    trend_df = filtered_df.groupby(['Country', pd.Grouper(key='DATE', freq='ME')])[selected_var].mean().reset_index()
    
    fig_line = px.line(
        trend_df, x='DATE', y=selected_var, color='Country',
        labels={selected_var: f'{selected_var} Avg', 'DATE': 'Timeline'},
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig_line.update_layout(hovermode="x unified", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig_line, width='stretch')

with col2:
    st.subheader(f"📊 {selected_var} Statistical Spread")
    fig_box = px.box(
        filtered_df, x='Country', y=selected_var, color='Country',
        labels={selected_var: f'{selected_var} Value'},
        template="plotly_white",
        points="outliers" # Show extreme events as dots
    )
    fig_box.update_layout(showlegend=False)
    st.plotly_chart(fig_box, width='stretch')

with st.expander("📊 View Detailed Statistical Summary"):
    st.write(f"Breakdown of **{selected_var}** by Country:")
    summary_df = filtered_df.groupby('Country')[selected_var].agg(['mean', 'std', 'min', 'max']).round(3)
    st.dataframe(summary_stats := summary_df, use_container_width=True)

    top_country = summary_df['mean'].idxmax()
    st.success(f"**Insight:** {top_country} shows the highest average **{selected_var}** in this period.")