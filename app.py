from bs4 import BeautifulSoup
import aspose.words as aw
import mammoth
from googletrans import Translator
from deep_translator import GoogleTranslator
translator=Translator()
from bs4 import BeautifulSoup

#  from docx to html

def docxTohtml(filePath):
    doc = aw.Document(f"{filePath}")
    # Enable export of fonts
    options = aw.saving.HtmlSaveOptions()
    options.export_font_resources = True
    # Save the document as HTML
    return doc.save("dataFolder/Doc1.html", options)


file_path = 'C:/Users/Vugatri/Documents/vscodeAIMS/data/COMPUTER_BASICS_HANDOUT.docx'
file1 = docxTohtml(file_path)

# Translating from english to kinyarwanda

def translated_html():
    translator = GoogleTranslator(source='auto', target='rw')

    with open('dataFolder/Doc1.html', 'r') as f:
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
    with open('dataFolder/modified_page1.html', 'w') as file:
        file.write(str(soup))
    
#  ================================================================================================================================
   
# # Translate from a file:
# translated = GoogleTranslator(source='auto', target='german').translate_file('C:/Users/Vugatri/Documents/fastapi/dataFolder/Computer_Basics_Student_Manual.docx')
# print(translated)

#  convert back to docx file
def convertHTML_to_Docx(pathOut):
    # import aspose.words as aw
    doc = aw.Document(f"{pathOut}")
    return doc.save("dataFolder/output/Output.docx")

path = 'dataFolder/modified_page1.html'

convertHTML_to_Docx(pathOut=path)



