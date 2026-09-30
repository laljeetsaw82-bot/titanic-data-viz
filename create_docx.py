import docx
from docx.shared import Inches
import os

doc = docx.Document()

doc.add_heading('Advanced Data Visualization and Storytelling with Python: The Titanic Dataset', 0)

doc.add_heading('1. Introduction', level=2)
doc.add_paragraph('This report explores the factors influencing passenger survival on the Titanic, one of the most famous maritime disasters in history. The objective is to uncover patterns and tell a compelling data story through visual analysis, making complex survival demographics accessible to a non-technical audience. By analyzing attributes such as passenger class, gender, age, and fare, we can understand the socio-economic and demographic dynamics that played a role in survival rates.')

doc.add_heading('2. Methods', level=2)
p = doc.add_paragraph()
p.add_run('Dataset Selection: ').bold = True
p.add_run('We utilized the publicly accessible "Titanic" dataset, which contains demographic and travel information for a subset of the passengers.\n')
p.add_run('Tools & Libraries: ').bold = True
p.add_run('The analysis was conducted using Python. Data manipulation was performed with pandas, and visualizations were generated using matplotlib and seaborn.\n')
p.add_run('Data Preprocessing: ').bold = True
p.add_run("The dataset was loaded directly via seaborn.load_dataset('titanic'). Missing values were handled inherently by the plotting functions (e.g., ignoring NaN values during aggregation).\n")
p.add_run('Visual Strategy: ').bold = True
p.add_run('We employed a variety of chart types—donut charts, grouped bar charts, violin plots, box plots with strip plots, and correlation heatmaps—to ensure the most appropriate and effective representation for different types of data relationships.')

doc.add_heading('3. Visual Analyses', level=2)

# Viz 1
doc.add_heading('3.1. The Baseline: Overall Survival Rate', level=3)
img1 = r"C:\Users\USER\.gemini\antigravity\brain\b0d76503-5ee8-42c2-bb36-f24b50e37b41\1_survival_rate.png"
if os.path.exists(img1):
    doc.add_picture(img1, width=Inches(5.0))
p1 = doc.add_paragraph()
p1.add_run('Visual Choice & Reasoning: ').bold = True
p1.add_run('A donut chart was selected to represent the part-to-whole relationship of the overall survival rate. It provides an immediate, intuitive grasp of the grim reality of the disaster without requiring the audience to interpret complex axes.\n')
p1.add_run('Narrative Contribution: ').bold = True
p1.add_run('This establishes the baseline for our story. It highlights that surviving the Titanic was the exception, not the rule, setting a dramatic stage for exploring who exactly made up that 38.4%.')

# Viz 2
doc.add_heading('3.2. The Impact of Socio-Economic Status and Gender', level=3)
img2 = r"C:\Users\USER\.gemini\antigravity\brain\b0d76503-5ee8-42c2-bb36-f24b50e37b41\2_survival_by_class_gender.png"
if os.path.exists(img2):
    doc.add_picture(img2, width=Inches(5.0))
p2 = doc.add_paragraph()
p2.add_run('Visual Choice & Reasoning: ').bold = True
p2.add_run('A grouped bar chart is ideal for comparing a categorical outcome (survival probability) across two independent categorical variables (Passenger Class and Gender). The color-coding makes the gender disparity immediately obvious within each class.\n')
p2.add_run('Narrative Contribution: ').bold = True
p2.add_run('This visualization enhances the narrative by revealing the "women and children first" protocol and the distinct advantage of wealth. We see that women in 1st and 2nd class had overwhelmingly high survival rates, whereas men in 3rd class had the lowest. This highlights the stark inequalities present during the evacuation.')

# Viz 3
doc.add_heading('3.3. Age Demographics of Survival', level=3)
img3 = r"C:\Users\USER\.gemini\antigravity\brain\b0d76503-5ee8-42c2-bb36-f24b50e37b41\3_age_distribution.png"
if os.path.exists(img3):
    doc.add_picture(img3, width=Inches(5.0))
p3 = doc.add_paragraph()
p3.add_run('Visual Choice & Reasoning: ').bold = True
p3.add_run('A violin plot was chosen because it effectively shows both the summary statistics (like a box plot) and the full probability density of the age distribution for both survivors and non-survivors.\n')
p3.add_run('Narrative Contribution: ').bold = True
p3.add_run('This chart adds depth to our understanding of the victims and survivors. The wider base on the "Survived" plot for younger ages indicates a higher survival rate for children. Conversely, the bulk of the non-survivors were young adults in their 20s and 30s, adding a poignant human element to the data story.')

# Viz 4
doc.add_heading('3.4. Financial Disparities: Fare and Class', level=3)
img4 = r"C:\Users\USER\.gemini\antigravity\brain\b0d76503-5ee8-42c2-bb36-f24b50e37b41\4_fare_distribution.png"
if os.path.exists(img4):
    doc.add_picture(img4, width=Inches(5.0))
p4 = doc.add_paragraph()
p4.add_run('Visual Choice & Reasoning: ').bold = True
p4.add_run('A combination of a box plot and a swarm/strip plot was used. The box plot shows the statistical distribution (median, quartiles) of fares within each class, while the overlaying colored points represent individual passengers, colored by survival.\n')
p4.add_run('Narrative Contribution: ').bold = True
p4.add_run('This visualization confirms the correlation between fare paid and passenger class, but more importantly, it visually clusters the survivors. We can physically see a higher density of blue (survived) dots in the higher fare ranges and 1st class, reinforcing the socio-economic narrative from a financial perspective.')

# Viz 5
doc.add_heading('3.5. Interconnected Variables: A Holistic View', level=3)
img5 = r"C:\Users\USER\.gemini\antigravity\brain\b0d76503-5ee8-42c2-bb36-f24b50e37b41\5_correlation_heatmap.png"
if os.path.exists(img5):
    doc.add_picture(img5, width=Inches(5.0))
p5 = doc.add_paragraph()
p5.add_run('Visual Choice & Reasoning: ').bold = True
p5.add_run('A correlation heatmap was selected to simultaneously display the linear relationships between all numerical variables in the dataset. Red indicates positive correlation, while blue indicates negative correlation.\n')
p5.add_run('Narrative Contribution: ').bold = True
p5.add_run('This final visualization acts as a quantitative summary. It statistically confirms our earlier visual findings: survival is negatively correlated with passenger class (lower class number = higher survival chance) and positively correlated with fare. It also reveals other relationships, such as the strong correlation between siblings/spouses (sibsp) and parents/children (parch), indicating family travel patterns.')

doc.add_heading('4. Conclusions', level=2)
doc.add_paragraph('The visual analysis of the Titanic dataset reveals a compelling story of survival dictated heavily by socio-economic status and gender. The data clearly shows that being female, being in a higher passenger class, and paying a higher fare significantly increased a passenger\'s chances of surviving the disaster. The "women and children first" maritime tradition is visible in the data, but it is heavily skewed by class disparities.')

doc.add_heading('5. Potential Business or Scientific Implications', level=2)
doc.add_paragraph('Risk Management & Protocol Design: Historically, these insights led to sweeping changes in maritime safety regulations (e.g., requiring lifeboats for all passengers). In a modern business context, similar analyses of disaster or failure data are crucial for developing robust emergency protocols and mitigating risk.', style='List Bullet')
doc.add_paragraph('Resource Allocation: Understanding how different demographic groups are affected during a crisis allows organizations to better allocate emergency resources and design targeted interventions.', style='List Bullet')
doc.add_paragraph('Customer Segmentation: In a commercial setting (unrelated to disasters), the techniques used here (analyzing behavior/outcomes by class, age, and spend) are identical to customer segmentation models used for targeted marketing and understanding customer lifetime value based on purchasing tiers.', style='List Bullet')

doc.save(r"C:\Users\USER\Downloads\websites\Week2_Report.docx")
print("DOCX generated successfully.")
