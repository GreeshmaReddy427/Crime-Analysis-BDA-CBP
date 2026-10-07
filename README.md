# Crime Analysis using Hadoop MapReduce

A Big Data analysis project that processes multiple crime datasets using **Hadoop HDFS and Hadoop MapReduce** and presents the processed results through an interactive **Streamlit and Plotly dashboard**.

The project focuses on analyzing different categories of crime in India across states and years. Five crime datasets are processed independently using MapReduce programs, and the resulting aggregated data is used for visualization and interactive analysis.

---

## 1. Project Overview

Crime datasets contain information across multiple states, years, crime categories, and demographic groups. Processing such datasets manually becomes difficult as the amount of data increases.

This project demonstrates how a Big Data processing pipeline can be built using Hadoop.

The main workflow is:

```text
Crime CSV Datasets
        |
        v
   Hadoop HDFS
        |
        v
 Hadoop MapReduce
   /    |    \
  /     |     \
IPC   Property  Auto Theft
       Murder
       Women
        |
        v
Aggregated CSV Results
        |
        v
Python Visualization
        |
        v
Interactive Streamlit Dashboard

The project uses Hadoop for distributed storage and MapReduce for data aggregation. Python is used after the MapReduce stage to prepare the results for visualization.
2. Objectives
The main objectives of this project are:
- Store crime datasets using Hadoop HDFS.
- Understand the structure of different crime datasets.
- Process large CSV files using Hadoop MapReduce.
- Implement separate Mapper and Reducer programs for different datasets.
- Aggregate crime statistics by state and year.
- Calculate useful crime-related metrics.
- Generate visualizations from the processed data.
- Build an interactive dashboard for filtering and exploring the results.
- Understand an end-to-end Big Data processing workflow.
3. Technologies Used
Technology	Purpose
Hadoop 3.5.0	Big Data processing framework
HDFS	Distributed storage of crime datasets
Hadoop MapReduce	Distributed data processing and aggregation
Python 3	Mapper, Reducer and visualization programs
Pandas	Processing MapReduce output
Matplotlib	Static visualizations
Plotly	Interactive charts
Streamlit	Interactive dashboard
Git	Version control
GitHub	Source code repository
WSL2 / Ubuntu	Hadoop execution environment


Development Environment
The project was developed and tested using:
- Windows 11
- WSL2
- Ubuntu 24.04 LTS
- Java 17
- Hadoop 3.5.0
- Python 3
- Hadoop Streaming
4. Datasets
Five crime datasets are used in the project.
The datasets cover different aspects of crime in India and contain information for multiple years and states.
4.1 IPC Crime Dataset
File:
01_District_wise_crimes_committed_IPC_2001_2012.csv

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
Processing performed
The MapReduce job extracts:
State + Year -> Total IPC Crimes

District-level records are aggregated to obtain the total IPC crime count for each state and year.
4.2 Crimes Against Women Dataset
File:
42_Cases_under_crime_against_women.csv

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
Processing performed
The MapReduce job aggregates selected case statistics by:
State + Year

The main values extracted are:
- Reported cases
- Chargesheeted cases
- Convicted cases
- Pending trial cases
4.3 Auto Theft Dataset
File:
30_Auto_theft.csv

This dataset contains statistics related to vehicle theft.
Important fields include:
- Area/State
- Year
- Group Name
- Sub Group Name
- Auto Theft Recovered
- Auto Theft Stolen
- Auto Theft Coordinated/Traced
Processing performed
The MapReduce job calculates:
State + Year -> Total Stolen
State + Year -> Total Recovered

This allows the dashboard to compare stolen and recovered vehicles across states and years.
4.4 Property Stolen and Recovered Dataset
File:
10_Property_stolen_and_recovered.csv

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
Processing performed
The MapReduce job calculates:
- Total cases of property stolen
- Total cases of property recovered
- Total value of property stolen
- Total value of property recovered
A recovery rate is also calculated:
Recovery Rate =
(Value of Property Recovered / Value of Property Stolen) × 100

4.5 Murder Victim Age and Sex Dataset
File:
32_Murder_victim_age_sex.csv

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
Processing performed
The MapReduce job aggregates:
State + Year -> Male Victims
State + Year -> Female Victims
State + Year -> Total Victims

5. Why MapReduce?
The project uses Hadoop MapReduce instead of performing the aggregation directly with Pandas.
The purpose is to demonstrate the Big Data processing concept of:
Input Data
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

For example, consider the IPC dataset.
The Mapper converts records into:
Telangana,2010    45000
Telangana,2010    32000
Telangana,2010    18000

During the MapReduce shuffle phase, values having the same key are grouped:
Telangana,2010 -> [45000, 32000, 18000]

The Reducer then calculates:
Telangana,2010 -> 95000

The same approach is applied to the other datasets with different aggregation logic.
6. Project Architecture
                    +----------------------+
                    |     Crime CSV Files  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      Hadoop HDFS     |
                    |       Input Data     |
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
          Matplotlib                    Streamlit
                                         Plotly

7. Project Structure
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
└── .gitignore

8. Hadoop Setup
8.1 Install Java
The project uses Java 17.
Check the installed version:
java -version

Also verify the Java compiler:
javac -version

8.2 Hadoop Installation
Hadoop 3.5.0 is installed under:
~/hadoop-3.5.0

Set the required environment variables:
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export HADOOP_HOME=$HOME/hadoop-3.5.0
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

These variables can be added to ~/.bashrc so that they are available whenever a new terminal is opened.
After editing .bashrc:
source ~/.bashrc

Check Hadoop:
hadoop version

9. Hadoop Configuration
The project uses Hadoop in pseudo-distributed mode.
The main Hadoop configuration files are located at:
~/hadoop-3.5.0/etc/hadoop/

The following files were configured:
core-site.xml
hdfs-site.xml
mapred-site.xml
yarn-site.xml

9.1 HDFS Configuration
The default filesystem is configured as:
hdfs://localhost:9000

HDFS replication is set to:
1

because this is a local academic project running on a single machine.
The local NameNode and DataNode storage directories are:
/home/greeshma/hadoop_data/namenode
/home/greeshma/hadoop_data/datanode

10. Starting Hadoop
Start HDFS:
start-dfs.sh

Start YARN:
start-yarn.sh

Check running Hadoop processes:
jps

The following processes should normally be visible:
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager

11. Creating the HDFS Project Directories
Create the project input directory:
hdfs dfs -mkdir -p /user/greeshma/crime_project/input

Create an output directory:
hdfs dfs -mkdir -p /user/greeshma/crime_project/output

Check the directories:
hdfs dfs -ls /user/greeshma/crime_project

12. Uploading the Datasets to HDFS
The datasets are stored locally inside:
~/crime_project/data

Upload them to HDFS:
hdfs dfs -put data/01_District_wise_crimes_committed_IPC_2001_2012.csv \
/user/greeshma/crime_project/input/

hdfs dfs -put data/42_Cases_under_crime_against_women.csv \
/user/greeshma/crime_project/input/

hdfs dfs -put data/30_Auto_theft.csv \
/user/greeshma/crime_project/input/

hdfs dfs -put data/10_Property_stolen_and_recovered.csv \
/user/greeshma/crime_project/input/

hdfs dfs -put data/32_Murder_victim_age_sex.csv \
/user/greeshma/crime_project/input/

Verify the uploaded files:
hdfs dfs -ls /user/greeshma/crime_project/input

13. Hadoop Streaming
The MapReduce programs in this project are written in Python.
Hadoop Streaming is used to allow Python scripts to work as Mapper and Reducer programs.
The Hadoop Streaming JAR used in the project is:
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar

14. Running the IPC MapReduce Job
Make the scripts executable:
chmod 755 mapper/ipc_mapper.py
chmod 755 reducer/ipc_reducer.py

Remove an old output directory if it already exists:
hdfs dfs -rm -r /user/greeshma/crime_project/output/ipc_state_year

Run the MapReduce job:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/01_District_wise_crimes_committed_IPC_2001_2012.csv \
-output /user/greeshma/crime_project/output/ipc_state_year \
-mapper "python3 mapper/ipc_mapper.py" \
-reducer "python3 reducer/ipc_reducer.py" \
-file mapper/ipc_mapper.py \
-file reducer/ipc_reducer.py

View the result:
hdfs dfs -cat /user/greeshma/crime_project/output/ipc_state_year/part-00000

15. Running the Property Theft MapReduce Job
Make the scripts executable:
chmod 755 mapper/property_mapper.py
chmod 755 reducer/property_reducer.py

Run:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/10_Property_stolen_and_recovered.csv \
-output /user/greeshma/crime_project/output/property_analysis \
-mapper "python3 mapper/property_mapper.py" \
-reducer "python3 reducer/property_reducer.py" \
-file mapper/property_mapper.py \
-file reducer/property_reducer.py

View the result:
hdfs dfs -cat /user/greeshma/crime_project/output/property_analysis/part-00000

16. Running the Auto Theft MapReduce Job
Make the scripts executable:
chmod 755 mapper/auto_mapper.py
chmod 755 reducer/auto_reducer.py

Run:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/30_Auto_theft.csv \
-output /user/greeshma/crime_project/output/auto_theft_analysis \
-mapper "python3 mapper/auto_mapper.py" \
-reducer "python3 reducer/auto_reducer.py" \
-file mapper/auto_mapper.py \
-file reducer/auto_reducer.py

View the result:
hdfs dfs -cat /user/greeshma/crime_project/output/auto_theft_analysis/part-00000

17. Running the Murder MapReduce Job
Make the scripts executable:
chmod 755 mapper/murder_mapper.py
chmod 755 reducer/murder_reducer.py

Run:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/32_Murder_victim_age_sex.csv \
-output /user/greeshma/crime_project/output/murder_analysis \
-mapper "python3 mapper/murder_mapper.py" \
-reducer "python3 reducer/murder_reducer.py" \
-file mapper/murder_mapper.py \
-file reducer/murder_reducer.py

View the result:
hdfs dfs -cat /user/greeshma/crime_project/output/murder_analysis/part-00000

18. Running the Crimes Against Women MapReduce Job
Make the scripts executable:
chmod 755 mapper/women_mapper.py
chmod 755 reducer/women_reducer.py

Run:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.5.0.jar \
-input /user/greeshma/crime_project/input/42_Cases_under_crime_against_women.csv \
-output /user/greeshma/crime_project/output/women_analysis \
-mapper "python3 mapper/women_mapper.py" \
-reducer "python3 reducer/women_reducer.py" \
-file mapper/women_mapper.py \
-file reducer/women_reducer.py

View the result:
hdfs dfs -cat /user/greeshma/crime_project/output/women_analysis/part-00000

19. Retrieving MapReduce Results
MapReduce output is stored in HDFS.
For example:
/user/greeshma/crime_project/output/ipc_state_year/

The result can be copied back to the local project:
hdfs dfs -get \
/user/greeshma/crime_project/output/ipc_state_year/part-00000 \
output/ipc_state_year.csv

Similarly:
hdfs dfs -get \
/user/greeshma/crime_project/output/property_analysis/part-00000 \
output/property_analysis.csv

hdfs dfs -get \
/user/greeshma/crime_project/output/auto_theft_analysis/part-00000 \
output/auto_theft_analysis.csv

hdfs dfs -get \
/user/greeshma/crime_project/output/murder_analysis/part-00000 \
output/murder_analysis.csv

hdfs dfs -get \
/user/greeshma/crime_project/output/women_analysis/part-00000 \
output/women_analysis.csv

These CSV files are then used by the visualization and dashboard scripts.
20. Python Environment
A Python virtual environment is used for the visualization and dashboard components.
Create the environment:
python3 -m venv .venv

Activate it:
source .venv/bin/activate

Install the required packages:
pip install pandas matplotlib streamlit plotly

The virtual environment is excluded from Git using .gitignore.
21. Generating Static Visualizations
The script:
scripts/visualize.py

reads the MapReduce output CSV files and generates graphs.
Run:
python3 scripts/visualize.py

The generated graphs are stored inside:
output/graphs/

The project generates visualizations for:
- IPC crimes by year
- Auto theft
- Crimes against women
- Murder victim gender
- Property recovery rate
22. Interactive Dashboard
The project also contains an interactive dashboard built using:
- Streamlit
- Plotly
- Pandas
The dashboard reads the processed MapReduce output files from:
output/

It does not directly process the original raw datasets.
The processing flow is:
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

23. Running the Dashboard
Activate the Python virtual environment:
source .venv/bin/activate

Run the Streamlit application:
streamlit run scripts/dashboard.py

Streamlit will start a local web server.
Open the displayed local URL in a browser, normally:
http://localhost:8501

24. Dashboard Features
The dashboard provides interactive analysis of the processed crime data.
A global filter section is provided on the left side.
Dataset
The user can select one of the available datasets:
- IPC Crimes
- Auto Theft
- Property Theft
- Murder
- Crimes Against Women
State
The state filter allows analysis for a specific state.
Year Range
The year range filter allows the user to select the required period.
The selected filters are applied to the displayed data and charts.
25. Dashboard Analysis
IPC Crime Analysis
The dashboard displays the aggregated IPC crime statistics by state and year.
This helps identify changes in overall IPC crime levels over time.
Auto Theft Analysis
The dashboard compares:
Vehicles Stolen
Vehicles Recovered

This provides a simple view of vehicle theft and recovery trends.
Property Theft Analysis
The dashboard displays property theft and recovery information.
The main metric is the recovery rate:
Recovery Rate =
Value Recovered / Value Stolen × 100

Murder Victim Analysis
The dashboard presents murder victim statistics with a focus on:
- Male victims
- Female victims
- Total victims
The results can be filtered by state and year.
Crimes Against Women
The dashboard presents selected case-status statistics including:
- Cases Reported
- Cases Chargesheeted
- Cases Convicted
- Cases Pending Trial
These can be explored using the state and year filters.
26. Data Processing Logic
Each dataset has a dedicated Mapper and Reducer.
Dataset	Mapper	Reducer	Main Aggregation
IPC Crimes	ipc_mapper.py	ipc_reducer.py	State + Year → Total IPC Crimes
Property Theft	property_mapper.py	property_reducer.py	State + Year → Stolen/Recovered
Auto Theft	auto_mapper.py	auto_reducer.py	State + Year → Stolen/Recovered
Murder	murder_mapper.py	murder_reducer.py	State + Year → Male/Female/Total
Crimes Against Women	women_mapper.py	women_reducer.py	State + Year → Reported/Chargesheeted/Convicted/Pending


This separation keeps the processing logic for each dataset independent.
27. Example MapReduce Flow
For a dataset containing:
State       Year       Value
--------------------------------
Telangana   2010       100
Telangana   2010       250
Telangana   2010       150
Andhra      2010       200

The Mapper produces:
Telangana,2010    100
Telangana,2010    250
Telangana,2010    150
Andhra,2010       200

Hadoop performs the shuffle and sort:
Andhra,2010      -> [200]
Telangana,2010   -> [100,250,150]

The Reducer produces:
Andhra,2010      -> 200
Telangana,2010   -> 500

This aggregated output is then stored in HDFS.
28. HDFS and MapReduce Commands Used
Some of the important Hadoop commands used in the project are:
Check Hadoop version
hadoop version

Start HDFS
start-dfs.sh

Start YARN
start-yarn.sh

Check Hadoop processes
jps

List HDFS files
hdfs dfs -ls /user/greeshma/crime_project/input

Create an HDFS directory
hdfs dfs -mkdir -p /user/greeshma/crime_project/input

Upload a file to HDFS
hdfs dfs -put <local-file> <hdfs-directory>

Read an HDFS file
hdfs dfs -cat <hdfs-file>

Remove an HDFS directory
hdfs dfs -rm -r <hdfs-directory>

Copy a file from HDFS
hdfs dfs -get <hdfs-file> <local-file>

29. Git and GitHub
The project is maintained using Git.
Initialize the repository:
git init -b main

Add the GitHub repository as remote:
git remote add origin <repository-url>

Check the remote:
git remote -v

Check the project status:
git status

Add project files:
git add .

Create a commit:
git commit -m "Initial crime analysis project"

Push the project:
git push -u origin main

The Python virtual environment is excluded from the repository using:
.venv/
__pycache__/
*.pyc

30. Complete Execution Order
For a fresh setup, the overall execution sequence is:
Step 1 — Install Java
java -version
javac -version

Step 2 — Install and configure Hadoop
Configure:
core-site.xml
hdfs-site.xml
mapred-site.xml
yarn-site.xml

Step 3 — Start Hadoop
start-dfs.sh
start-yarn.sh

Step 4 — Verify Hadoop
jps

Step 5 — Create HDFS directories
hdfs dfs -mkdir -p /user/greeshma/crime_project/input
hdfs dfs -mkdir -p /user/greeshma/crime_project/output

Step 6 — Upload datasets
hdfs dfs -put data/<dataset>.csv \
/user/greeshma/crime_project/input/

Step 7 — Run MapReduce jobs
Run the five Mapper/Reducer pairs.
Step 8 — Retrieve the results
hdfs dfs -get <hdfs-output> output/

Step 9 — Generate visualizations
python3 scripts/visualize.py

Step 10 — Start the dashboard
streamlit run scripts/dashboard.py

31. Results
The MapReduce stage produces five processed datasets:
ipc_state_year.csv
property_analysis.csv
auto_theft_analysis.csv
murder_analysis.csv
women_analysis.csv

These processed files are used to generate the visualizations and interactive dashboard.
The final dashboard allows users to explore the results using:
- Dataset selection
- State selection
- Year range selection
This provides a more flexible way of exploring the data than viewing static graphs alone.
32. Limitations
This project is designed as an academic Big Data implementation and runs on a single local machine.
Therefore:
- HDFS replication is configured to 1.
- The Hadoop cluster is a pseudo-distributed local setup.
- The project uses five selected datasets rather than the complete collection of crime datasets.
- MapReduce jobs focus on aggregation rather than predictive modeling.
- The dashboard operates on the processed MapReduce output rather than querying HDFS directly.
- The project does not include a production deployment.
The main purpose is to demonstrate the concepts of HDFS, MapReduce, data aggregation, and interactive visualization.
33. Future Improvements
Possible extensions include:
- Processing additional NCRB datasets.
- Running Hadoop on a multi-node cluster.
- Increasing HDFS replication for fault tolerance.
- Adding more MapReduce analytics.
- Adding crime-category-level analysis.
- Adding district-level interactive analysis.
- Integrating a database or data warehouse.
- Adding real-time crime data processing.
- Adding predictive analytics and forecasting.
- Deploying the dashboard on a cloud platform.
34. Conclusion
This project demonstrates an end-to-end Big Data workflow for crime data analysis.
The project starts with raw crime datasets and stores them in HDFS. Hadoop MapReduce is then used to process and aggregate the data based on state and year. The processed results are retrieved as CSV files and used to generate visualizations and an interactive Streamlit dashboard.
The project provides practical experience with:
- Hadoop HDFS
- Hadoop MapReduce
- Hadoop Streaming
- Python-based Mapper and Reducer programs
- Data aggregation
- Pandas
- Matplotlib
- Plotly
- Streamlit
- Git and GitHub
The overall pipeline is:
Raw Crime Data
      ↓
     HDFS
      ↓
Hadoop MapReduce
      ↓
Processed Results
      ↓
Python Analysis
      ↓
