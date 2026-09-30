import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create output directory
output_dir = "visualizations"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load dataset
print("Loading Titanic dataset...")
df = sns.load_dataset('titanic')

# Set style
sns.set_theme(style="whitegrid", palette="muted")

# Plot 1: Survival Rate (Donut Chart)
print("Generating Plot 1...")
plt.figure(figsize=(8, 6))
survival_counts = df['survived'].value_counts()
plt.pie(survival_counts, labels=['Did Not Survive', 'Survived'], autopct='%1.1f%%', 
        startangle=90, colors=['#ff9999','#66b3ff'], wedgeprops=dict(width=0.4))
plt.title('Overall Survival Rate on the Titanic', fontsize=16)
plt.tight_layout()
plt.savefig(f"{output_dir}/1_survival_rate.png", dpi=300)
plt.close()

# Plot 2: Survival by Class and Gender (Barplot)
print("Generating Plot 2...")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x="pclass", y="survived", hue="sex", data=df, errorbar=None)
plt.title('Survival Probability by Passenger Class and Gender', fontsize=16)
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Survival Probability', fontsize=12)
ax.set_xticklabels(['1st Class', '2nd Class', '3rd Class'])
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig(f"{output_dir}/2_survival_by_class_gender.png", dpi=300)
plt.close()

# Plot 3: Age Distribution of Survivors vs Non-Survivors (Violin Plot)
print("Generating Plot 3...")
plt.figure(figsize=(10, 6))
sns.violinplot(x="survived", y="age", data=df, hue="survived", palette={0: "#ff9999", 1: "#66b3ff"}, inner="quart")
plt.title('Age Distribution by Survival Status', fontsize=16)
plt.xlabel('Survival Status', fontsize=12)
plt.ylabel('Age', fontsize=12)
plt.xticks([0, 1], ['Did Not Survive', 'Survived'])
plt.tight_layout()
plt.savefig(f"{output_dir}/3_age_distribution.png", dpi=300)
plt.close()

# Plot 4: Fare Distribution by Passenger Class (Box Plot with Swarm)
print("Generating Plot 4...")
plt.figure(figsize=(12, 7))
sns.boxplot(x="pclass", y="fare", data=df, fliersize=0, color='lightgray')
sns.stripplot(x="pclass", y="fare", data=df, hue="survived", palette={0: "#ff9999", 1: "#66b3ff"}, alpha=0.6, jitter=True)
plt.title('Fare Distribution by Passenger Class', fontsize=16)
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Fare', fontsize=12)
plt.ylim(-10, df['fare'].quantile(0.95)) # limit y-axis to remove extreme outliers for better visibility
plt.legend(title='Survived', labels=['No', 'Yes'], loc='upper right')
plt.tight_layout()
plt.savefig(f"{output_dir}/4_fare_distribution.png", dpi=300)
plt.close()

# Plot 5: Correlation Heatmap of Numerical Features
print("Generating Plot 5...")
plt.figure(figsize=(10, 8))
# Select numerical columns
num_cols = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, linewidths=.5)
plt.title('Correlation Heatmap of Numerical Features', fontsize=16)
plt.tight_layout()
plt.savefig(f"{output_dir}/5_correlation_heatmap.png", dpi=300)
plt.close()

print("All visualizations generated successfully in the 'visualizations' folder.")
