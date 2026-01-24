"""
Automated Report Generation using Python and ReportLab
"""

import csv
import statistics
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# File paths
DATA_FILE = "sales_data.csv"
REPORT_FILE = "sales_report.pdf"

# --------------------------------------------------
# Step 1: Create sample data file
# --------------------------------------------------
data = [
    ["Month", "Sales"],
    ["January", 1200],
    ["February", 1500],
    ["March", 1100],
    ["April", 1700],
    ["May", 1600],
]

with open(DATA_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


# --------------------------------------------------
# Step 2: Read and analyze data
# --------------------------------------------------
months = []
sales = []

with open(DATA_FILE, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        months.append(row["Month"])
        sales.append(int(row["Sales"]))

total_sales = sum(sales)
average_sales = statistics.mean(sales)
max_sales = max(sales)
min_sales = min(sales)

# --------------------------------------------------
# Step 3: Generate PDF report
# --------------------------------------------------
doc = SimpleDocTemplate(REPORT_FILE, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("Automated Sales Report", styles["Title"]))
elements.append(Paragraph(
    "This report is automatically generated using Python and the ReportLab library.",
    styles["Normal"]
))

elements.append(Paragraph("Sales Summary", styles["Heading2"]))
elements.append(Paragraph(f"Total Sales: {total_sales}", styles["Normal"]))
elements.append(Paragraph(f"Average Monthly Sales: {average_sales:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Monthly Sales: {max_sales}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Monthly Sales: {min_sales}", styles["Normal"]))

elements.append(Paragraph("Monthly Sales Data", styles["Heading2"]))

table_data = [["Month", "Sales"]] + list(zip(months, sales))
table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
]))

elements.append(table)

doc.build(elements)

print("PDF report generated successfully!")
