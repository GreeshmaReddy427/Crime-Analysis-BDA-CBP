import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------
# Folders
# ---------------------------------------------------------

OUTPUT_DIR = os.path.expanduser("~/crime_project/output")
GRAPH_DIR = os.path.join(OUTPUT_DIR, "graphs")

os.makedirs(GRAPH_DIR, exist_ok=True)


# =========================================================
# 1. IPC CRIMES
# =========================================================

ipc_file = os.path.join(OUTPUT_DIR, "ipc_state_year.csv")

ipc = pd.read_csv(
    ipc_file,
    sep="\t",
    header=None,
    names=["StateYear", "Total_IPC"]
)

# Split "State,Year"
ipc[["State", "Year"]] = ipc["StateYear"].str.rsplit(
    ",", n=1, expand=True
)

ipc["Year"] = pd.to_numeric(ipc["Year"])
ipc["Total_IPC"] = pd.to_numeric(ipc["Total_IPC"])

# Total crimes across all states for each year
ipc_year = ipc.groupby("Year")["Total_IPC"].sum()

plt.figure(figsize=(10, 6))

plt.plot(
    ipc_year.index,
    ipc_year.values,
    marker="o"
)

plt.title("Total IPC Crimes by Year")
plt.xlabel("Year")
plt.ylabel("Total IPC Crimes")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(GRAPH_DIR, "ipc_crimes_by_year.png")
)

plt.close()


# =========================================================
# 2. AUTO THEFT
# =========================================================

auto_file = os.path.join(
    OUTPUT_DIR,
    "auto_theft_analysis.csv"
)

auto = pd.read_csv(
    auto_file,
    sep="\t",
    header=None,
    names=["StateYear", "Values"]
)

auto[["State", "Year"]] = auto["StateYear"].str.rsplit(
    ",", n=1, expand=True
)

auto["Year"] = pd.to_numeric(auto["Year"])

# Values format:
# Stolen,Recovered
auto[["Stolen", "Recovered"]] = auto["Values"].str.split(
    ",",
    expand=True
)

auto["Stolen"] = pd.to_numeric(auto["Stolen"])
auto["Recovered"] = pd.to_numeric(auto["Recovered"])

auto_year = auto.groupby("Year")[
    ["Stolen", "Recovered"]
].sum()

plt.figure(figsize=(10, 6))

plt.plot(
    auto_year.index,
    auto_year["Stolen"],
    marker="o",
    label="Stolen"
)

plt.plot(
    auto_year.index,
    auto_year["Recovered"],
    marker="o",
    label="Recovered"
)

plt.title("Auto Theft: Stolen vs Recovered")
plt.xlabel("Year")
plt.ylabel("Number of Vehicles")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(GRAPH_DIR, "auto_theft.png")
)

plt.close()


# =========================================================
# 3. PROPERTY THEFT
# =========================================================

property_file = os.path.join(
    OUTPUT_DIR,
    "property_analysis.csv"
)

prop = pd.read_csv(
    property_file,
    sep="\t",
    header=None,
    names=["StateYear", "Values"]
)

prop[["State", "Year"]] = prop["StateYear"].str.rsplit(
    ",", n=1, expand=True
)

prop["Year"] = pd.to_numeric(prop["Year"])

# Values format:
# CasesStolen,CasesRecovered,ValueStolen,ValueRecovered,RecoveryRate

prop[
    [
        "Cases_Stolen",
        "Cases_Recovered",
        "Value_Stolen",
        "Value_Recovered",
        "Recovery_Rate"
    ]
] = prop["Values"].str.split(
    ",",
    expand=True
)

prop["Value_Stolen"] = pd.to_numeric(
    prop["Value_Stolen"]
)

prop["Value_Recovered"] = pd.to_numeric(
    prop["Value_Recovered"]
)

property_year = prop.groupby("Year")[
    ["Value_Stolen", "Value_Recovered"]
].sum()

# Calculate percentage
property_year["Recovery_Rate"] = (
    property_year["Value_Recovered"]
    / property_year["Value_Stolen"]
    * 100
)

plt.figure(figsize=(10, 6))

plt.plot(
    property_year.index,
    property_year["Recovery_Rate"],
    marker="o"
)

plt.title("Property Recovery Rate by Year")
plt.xlabel("Year")
plt.ylabel("Recovery Rate (%)")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "property_recovery_rate.png"
    )
)

plt.close()


# =========================================================
# 4. MURDER VICTIMS
# =========================================================

murder_file = os.path.join(
    OUTPUT_DIR,
    "murder_analysis.csv"
)

murder = pd.read_csv(
    murder_file,
    sep="\t",
    header=None,
    names=["StateYear", "Values"]
)

murder[["State", "Year"]] = murder["StateYear"].str.rsplit(
    ",", n=1, expand=True
)

murder["Year"] = pd.to_numeric(murder["Year"])

# Values format:
# Male,Female,Total
murder[
    ["Male", "Female", "Total"]
] = murder["Values"].str.split(
    ",",
    expand=True
)

murder["Male"] = pd.to_numeric(murder["Male"])
murder["Female"] = pd.to_numeric(murder["Female"])
murder["Total"] = pd.to_numeric(murder["Total"])

murder_year = murder.groupby("Year")[
    ["Male", "Female"]
].sum()

plt.figure(figsize=(10, 6))

plt.plot(
    murder_year.index,
    murder_year["Male"],
    marker="o",
    label="Male"
)

plt.plot(
    murder_year.index,
    murder_year["Female"],
    marker="o",
    label="Female"
)

plt.title("Murder Victims by Gender")
plt.xlabel("Year")
plt.ylabel("Number of Victims")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "murder_gender.png"
    )
)

plt.close()


# =========================================================
# 5. CRIMES AGAINST WOMEN
# =========================================================

women_file = os.path.join(
    OUTPUT_DIR,
    "women_analysis.csv"
)

women = pd.read_csv(
    women_file,
    sep="\t",
    header=None,
    names=["StateYear", "Values"]
)

women[["State", "Year"]] = women["StateYear"].str.rsplit(
    ",", n=1, expand=True
)

women["Year"] = pd.to_numeric(women["Year"])

# Values format:
# Reported,Chargesheeted,Convicted,PendingTrial

women[
    [
        "Reported",
        "Chargesheeted",
        "Convicted",
        "Pending_Trial"
    ]
] = women["Values"].str.split(
    ",",
    expand=True
)

women["Reported"] = pd.to_numeric(
    women["Reported"]
)

women["Chargesheeted"] = pd.to_numeric(
    women["Chargesheeted"]
)

women["Convicted"] = pd.to_numeric(
    women["Convicted"]
)

women["Pending_Trial"] = pd.to_numeric(
    women["Pending_Trial"]
)

women_year = women.groupby("Year")[
    [
        "Reported",
        "Chargesheeted",
        "Convicted",
        "Pending_Trial"
    ]
].sum()

plt.figure(figsize=(10, 6))

plt.plot(
    women_year.index,
    women_year["Reported"],
    marker="o",
    label="Reported"
)

plt.plot(
    women_year.index,
    women_year["Convicted"],
    marker="o",
    label="Convicted"
)

plt.title("Crimes Against Women: Reported vs Convicted")
plt.xlabel("Year")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(
        GRAPH_DIR,
        "crimes_against_women.png"
    )
)

plt.close()


# =========================================================
# DONE
# =========================================================

print()
print("All graphs generated successfully!")
print()
print("Graphs saved in:")
print(GRAPH_DIR)
