# okurmen/utils.py
import io  # добавим эту строку для импорта модуля io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_receipt(student):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Add your receipt content here
    p.drawString(100, 750, f"Receipt for {student.name}")
    p.drawString(100, 730, f"Student Number: {student.number}")
    p.drawString(100, 710, f"Payment Amount: {student.payment}")
    p.drawString(100, 690, f"Payment Date: {student.payment_date}")
    p.drawString(100, 670, f"Manager: {student.manager.name}")

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Buffer is now a PDF file-like object
    buffer.seek(0)
    return buffer

