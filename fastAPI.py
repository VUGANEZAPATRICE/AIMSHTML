from fastapi import FastAPI
import mammoth 
from fastapi import FastAPI, Response,File, UploadFile
from fastapi.responses import HTMLResponse,FileResponse
import os


app = FastAPI()


@app.get("/file", response_class=HTMLResponse)
def upload_file_form(file: str):
    return """
    <form method="post" action="/file">
    <!-- upload of a single file -->
    <p>
        <label>Add file (single): </label><br/>
        <input type="file" name="example1"/>
    </p>

    <p>
        <input type="submit"/>
    </p>
</form>
    """

@app.post("/file1", response_class=HTMLResponse)
def upload_file(file: str):
    # with open(f"document.docx", "rb") as docx_file:
    with open(file.filename, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value #the generated html
        messages = result.messages #any messages, such as warnings during conversion
        with open('output.html', 'w', encoding= 'utf-8') as htmlFile:
            # htmlFile.write(result.value)
            htmlFile.write(html)
        with open('output.html', 'rb') as fh:
          data = fh.read()

    # Do here your stuff with the file
    return Response(content=data, media_type="text/html")


@app.post("/file")
# async def root(file: UploadFile= File(...)):
    # with open(f"document.docx", "rb") as docx_file:
    #with open(file.filename, "rb") as docx_file:
def file_resp():
    path="C:/Users/Vugatri/Documents/fastapi"
    file_path = os.path.join(path, 'output.html')
    # if os.path.exists(file_path):
    return FileResponse(file_path)
    


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}