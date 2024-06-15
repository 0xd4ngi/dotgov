from flask import Flask, send_file, request, render_template_string
import os
from scraper import scrape_website
from pdf_generator import save_to_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Daily Updates</h1>
        <p>Click the button below to generate and download the latest updates in PDF format:</p>
        <form action="/generate" method="post">
            <button type="submit">Generate PDF</button>
        </form>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    url = 'https://www.india.gov.in'  # Replace with target website URL
    updates = scrape_website(url)
    save_to_pdf(updates, 'daily_updates.pdf')
    return '''
        <h1>PDF Generated</h1>
        <p>Your PDF has been generated. Click the link below to download:</p>
        <a href="/download">Download Updates</a>
    '''

@app.route('/download')
def download():
    file_path = 'daily_updates.pdf'
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'No updates available', 404

if __name__ == '__main__':
    app.run(debug=True)
