import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_file = "df.csv"
df = pd.read_csv(data_file)




cause_category_summary = df.groupby("Cause category").agg(
    count=("Count", "count"),
    mean=("Count", "mean"),
    median=("Count", "median")
)


city_summary = df.groupby("Million Plus Cities").agg(
    count=("Count", "count"),
    mean=("Count", "mean"),
    median=("Count", "median")
)


print("\nTrends and patterns by Cause category:\n")
print(cause_category_summary)

print("\nTrends and patterns by Million Plus Cities:\n")
print(city_summary)


summary = df.groupby(["Cause category", "Million Plus Cities"]).agg(
    count=("Count", "count"),
    mean=("Count", "mean"),
    median=("Count", "median")
).reset_index()


plt.figure(figsize=(8, 6))
sns.barplot(x="Cause category", y="count", data=summary)
plt.xlabel("Cause Category")
plt.ylabel("Total Incidents")
plt.title("Total Incidents by Cause Category")
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()



pivot_table = df.pivot_table(index="Million Plus Cities", columns="Cause category", values="Count", aggfunc='count')
total_counts = pivot_table.sum()


plt.figure(figsize=(10, 8))
plt.pie(total_counts, labels=total_counts.index, autopct='%1.1f%%')
plt.title("Incidents per Cause Category")
plt.show()


summary = df.groupby("Cause category").agg(
    total_incidents=("Count", "sum")
).reset_index()


plt.figure(figsize=(8, 6))
plt.pie(summary['total_incidents'], labels=summary['Cause category'], autopct='%1.1f%%')
plt.title("Total Incidents by Cause Category")
plt.tight_layout()
plt.show()


cause_category_summary = cause_category_summary.sort_values(by="mean", ascending=False)


print("\nTop 5 cause categories with the highest mean:\n")
print(cause_category_summary.head())


plt.figure(figsize=(8, 6))
sns.barplot(x="Cause category", y="mean", data=cause_category_summary.head())
plt.xlabel("Cause Category")
plt.ylabel("Average Incidents")
plt.title("Top 5 Cause Categories with the Highest Mean")
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()


cause_category_summary = cause_category_summary.sort_values(by="median", ascending=False)


print("\nTop 5 cause categories with the highest median:\n")
print(cause_category_summary.head())


plt.figure(figsize=(8, 6))
sns.barplot(x="Cause category", y="median", data=cause_category_summary.head())
plt.xlabel("Cause Category")
plt.ylabel("Median Incidents")
plt.title("Top 5 Cause Categories with the Highest Median")
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()


threshold = 0.1 * total_counts.sum()
high_risk_causes = total_counts[total_counts > threshold]


print("\nHigh risk cause categories:\n")
print(high_risk_causes)


plt.figure(figsize=(8, 6))
plt.pie(high_risk_causes, labels=high_risk_causes.index, autopct='%1.1f%%')
plt.title("High Risk Cause Categories")
plt.tight_layout()
plt.show()
