from flask import Flask, render_template, request, jsonify
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' in request.files:
        pdf_file = request.files['pdf']
        if pdf_file.filename != '':
            pdf_text = extract_text_from_pdf(pdf_file)
            return jsonify({'success': True, 'text': pdf_text})
    
    return jsonify({'success': False, 'error': 'No PDF file uploaded'})

def extract_text_from_pdf(pdf_file):
    text = ''
    try:
        pdf_reader = PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    except Exception as e:
        text = f'Error: {str(e)}'
    return text

if __name__ == '__main__':
    app.run(debug=True)



    
