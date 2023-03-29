from bs4 import BeautifulSoup
import mammoth
from deep_translator import GoogleTranslator

with open('output.html', 'r') as f:
    contents = f.read()
soup = BeautifulSoup(contents, 'lxml')
# text_elements = [element for element in soup.find_all() if element.name not in ['script', 'style','img']]
text_elements = [element for element in soup.find_all(string=True) if element.name not in ['script', 'style','img']]
# print(text_elements)
for element in text_elements:
    print(element.name)
    text = element.get_text(strip=True)
    # print(text)
    
    if not text:
        continue
        # # Translate the text
        # translated_text = translator.translate(text, dest='fr').text
        # print(translated_text)
    splitted_text=""
    splitted_list = text.split(".")
    # for splitted in splitted_list:    
    #     # Translate the text
    #     # translated_text = translator.translate(text, dest='fr').text
    #     translator = GoogleTranslator(source='auto', target='rw')
    #     translated_text = translator.translate(splitted)
    #     splitted_text = splitted_text+translated_text
    print(splitted_text)
    # Replace the text in the element
    # element.string.replace_with(splitted_text)
print("**********************************************************************************")            
# print(TraverseTags)
print("=============================================================================================================")
print("DONE")
 
# from bs4 import BeautifulSoup

# # Sample HTML code
# html = """
# <html>
# <head>
# <title>Sample Page</title>
# </head>
# <body>
# <h1>Welcome to my page!</h1>
# <p>This is a sample paragraph.</p>
# <ul>
#   <li>Item 1</li>
#   <li>Item 2</li>
#   <li>Item 3</li>
# </ul>
# <img src="image.jpg" alt="Sample Image">
# <style>
#   h1 {
#     color: red;
#   }
# </style>
# <script>
#   alert('Hello, World!');
# </script>
# <link rel="stylesheet" href="style.css">
# </body>
# </html>
# """

# # Create BeautifulSoup object
# soup = BeautifulSoup(html, 'html.parser')

# # Loop through all HTML tags (excluding certain ones) and change their text contents
# for tag in soup.find_all(lambda tag: tag.name not in ['style', 'script', 'link']):
#     tag.string = f'{tag.name} has been modified'

# # Access an image tag and replace it
# img = soup.find('img')
# img['src'] = 'new_image.jpg'
# img['alt'] = 'New Image'

# # Save modified HTML code to a file
# with open('modified_page.html', 'w') as file:
#     file.write(str(soup))


# ===============================================================================

# from bs4 import BeautifulSoup

# # Sample HTML code
# html = """
# <html>
# <head>
# <title>Sample Page</title>
# </head>
# <body>
# <h1>Welcome to my page!</h1>
# <p>This is a sample paragraph.</p>
# <ul>
#   <li>Item 1</li>
#   <li>Item 2</li>
#   <li>Item 3</li>
# </ul>
# <img src="image.jpg" alt="Sample Image">
# <style>
#   h1 {
#     color: red;
#   }
# </style>
# <script>
#   alert('Hello, World!');
# </script>
# <link rel="stylesheet" href="style.css">
# </body>
# </html>
# """

# # Create BeautifulSoup object
# soup = BeautifulSoup(html, 'html.parser')

# # Loop through all HTML tags (excluding certain ones) and print their text contents
# for tag in soup.find_all(lambda tag: tag.name not in ['style', 'script', 'link']):
#     print(f"Before modifying: {tag.text}")
#     tag.string = f'{tag.name} has been modified'
#     print(f"After modifying: {tag.text}")

# # Access an image tag and replace it
# img = soup.find('img')
# img['src'] = 'new_image.jpg'
# img['alt'] = 'New Image'

# # Save modified HTML code to a file
# with open('modified_page.html', 'w') as file:
#     file.write(str(soup))
