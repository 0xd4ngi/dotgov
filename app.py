from flask import Flask, send_file, request
import os
from scraper import scrape_multiple_websites
from pdf_generator import save_to_pdf

app = Flask(__name__)

# List of websites to scrape
websites = [
    {'url': 'https://www.eci.gov.in/', 'class_name': 'update-class1'},
    {'url': 'https://www.pmindia.gov.in/en/', 'class_name': 'update-class2'},
    {'url': 'https://www.mha.gov.in/en', 'class_name': 'update-class2'},
    {'url': 'https://www.india.gov.in/', 'class_name': 'update-class2'},
    # {'url': 'https://www.meity.gov.in/', 'class_name': 'update-class2'},
    # {'url': 'https://sansad.in/ls', 'class_name': 'update-class2'},
    # {'url': 'https://sansad.in/rs', 'class_name': 'update-class2'},
    # {'url': 'https://cvc.gov.in/', 'class_name': 'update-class2'},
    # {'url': 'https://bprd.nic.in/', 'class_name': 'update-class2'},
    # {'url': 'https://ncrb.gov.in/', 'class_name': 'update-class2'},
    # {'url': 'https://i4c.mha.gov.in/', 'class_name': 'update-class2'},
    # {'url': 'https://www.drdo.gov.in/drdo/', 'class_name': 'update-class2'},
    # {'url': 'https://www.mea.gov.in/', 'class_name': 'update-class2'},
    # {'url': 'https://dopt.gov.in/ ', 'class_name': 'update-class2'},


    # Add more websites and their corresponding class names here
]

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
    updates = scrape_multiple_websites(websites)
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
