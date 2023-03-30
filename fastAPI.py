from fastapi import FastAPI
import mammoth 
from fastapi import FastAPI, Response,File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,FileResponse
import os

from bs4 import BeautifulSoup
import aspose.words as aw
import mammoth
from googletrans import Translator
from deep_translator import GoogleTranslator
translator=Translator()
from bs4 import BeautifulSoup

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


#Save the document locally
def save_docx(filebytes : bytes, filename: str):
    with open(f'assets/doc/{filename}', 'wb') as docx:
        docx.write(filebytes)

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def docxToHtml(filePath):
    doc = aw.Document(f"{filePath}")
    # Enable export of fonts
    options = aw.saving.HtmlSaveOptions()
    options.export_font_resources = True
    # Save the document as HTML
    return doc.save(f'assets/html/{filePath}.html', options)

def translate_html(file):
    translator = GoogleTranslator(source='auto', target='rw')
    with open(f'assets/html/{file[:-4]}.html', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    text_elements = [element for element in soup.find_all(string=True) if element.parent and element.parent.name not in ['script', 'style']]
    print(text_elements)
    for element in text_elements:
        # Extract the text from the element
        text = element.get_text(strip=True)
        # Skip the element if it's empty
        if not text or text=="":
            continue
        splitted_text=""
        for splitted in text.split("."):
            # Translate the text
            try:
                translated_text = translator.translate(splitted)
            except:
                pass
            splitted_text = splitted_text+translated_text
        print(splitted_text)
        
        element.string.replace_with(str(splitted_text))
    # Save modified HTML code to a file
    with open(f'assets/html/tran/{file}.html', 'w') as f:
        f.write(str(soup))

def convert_html_to_doc(path):
    # import aspose.words as aw
    doc = aw.Document(f"assets/html/tran/{path[:-4]}.html")
    return doc.save(f"assets/doc/tran/{path}.docx")

@app.get("/", response_class=HTMLResponse)
def upload_file_form():
    return """
    <form method="post" action="/file" enctype="multipart/form-data">
    <!-- upload of a single file -->
    <p>
        <label>Add file (single): </label><br/>
        <input type="file" name="file"/>
    </p>

    <p>
        <input type="submit"/>
    </p>
</form>
"""

@app.post("/", response_class=HTMLResponse)
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    docxToHtml(file)
    translate_html(file)

    return contents

@app.get('/translate')
def translate(request: Request):
    files = get_files('templates/html')
    return templates.TemplateResponse("html/output.html", context ={
        "request":request,
        'files': files,
        })
