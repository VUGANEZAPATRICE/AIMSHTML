from fastapi import FastAPI
import mammoth 
from fastapi import FastAPI, Response,File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,FileResponse
import os

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


#Save the document locally
def save_docx(filebytes : bytes, filename: str):
    with open(f'documents/{filename}', 'wb') as docx:
        docx.write(filebytes)
    

@app.get("/file", response_class=HTMLResponse)
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

@app.post("/file", response_class=HTMLResponse)
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    #Save file
    save_docx(contents, file.filename)

    result = mammoth.convert_to_html(f'documents/{file.filename}')
    messages = result.messages #any messages, such as warnings during conversion

    #return HTML Website
    return contents

@app.get('/translate')
def translate(request: Request):
    files = get_files('templates/html')
    return templates.TemplateResponse("html/output.html", context ={
        "request":request,
        'files': files,
        })
