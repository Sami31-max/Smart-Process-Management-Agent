
import streamlit as st
import psutil
import pandas as pd
import time

# Page Configuration


st.markdown("""
<div style="
background: linear-gradient(90deg, #2563EB, #60A5FA);
padding:20px;
border-radius:15px;
text-align:center;
color:white;">
<h1>🖥 Smart Process Management Agent</h1>
<p>Agentic AI Based OS Monitoring System</p>
</div>
""", unsafe_allow_html=True)



#  UI

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #EAF1FB;
}

/* Main Container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Headers */
h1 {
    color: #1E3A8A;
    text-align: center;
    font-weight: bold;
}

h2, h3 {
    color: #1E40AF;
}

/* Metric Cards */
div[data-testid="metric-container"] {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    border-left: 5px solid #2563EB;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #DBEAFE;
}

/* Buttons */
div.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    height: 3em;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}

/* Download Button */
div.stDownloadButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    height: 3em;
    font-weight: bold;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 10px;
    padding: 10px;
}

/* Input Box */
div[data-baseweb="input"] {
    background-color: white;
    border-radius: 10px;
}

/* Alert Boxes */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)





# Sidebar

st.sidebar.title("Smart Process Agent")

st.sidebar.write("Agentic AI Based OS Monitoring System")

refresh = st.sidebar.button("🔄 Refresh System Data")

st.sidebar.write("---")


# Real-Time Clock
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
st.write(f"🕒 Current Time: {current_time}")

st.write("Real-Time System Monitoring and Intelligent Process Analysis")


# System Monitoring

cpu_usage = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()
memory_usage = memory.percent


# Metrics

col1, col2 = st.columns(2)

with col1:
    st.metric("CPU Usage", f"{cpu_usage}%")

with col2:
    st.metric("RAM Usage", f"{memory_usage}%")

# Progress Bars

st.write("### CPU Usage")

st.progress(int(cpu_usage))

st.write("### RAM Usage")

st.progress(int(memory_usage))




# Live Charts

chart_data = {
    "CPU": [cpu_usage],
    "RAM": [memory_usage]
}

st.subheader("📈 System Performance")

st.bar_chart(chart_data)


# AI Decision Section

st.subheader("🤖 AI System Analysis")

# System Health Status
if cpu_usage < 50 and memory_usage < 50:

    st.success("🟢 System Status: Stable")

elif cpu_usage < 80 and memory_usage < 80:

    st.warning("🟡 System Status: Moderate Load")

else:

    st.error("🔴 System Status: Critical Load")

# CPU Analysis
if cpu_usage > 80:

    st.warning("⚠ High CPU Usage Detected!")
    st.info("💡 Suggestion: Close unnecessary applications")

else:

    st.success("✅ CPU Usage is Normal")

# RAM Analysis
if memory_usage > 80:

    st.warning("⚠ High RAM Usage Detected!")
    st.info("💡 Suggestion: Close background applications")

else:

    st.success("✅ RAM Usage is Normal")

# AI Health Score

health_score = 100

health_score -= cpu_usage * 0.4
health_score -= memory_usage * 0.4

health_score = max(0, int(health_score))

st.metric(
    "🧠 AI Health Score",
    f"{health_score}/100"
)


# Risk Level

if cpu_usage > 85:
    risk = "🔴 Critical"

elif cpu_usage > 60:
    risk = "🟡 Medium"

else:
    risk = "🟢 Low"

st.metric("⚠ Risk Level", risk)





# Process Monitoring

st.subheader("📊 Running Processes")

# Refresh CPU readings
for process in psutil.process_iter():

    try:
        process.cpu_percent(interval=None)

    except:
        pass

time.sleep(1)

process_data = []

# ---------------------------------
# Process Analysis
# ---------------------------------

for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):

    try:

        cpu = process.info['cpu_percent']
        name = process.info['name']
        pid = process.info['pid']

        # Ignore Windows system processes
        ignore_processes = [
            "System Idle Process",
            "System",
            "Registry",
            "Memory Compression"
        ]

        if name in ignore_processes:
            continue

        # ---------------------------------
        # Intelligent Agent Decision
        # ---------------------------------

        safe_apps = [
            "chrome.exe",
            "spotify.exe",
            "Code.exe"
        ]

        if (
            cpu_usage > 80 and
            memory_usage > 80 and
            cpu > 20 and
            name in safe_apps
        ):

            try:

                psutil.Process(pid).terminate()

                st.error(
                    f"🚨 Agent automatically terminated "
                    f"{name} due to critical overload!"
                )

            except:

                st.warning(f"⚠ Unable to terminate {name}")

      
        # AI Recommendations
      

        recommendation = "Normal Process"

        if "chrome" in name.lower():
            recommendation = "Reduce Chrome tabs"

        elif "code" in name.lower():
            recommendation = "Close unused VS Code windows"

        elif "spotify" in name.lower():
            recommendation = "Close Spotify if unnecessary"

        process_data.append({
            "PID": pid,
            "Process Name": name,
            "CPU Usage (%)": cpu,
            "Recommendation": recommendation
        })

    except:
        pass


# Process Table
# ---------------------------------

if process_data:

    df = pd.DataFrame(process_data)

    # Search Process
    search = st.text_input("🔍 Search Process")

    if search:

        filtered_df = df[
            df["Process Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    else:

        filtered_df = df


    # AI Insights

    highest_cpu = filtered_df["CPU Usage (%)"].max()

    highest_process = filtered_df.loc[
        filtered_df["CPU Usage (%)"].idxmax(),
        "Process Name"
    ]

    st.subheader("🧠 AI Insights")
    

    st.info(
        f"Highest resource consuming process: "
        f"{highest_process} ({highest_cpu}%)"
    )
    
    

   
    # Display Process Table
    # ---------------------------------

    st.dataframe(filtered_df, use_container_width=True)

    # ---------------------------------
    # Download CSV Report
    # ---------------------------------

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Process Report",
        data=csv,
        file_name="process_report.csv",
        mime="text/csv"
    )

    # ---------------------------------
    # Process Action Section
    # ---------------------------------

    st.subheader("⚙ Process Actions")

    selected_process = st.selectbox(
        "Select Process to Terminate",
        filtered_df["Process Name"]
    )

    # Terminate Button
    if st.button("❌ Terminate Process"):

        try:

            for process in psutil.process_iter(['pid', 'name']):

                if process.info['name'] == selected_process:

                    psutil.Process(
                        process.info['pid']
                    ).terminate()

                    st.success(
                        f"✅ {selected_process} terminated successfully"
                    )

                    break

        except Exception as e:

            st.error(f"Error: {e}")

else:

    st.success("✅ No running processes detected")

# ---------------------------------
# Footer
# ---------------------------------

st.write("---")

st.info(
    "💡 Press the refresh button in the sidebar "
    "to update live system data."
)

st.write("---")

st.caption("Smart Process Management Agent")
st.caption("Agentic AI Operating Systems Project")

