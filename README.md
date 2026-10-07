# Crime Analysis using Hadoop MapReduce

A Big Data analysis project that processes crime datasets using **Hadoop HDFS and Hadoop MapReduce** and presents the processed results through an interactive **Streamlit and Plotly dashboard**.

The project analyzes five crime-related datasets covering different categories such as IPC crimes, auto theft, property theft, murder victims, and crimes against women. Each dataset is processed using a separate Mapper and Reducer, and the resulting aggregated data is used for visualization and interactive analysis.

---

## 1. Project Overview

Crime datasets contain information across different states, districts, years, crime categories, and demographic groups. Processing and analyzing such data provides an opportunity to demonstrate how Big Data technologies can be used for storage, processing, and analysis.

This project implements a complete Big Data processing workflow using Hadoop.

The overall workflow is:

```text
Crime CSV Datasets
        |
        v
   Hadoop HDFS
        |
        v
 Hadoop MapReduce
        |
        v
Aggregated Results
        |
        v
Processed CSV Files
        |
        +----------------------+
        |                      |
        v                      v
Static Visualizations    Interactive Dashboard
   Matplotlib            Streamlit + Plotly
```

The Hadoop part of the project is responsible for storing and processing the datasets. Python is then used to work with the processed MapReduce results and present them through visualizations and an interactive dashboard.

---

## 2. Objectives

The main objectives of this project are:

- Store crime datasets using Hadoop HDFS.
- Understand the structure of different crime datasets.
- Process the datasets using Hadoop MapReduce.
- Implement separate Mapper and Reducer programs for different datasets.
- Aggregate crime statistics by state and year.
- Calculate useful crime-related metrics.
- Generate visualizations from the processed data.
- Build an interactive dashboard for exploring the results.
- Demonstrate an end-to-end Big Data processing workflow.

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Hadoop 3.5.0 | Big Data processing framework |
| HDFS | Storage of crime datasets |
| Hadoop MapReduce | Data processing and aggregation |
| Hadoop Streaming | Running Python Mapper and Reducer programs |
| Python 3 | Mapper, Reducer and analysis programs |
| Pandas | Processing MapReduce output |
| Matplotlib | Static visualizations |
| Plotly | Interactive charts |
| Streamlit | Interactive dashboard |
| Git | Version control |
| GitHub | Source code repository |
| WSL2 / Ubuntu | Local Hadoop execution environment |

### Development Environment

The project was developed and tested using:

- Windows 11
- WSL2
- Ubuntu 24.04 LTS
- Java 17
- Hadoop 3.5.0
- Python 3
- Hadoop Streaming

The Hadoop environment is configured in **pseudo-distributed mode**, allowing HDFS and MapReduce/YARN components to run on a single machine.

---

# 4. Datasets

Five crime datasets are used in this project.

The datasets cover different aspects of crime in India and contain information across multiple years and states.

---

## 4.1 IPC Crime Dataset

**File:**

```text
01_District_wise_crimes_committed_IPC_2001_2012.csv
```

This dataset contains district-wise crime statistics under the Indian Penal Code.

Important fields include:

- State/UT
- District
- Year
- Murder
- Attempt to Murder
- Rape
- Kidnapping & Abduction
- Dacoity
- Robbery
- Burglary
- Theft
- Auto Theft
- Riots
- Cheating
- Arson
- Dowry Deaths
- Other IPC Crimes
- Total IPC Crimes

### Processing

The MapReduce job aggregates the district-level records using:

```text
State + Year
```

The main output is:

```text
State + Year -> Total IPC Crimes
```

This provides the total IPC crime count for each state and year.

---

## 4.2 Crimes Against Women Dataset

**File:**

```text
42_Cases_under_crime_against_women.csv
```

This dataset contains information about cases related to crimes against women.

Important fields include:

- Area/State
- Year
- Cases Reported
- Cases Chargesheeted
- Cases Convicted
- Cases Pending Trial
- Cases Investigated
- Cases Sent for Trial
- Cases Trials Completed
- Other case-status fields

### Processing

The MapReduce job aggregates selected case statistics using:

```text
State + Year
```

The main values extracted are:

- Reported cases
- Chargesheeted cases
- Convicted cases
- Pending trial cases

---

## 4.3 Auto Theft Dataset

**File:**

```text
30_Auto_theft.csv
```

This dataset contains statistics related to vehicle theft.

Important fields include:

- Area/State
- Year
- Group Name
- Sub Group Name
- Auto Theft Recovered
- Auto Theft Stolen
- Auto Theft Coordinated/Traced

### Processing

The MapReduce job calculates:

```text
State + Year -> Total Stolen
State + Year -> Total Recovered
```

This allows stolen and recovered vehicles to be compared across states and years.

---

## 4.4 Property Stolen and Recovered Dataset

**File:**

```text
10_Property_stolen_and_recovered.csv
```

This dataset contains information about property reported stolen and subsequently recovered.

Important fields include:

- Area/State
- Year
- Group Name
- Sub Group Name
- Cases Property Stolen
- Cases Property Recovered
- Value of Property Stolen
- Value of Property Recovered

### Processing

The MapReduce job calculates:

- Total cases of property stolen
- Total cases of property recovered
- Total value of property stolen
- Total value of property recovered

A recovery rate is calculated from the aggregated values:

```text
Recovery Rate =
(Value of Property Recovered / Value of Property Stolen) × 100
```

---

## 4.5 Murder Victim Age and Sex Dataset

**File:**

```text
32_Murder_victim_age_sex.csv
```

This dataset contains demographic information about murder victims.

Important fields include:

- Area/State
- Year
- Group Name
- Sub Group Name
- Victims Total
- Victims Above 50 Years
- Victims Up to 10 Years
- Victims Up to 15-18 Years
- Victims Up to 18-30 Years
- Victims Up to 30-50 Years

The dataset also contains group information that allows male and female victim counts to be extracted.

### Processing

The MapReduce job aggregates:

```text
State + Year -> Male Victims
State + Year -> Female Victims
State + Year -> Total Victims
```

---

# 5. Why Hadoop MapReduce?

The main processing requirement of the project is to demonstrate Big Data processing using Hadoop.

Instead of directly aggregating the raw CSV files using Pandas, the project uses **Hadoop MapReduce** to perform the main aggregation stage.

The MapReduce workflow is:

```text
Input Dataset
      |
      v
   Mapper
      |
      v
Intermediate Key-Value Pairs
      |
      v
Shuffle and Sort
      |
      v
   Reducer
      |
      v
Aggregated Output
```

For example, consider the following records:

```text
State       Year       Value
--------------------------------
Telangana   2010       100
Telangana   2010       250
Telangana   2010       150
Andhra      2010       200
```

The Mapper generates key-value pairs:

```text
Telangana,2010    100
Telangana,2010    250
Telangana,2010    150
Andhra,2010       200
```

During the shuffle and sort phase, Hadoop groups values having the same key:

```text
Andhra,2010      -> [200]
Telangana,2010   -> [100, 250, 150]
```

The Reducer then calculates the aggregated values:

```text
Andhra,2010      -> 200
Telangana,2010   -> 500
```

The same MapReduce concept is used for all five datasets, with the Mapper and Reducer logic adapted to the structure of each dataset.

---

# 6. Project Architecture

```text
                    +----------------------+
                    |     Crime CSV Files  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      Hadoop HDFS     |
                    |      Input Data      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Hadoop MapReduce   |
                    +----------+-----------+
                               |
             +-----------------+------------------+
             |                 |                  |
             v                 v                  v
        IPC Analysis      Property Analysis   Auto Theft
             |                 |                  |
             +-----------------+------------------+
                               |
                    +----------+-----------+
                    |  Murder / Women Jobs |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Aggregated CSV Files |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
        Static Visualizations       Interactive Dashboard
            Matplotlib              Streamlit + Plotly
```

---

# 7. Project Structure

```text
Crime-Analysis-BDA-CBP/
│
├── data/
│   ├── 01_District_wise_crimes_committed_IPC_2001_2012.csv
│   ├── 42_Cases_under_crime_against_women.csv
│   ├── 30_Auto_theft.csv
│   ├── 10_Property_stolen_and_recovered.csv
│   └── 32_Murder_victim_age_sex.csv
│
├── mapper/
│   ├── ipc_mapper.py
│   ├── property_mapper.py
│   ├── auto_mapper.py
│   ├── murder_mapper.py
│   └── women_mapper.py
│
├── reducer/
│   ├── ipc_reducer.py
│   ├── property_reducer.py
│   ├── auto_reducer.py
│   ├── murder_reducer.py
│   └── women_reducer.py
│
├── scripts/
│   ├── visualize.py
│   └── dashboard.py
│
├── output/
│   ├── ipc_state_year.csv
│   ├── property_analysis.csv
│   ├── auto_theft_analysis.csv
│   ├── murder_analysis.csv
│   ├── women_analysis.csv
│   └── graphs/
│
├── .streamlit/
│   └── config.toml
│
├── .gitignore
└── README.md
```

---

# 8. Hadoop Setup

## 8.1 Java

The project uses Java 17.

Check the installed Java version:

```bash
java -version
```

Check the Java compiler:

```bash
javac -version
```

The Java installation used in the project is:

```text
/usr/lib/jvm/java-17-openjdk-amd64
```

---

## 8.2 Hadoop Installation

Hadoop 3.5.0 is installed under:

```text
~/hadoop-3.5.0
```

The following environment variables are used:

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export HADOOP_HOME=$HOME/hadoop-3.5.0
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

These variables can be added to `~/.bashrc` so that they are available in new terminal sessions.

After modifying `.bashrc`:

```bash
source ~/.bashrc
```

Check Hadoop:

```bash
hadoop version
```

---

# 9. Hadoop Configuration

The project uses Hadoop in **pseudo-distributed mode**.

The main Hadoop configuration files are located at:

```text
~/hadoop-3.5.0/etc/hadoop/
```

The following configuration files were used:

```text
core-site.xml
hdfs-site.xml
mapred-site.xml
yarn-site.xml
```

## 9.1 HDFS Configuration

The default filesystem is configured as:

```text
hdfs://localhost:9000
```

HDFS replication is configured as:

```text
1
```

Since the project runs on a single local machine, one replica is sufficient for this academic implementation.

The local NameNode and DataNode directories are:

```text
/home/greeshma/hadoop_data/namenode
/home/greeshma/hadoop_data/datanode
```

---

# 10. Starting Hadoop

Start HDFS:

```bash
start-dfs.sh
```

Start YARN:

```bash
start-yarn.sh
```

Check the running Hadoop processes:

```bash
jps
```

The expected processes include:

```text
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager
```

---

# 11. Creating the HDFS Project Directories

Create the HDFS input directory:

```bash
hdfs dfs -mkdir -p /user/greeshma/crime_project/input
```

Create the HDFS output directory:

```bash
hdfs dfs -mkdir -p /user/greeshma/crime_project/output
```

Check the directories:

```bash
hdfs dfs -ls /user/greeshma/crime_project
```

---

# 12. Uploading the Datasets to HDFS

The local datasets are stored in:

```text
~/crime_project/data
```

Upload the IPC dataset:

```bash
hdfs dfs -put data/01_District_wise_crimes_committed_IPC_2001_2012.csv \
/user/greeshma/crime_project/input/
```

Upload the crimes against women dataset:

```bash
hdfs dfs -put data/42_Cases_under_crime_against_women.csv \
/user/greeshma/crime_project/input/
```

Upload the auto theft dataset:

```bash
hdfs dfs -put data/30_Auto_theft.csv \
/user/greeshma/crime_project/input/
```

Upload the property dataset:

```bash
hdfs dfs -put data/10_Property_stolen_and_recovered.csv \
/user/greeshma/crime_project/input/
```

Upload the murder dataset:

```bash
hdfs dfs -put data/32_Murder_victim_age_sex.csv \
/user/greeshma/crime_project/input/
```

Verify the uploaded files:

```bash
hdfs dfs -ls /user/greeshma/crime_project/input
```

---

# 13. Hadoop Streaming

The Mapper and Reducer programs in this project are written in Python.

**Hadoop Streaming** is used to execute these Python programs as Hadoop Mapper and Reducer tasks.

The Hadoop Streaming JAR used is:

```text
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar
```

The basic MapReduce execution pattern is:

```text
Python Mapper
      |
      v
Hadoop Shuffle and Sort
      |
      v
Python Reducer
      |
      v
HDFS Output
```

---

# 14. Running the IPC MapReduce Job

Make the scripts executable:

```bash
chmod 755 mapper/ipc_mapper.py
chmod 755 reducer/ipc_reducer.py
```

If an output directory from a previous run exists, remove it:

```bash
hdfs dfs -rm -r /user/greeshma/crime_project/output/ipc_state_year
```

Run the MapReduce job:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/01_District_wise_crimes_committed_IPC_2001_2012.csv \
-output /user/greeshma/crime_project/output/ipc_state_year \
-mapper "python3 mapper/ipc_mapper.py" \
-reducer "python3 reducer/ipc_reducer.py" \
-file mapper/ipc_mapper.py \
-file reducer/ipc_reducer.py
```

View the output:

```bash
hdfs dfs -cat /user/greeshma/crime_project/output/ipc_state_year/part-00000
```

---

# 15. Running the Property Theft MapReduce Job

Make the scripts executable:

```bash
chmod 755 mapper/property_mapper.py
chmod 755 reducer/property_reducer.py
```

Run the MapReduce job:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/10_Property_stolen_and_recovered.csv \
-output /user/greeshma/crime_project/output/property_analysis \
-mapper "python3 mapper/property_mapper.py" \
-reducer "python3 reducer/property_reducer.py" \
-file mapper/property_mapper.py \
-file reducer/property_reducer.py
```

View the output:

```bash
hdfs dfs -cat /user/greeshma/crime_project/output/property_analysis/part-00000
```

---

# 16. Running the Auto Theft MapReduce Job

Make the scripts executable:

```bash
chmod 755 mapper/auto_mapper.py
chmod 755 reducer/auto_reducer.py
```

Run the MapReduce job:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/30_Auto_theft.csv \
-output /user/greeshma/crime_project/output/auto_theft_analysis \
-mapper "python3 mapper/auto_mapper.py" \
-reducer "python3 reducer/auto_reducer.py" \
-file mapper/auto_mapper.py \
-file reducer/auto_reducer.py
```

View the output:

```bash
hdfs dfs -cat /user/greeshma/crime_project/output/auto_theft_analysis/part-00000
```

---

# 17. Running the Murder MapReduce Job

Make the scripts executable:

```bash
chmod 755 mapper/murder_mapper.py
chmod 755 reducer/murder_reducer.py
```

Run the MapReduce job:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/32_Murder_victim_age_sex.csv \
-output /user/greeshma/crime_project/output/murder_analysis \
-mapper "python3 mapper/murder_mapper.py" \
-reducer "python3 reducer/murder_reducer.py" \
-file mapper/murder_mapper.py \
-file reducer/murder_reducer.py
```

View the output:

```bash
hdfs dfs -cat /user/greeshma/crime_project/output/murder_analysis/part-00000
```

---

# 18. Running the Crimes Against Women MapReduce Job

Make the scripts executable:

```bash
chmod 755 mapper/women_mapper.py
chmod 755 reducer/women_reducer.py
```

Run the MapReduce job:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/42_Cases_under_crime_against_women.csv \
-output /user/greeshma/crime_project/output/women_analysis \
-mapper "python3 mapper/women_mapper.py" \
-reducer "python3 reducer/women_reducer.py" \
-file mapper/women_mapper.py \
-file reducer/women_reducer.py
```

View the output:

```bash
hdfs dfs -cat /user/greeshma/crime_project/output/women_analysis/part-00000
```

---

# 19. Retrieving MapReduce Results

The MapReduce results are stored in HDFS.

For example:

```text
/user/greeshma/crime_project/output/ipc_state_year/
```

The result can be copied back to the local project:

```bash
hdfs dfs -get \
/user/greeshma/crime_project/output/ipc_state_year/part-00000 \
output/ipc_state_year.csv
```

Property analysis:

```bash
hdfs dfs -get \
/user/greeshma/crime_project/output/property_analysis/part-00000 \
output/property_analysis.csv
```

Auto theft analysis:

```bash
hdfs dfs -get \
/user/greeshma/crime_project/output/auto_theft_analysis/part-00000 \
output/auto_theft_analysis.csv
```

Murder analysis:

```bash
hdfs dfs -get \
/user/greeshma/crime_project/output/murder_analysis/part-00000 \
output/murder_analysis.csv
```

Crimes against women analysis:

```bash
hdfs dfs -get \
/user/greeshma/crime_project/output/women_analysis/part-00000 \
output/women_analysis.csv
```

These processed CSV files are then used by the visualization and dashboard components.

---

# 20. Python Environment

A Python virtual environment is used for the visualization and dashboard components.

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install pandas matplotlib streamlit plotly
```

The virtual environment is excluded from Git using `.gitignore`.

---

# 21. Generating Static Visualizations

The visualization script is:

```text
scripts/visualize.py
```

The script reads the processed MapReduce output CSV files and generates static graphs.

Run:

```bash
python3 scripts/visualize.py
```

The generated graphs are stored in:

```text
output/graphs/
```

The project generates visualizations for:

- IPC crimes by year
- Auto theft
- Crimes against women
- Murder victim gender
- Property recovery rate

---

# 22. Interactive Dashboard

The project also includes an interactive dashboard built using:

- Streamlit
- Plotly
- Pandas

The dashboard reads the processed MapReduce output files from:

```text
output/
```

It does not directly process the original raw datasets.

The dashboard workflow is:

```text
Raw Dataset
     |
     v
HDFS
     |
     v
MapReduce
     |
     v
Processed CSV
     |
     v
Streamlit Dashboard
```

This separation keeps the Hadoop processing stage independent from the visualization stage.

---

# 23. Running the Dashboard

Activate the Python virtual environment:

```bash
source .venv/bin/activate
```

Run the dashboard:

```bash
streamlit run scripts/dashboard.py
```

Streamlit will start a local web server.

Open the URL displayed in the terminal. It will normally be:

```text
http://localhost:8501
```

---

# 24. Dashboard Features

The dashboard provides interactive analysis of the processed crime data.

A common filter section is available on the left side.

### Dataset

The user can select one of the available datasets:

- IPC Crimes
- Auto Theft
- Property Theft
- Murder
- Crimes Against Women

### State

The state filter allows the user to analyze the selected dataset for a specific state.

### Year Range

The year range filter allows the user to select the required time period.

The selected filters are applied to the displayed data and charts.

---

# 25. Dashboard Analysis

## IPC Crime Analysis

The dashboard displays aggregated IPC crime statistics by state and year.

This can be used to examine changes in overall IPC crime levels across different years.

## Auto Theft Analysis

The dashboard compares:

- Vehicles Stolen
- Vehicles Recovered

This provides a view of vehicle theft and recovery trends.

## Property Theft Analysis

The dashboard displays:

- Property cases stolen
- Property cases recovered
- Value of property stolen
- Value of property recovered
- Recovery rate

The recovery rate is calculated as:

```text
Recovery Rate =
(Value Recovered / Value Stolen) × 100
```

## Murder Victim Analysis

The dashboard presents murder victim statistics including:

- Male victims
- Female victims
- Total victims

The results can be filtered by state and year.

## Crimes Against Women

The dashboard presents selected case-status statistics including:

- Cases Reported
- Cases Chargesheeted
- Cases Convicted
- Cases Pending Trial

These values can be explored using the state and year filters.

---

# 26. Data Processing Logic

Each dataset has a dedicated Mapper and Reducer.

| Dataset | Mapper | Reducer | Main Aggregation |
|---|---|---|---|
| IPC Crimes | `ipc_mapper.py` | `ipc_reducer.py` | State + Year → Total IPC Crimes |
| Property Theft | `property_mapper.py` | `property_reducer.py` | State + Year → Stolen / Recovered |
| Auto Theft | `auto_mapper.py` | `auto_reducer.py` | State + Year → Stolen / Recovered |
| Murder | `murder_mapper.py` | `murder_reducer.py` | State + Year → Male / Female / Total |
| Crimes Against Women | `women_mapper.py` | `women_reducer.py` | State + Year → Reported / Chargesheeted / Convicted / Pending |

Keeping a separate Mapper and Reducer for each dataset allows the processing logic to match the structure and fields of that particular dataset.

---

# 27. HDFS and MapReduce Commands Used

Some of the main Hadoop commands used in the project are listed below.

### Check Hadoop version

```bash
hadoop version
```

### Start HDFS

```bash
start-dfs.sh
```

### Start YARN

```bash
start-yarn.sh
```

### Check Hadoop processes

```bash
jps
```

### List HDFS files

```bash
hdfs dfs -ls /user/greeshma/crime_project/input
```

### Create an HDFS directory

```bash
hdfs dfs -mkdir -p /user/greeshma/crime_project/input
```

### Upload a file to HDFS

```bash
hdfs dfs -put <local-file> <hdfs-directory>
```

### Read an HDFS file

```bash
hdfs dfs -cat <hdfs-file>
```

### Remove an HDFS directory

```bash
hdfs dfs -rm -r <hdfs-directory>
```

### Copy a file from HDFS

```bash
hdfs dfs -get <hdfs-file> <local-file>
```

---

# 28. Complete Execution Order

For a fresh setup, the project can be executed in the following order.

### Step 1 — Verify Java

```bash
java -version
javac -version
```

### Step 2 — Configure Hadoop

Configure:

```text
core-site.xml
hdfs-site.xml
mapred-site.xml
yarn-site.xml
```

### Step 3 — Start Hadoop

```bash
start-dfs.sh
start-yarn.sh
```

### Step 4 — Verify Hadoop

```bash
jps
```

### Step 5 — Create HDFS directories

```bash
hdfs dfs -mkdir -p /user/greeshma/crime_project/input
hdfs dfs -mkdir -p /user/greeshma/crime_project/output
```

### Step 6 — Upload datasets

Upload the five CSV files to:

```text
/user/greeshma/crime_project/input/
```

### Step 7 — Run the five MapReduce jobs

Run:

1. IPC Crime MapReduce
2. Property Theft MapReduce
3. Auto Theft MapReduce
4. Murder MapReduce
5. Crimes Against Women MapReduce

### Step 8 — Retrieve the results

Copy the generated HDFS outputs to:

```text
output/
```

### Step 9 — Generate static visualizations

```bash
python3 scripts/visualize.py
```

### Step 10 — Start the interactive dashboard

```bash
streamlit run scripts/dashboard.py
```

---

# 29. Results

The MapReduce processing stage produces five processed datasets:

```text
ipc_state_year.csv
property_analysis.csv
auto_theft_analysis.csv
murder_analysis.csv
women_analysis.csv
```

These files are used to generate the static visualizations and power the interactive dashboard.

The final dashboard allows users to explore the processed results using:

- Dataset selection
- State selection
- Year range selection

The interactive dashboard provides a more flexible way to explore the processed data compared with viewing only static graphs.

---

# 30. Limitations

This project is designed as an academic Big Data implementation and runs on a single local machine.

The main limitations are:

- Hadoop runs in pseudo-distributed mode on a single machine.
- HDFS replication is configured to `1`.
- Only five selected crime datasets are processed.
- The MapReduce jobs focus mainly on aggregation rather than predictive modeling.
- The dashboard works with the processed MapReduce output files rather than querying HDFS directly.
- The project is intended for academic demonstration rather than production deployment.

The main focus of the project is to demonstrate HDFS storage, MapReduce processing, data aggregation, and interactive visualization.

---

# 31. Future Improvements

Possible extensions to the project include:

- Processing additional crime datasets.
- Adding more crime categories and analytical metrics.
- Adding district-level analysis to the dashboard.
- Running the Hadoop environment on multiple nodes.
- Increasing HDFS replication for fault tolerance.
- Adding more MapReduce jobs for advanced analysis.
- Integrating a database or data warehouse.
- Adding real-time crime data processing.
- Adding predictive analytics and forecasting.
- Deploying the dashboard to a cloud platform.

---

# 32. Git and GitHub

Git is used for version control and GitHub is used to host the project repository.

Initialize the repository:

```bash
git init -b main
```

Add the GitHub repository as the remote:

```bash
git remote add origin <repository-url>
```

Check the remote:

```bash
git remote -v
```

Check the project status:

```bash
git status
```

Add project files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initial crime analysis project"
```

Push the project:

```bash
git push -u origin main
```

The Python virtual environment and Python cache files are excluded using `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
```

---

# 33. Conclusion

This project demonstrates an end-to-end Big Data workflow for crime data analysis.

The process begins with raw crime datasets, which are uploaded to Hadoop HDFS. Hadoop MapReduce is then used to process and aggregate the datasets based on state and year. The processed results are retrieved as CSV files and used for visualization and interactive analysis.

The project provides practical experience with:

- Hadoop HDFS
- Hadoop MapReduce
- Hadoop Streaming
- Python Mapper and Reducer programs
- Data aggregation
- Pandas
- Matplotlib
- Plotly
- Streamlit
- Git and GitHub

The complete pipeline can be summarized as:

```text
Raw Crime Data
      |
      v
    HDFS
      |
      v
Hadoop MapReduce
      |
      v
Processed Results
      |
      v
Python Analysis
      |
      v
Interactive Dashboard
```

---

## Repository

GitHub repository:

**Crime Analysis using Hadoop MapReduce**

https://github.com/GreeshmaReddy427/Crime-Analysis-BDA-CBP
