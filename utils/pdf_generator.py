from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_report(patient_name, score, disease, graph_path="graph.png", filename="Cardio_Report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "CardioNexa AI - Heart Health Report")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, 710, f"Patient Name: {patient_name}")
    c.drawString(50, 690, f"Heart Health Score: {score}%")
    c.drawString(50, 670, f"Predicted Disease: {disease}")
    
    c.drawImage(graph_path, 50, 500, width=200, height=200)
    c.save()
    return filename

