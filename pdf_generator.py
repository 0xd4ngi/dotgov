from fpdf import FPDF

def save_to_pdf(data, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for url, updates in data.items():
        pdf.cell(200, 10, txt=f"Updates from {url}:", ln=True)
        if updates:
            for item in updates:
                pdf.cell(200, 10, txt=item, ln=True)
        else:
            pdf.cell(200, 10, txt="No updates till last day", ln=True)
        pdf.cell(200, 10, txt="", ln=True)  # Add a blank line between different websites

    pdf.output(file_name)
