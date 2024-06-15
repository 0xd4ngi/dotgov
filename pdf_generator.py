from fpdf import FPDF

def save_to_pdf(data, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    if data:
        for item in data:
            pdf.cell(200, 10, txt=item, ln=True)
    else:
        pdf.cell(200, 10, txt="No updates till last day", ln=True)

    pdf.output(file_name)
