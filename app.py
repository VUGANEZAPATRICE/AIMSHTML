# # Convert a Word Document to HTML in Python
# # pip install aspose-words

# import aspose.words as aw
# # Load the document from disk
# doc = aw.Document("data/Doc1.docx")

# # Enable export of fonts
# options = aw.saving.HtmlSaveOptions()
# options.export_font_resources = True
  
# # Save the document as HTML
# doc.save("datahtml/Doc1.html", options)

# translating html file contents into another language
# ===================================================================================


from googletrans import Translator
from bs4 import BeautifulSoup, Tag,NavigableString
html = open("datahtml/Document.html").read()
soup = BeautifulSoup(html)
translator=Translator()

text_elements = [element for element in soup.find_all(string=True) if element.parent.name not in ['script', 'style']]

for element in text_elements:
    # Extract the text from the element
    text = element.get_text(strip=True)
    # Skip the element if it's empty
    if not text:
        continue
    # Translate the text
    translated_text = translator.translate(text, dest='fr').text
    
    # print(translated_text)
    # Replace the text in the element
    element.replace_with(translated_text)