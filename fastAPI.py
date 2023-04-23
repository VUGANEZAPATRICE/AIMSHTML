'''
    Server side for document translation
'''
import os
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from bs4 import BeautifulSoup
import aspose.words as aw
from googletrans import Translator
from deep_translator import GoogleTranslator
translator = Translator()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Save the document locally
def save_docx(filebytes: bytes, filename: str):
    with open(f'assets/doc/{filename}', 'wb') as docx:
        docx.write(filebytes)


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def docxToHtml(file):
    doc = aw.Document(f"assets/doc/{file}")
    options = aw.saving.HtmlSaveOptions()
    options.export_font_resources = True
    return doc.save(f'assets/html/{file[:-5]}.html', options)


def translate_html(file):
    translator = GoogleTranslator(source='auto', target='rw')
    with open(f'assets/html/{file[:-5]}.html', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    text_elements = [element for element in soup.find_all(
        string=True) if element.parent and element.parent.name not in ['script', 'style']]
    print(text_elements)
    for element in text_elements:
        # Extract the text from the element
        text = element.get_text(strip=True)
        # Skip the element if it's empty
        if not text or text == "":
            continue
        splitted_text = ""
        for splitted in text.split("."):
            # Translate the text
            try:
                translated_text = translator.translate(splitted)
            except:
                pass
            splitted_text = f'{splitted_text} {translated_text}'
        print(splitted_text)

        element.string.replace_with(str(splitted_text))
    # Save modified HTML code to a file
    with open(f'assets/html/tran/{file[:-5]}.html', 'w') as f:
        f.write(str(soup))


def convert_html_to_doc(path):
    doc = aw.Document(f"assets/html/tran/{path[:-5]}.html")
    return doc.save(f"assets/doc/tran/{path[:-5]}.docx")


@app.get("/", response_class=HTMLResponse)
def upload_file_form(request: Request):
    files = get_files('assets/doc/tran')

    return templates.TemplateResponse('index.html', context={
        'request': request,
        'files': files,
    })


@app.post("/", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    save_docx(contents, file.filename)
    docxToHtml(file.filename)
    translate_html(file.filename)
    convert_html_to_doc(file.filename)
    files = get_files('assets/doc/tran')
    return templates.TemplateResponse('index.html', context={
        "request": request,
        'files': files,
        'info': os.stat(file.filename)
    })


@app.get('/translate')
def translate(request: Request):
    files = get_files('templates/html')
    return templates.TemplateResponse("html/output.html", context={
        "request": request,
        'files': files,
    })
