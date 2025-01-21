import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
@st.cache_data
def load_data():
    hour_df = pd.read_csv("https://raw.githubusercontent.com/Flytomarsz/Bike-Sharing-System-Analysis/refs/heads/main/Dashboard/hour.csv")
    hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])
    return hour_df

hour_df = load_data()

# Month names mapping
month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

# Sidebar filters
st.sidebar.header("Bike Sharing Analysis Dashboard")
selected_month = st.sidebar.selectbox(
    "Select Month",
    options=range(1, 13),
    format_func=lambda x: month_names[x]
)

# Filter data by year (2012) and selected month
filtered_df = hour_df[(hour_df["yr"] == 1) & (hour_df["mnth"] == selected_month)]

# Total users calculation
total_casual = filtered_df["casual"].sum()
total_registered = filtered_df["registered"].sum()

# Display total counts
st.subheader("Total Users")
col1, col2 = st.columns(2)  # Creating two columns
with col1:
    st.metric("Total Casual Users", total_casual)
with col2:
    st.metric("Total Registered Users", total_registered)

# Filter data by time and weekday
def filter_by_time_and_weekday(df, start_hour, end_hour):
    return df[(df["hr"] >= start_hour) & (df["hr"] <= end_hour) & (df["weekday"] <= 5)]

df_filtered_time = filter_by_time_and_weekday(filtered_df, 9, 17)

# Seasonal percentage calculation (based on filtered data)
df_seasonal = filtered_df.groupby("season")[["casual", "registered"]].sum().reset_index()
if not df_seasonal.empty:
    df_seasonal["percentage"] = (df_seasonal["registered"] / df_seasonal["registered"].sum()) * 100

# Pie Chart: User's Segmentation
st.write(f"### Question 1: How is the user's segmentation in {month_names[selected_month]}/2012?")

labels = ["Casual Users", "Registered Users"]
sizes = [total_casual, total_registered]
colors = ["#b392ac", "#735d78"]

fig, ax = plt.subplots(figsize=(7, 7))
plt.style.use("fivethirtyeight")
ax.pie(
    sizes,
    labels=labels,
    autopct="%.1f%%",
    colors=colors,
    startangle=140,
    wedgeprops={"edgecolor": "white"},
)
ax.set_title(f"User's Segmentation in {month_names[selected_month]}/2012")

st.pyplot(fig)
st.write("### User's Segmentation")
st.write(f"- **Casual Users**: {total_casual} ({(total_casual / (total_casual + total_registered)) * 100:.1f}%)")
st.write(f"- **Registered Users**: {total_registered} ({(total_registered / (total_casual + total_registered)) * 100:.1f}%)")

# Line Chart: Bike Rental Demand During Rush Hours
st.write(f"### Question 2: How is the impact of rush hours (9 A.M - 5 P.M) for bike rental demand on weekdays in {month_names[selected_month]}/2012 for registered users?")

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(
    data=df_filtered_time,
    x="hr",
    y="registered",
    marker="o",
    linewidth=2,
    label="Demand",
    ax=ax
)
ax.set_title(f"Bike Rental Demand During Rush Hours (9 AM - 5 PM) on Weekdays in {month_names[selected_month]}/2012")
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Registered Users")
ax.set_xticks(range(9, 18))  # Set ticks for hours 9 to 17
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Bar Chart: Percentage of Bicycle Rental Demand Across Different Seasons
st.write(f"### Question 3: How much percentage of bicycle rental demand across seasons in {month_names[selected_month]}/2012 for registered users?")

if not df_seasonal.empty:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=df_seasonal,
        x="season",
        y="percentage",
        hue="season",
        dodge=False,  # Single bar per season
        palette="viridis",
        ax=ax
    )
    ax.set_title("Percentage of Bicycle Rental Demand Across Different Seasons")
    ax.set_xlabel("Season (1: Winter, 2: Spring, 3: Summer, 4: Fall)")
    ax.set_ylabel("Percentage (%)")
    ax.set_ylim(0, 100)
    ax.grid(axis="y", linestyle="--", linewidth=0.7, alpha=0.7)
    ax.legend_.remove()  # Remove duplicate legend if "hue" is same as x

    st.pyplot(fig)
    st.dataframe(df_seasonal)
else:
    st.warning("No data available for the selected month.")

# Heatmap: Clustering Patterns by Season (Full Year Data)
st.write("## Clustering Analysis")
st.write("How is the demand's pattern between casual and registered users across different seasons in 2012?")

# Clustering analysis using the full 2012 dataset
season_cluster_data = hour_df[hour_df["yr"] == 1].groupby("season")[["casual", "registered", "cnt"]].mean().reset_index()
scaler = StandardScaler()
normalized_data = scaler.fit_transform(season_cluster_data[["casual", "registered", "cnt"]])
kmeans = KMeans(n_clusters=3, random_state=42)
season_cluster_data["Cluster"] = kmeans.fit_predict(normalized_data)

# Map season numbers to season names
season_names = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
season_cluster_data["Season"] = season_cluster_data["season"].map(season_names)

# Pivot data for heatmap
pivot_data = season_cluster_data.pivot(index="Season", columns="Cluster", values="cnt")

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    pivot_data,
    annot=True,
    fmt=".1f",
    cmap="coolwarm",
    cbar_kws={"label": "Average Bike Rentals"},
    ax=ax,
)

ax.set_title("Heatmap of Clustering Patterns by Season in 2012")
ax.set_xlabel("Cluster")
ax.set_ylabel("Season")
st.pyplot(fig)

# Clustering Details
st.write("### Clustering Details by Season")
for cluster in sorted(season_cluster_data["Cluster"].unique()):
    st.write(f"#### Cluster {cluster}:")
    cluster_data = season_cluster_data[season_cluster_data["Cluster"] == cluster]
    st.dataframe(cluster_data)

st.markdown("Designed with ❤️ using Streamlit")
