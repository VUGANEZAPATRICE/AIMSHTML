# from bs4 import BeautifulSoup
# import aspose.words as aw
# import mammoth
# from googletrans import Translator
# from deep_translator import GoogleTranslator
# translator=Translator()

# def docxTohtml(filePath):
#     # Convert a Word Document to HTML in Python
#     # pip install aspose-words

#     # Load the document from disk
#     doc = aw.Document(f"{filePath}")

#     # Enable export of fonts
#     options = aw.saving.HtmlSaveOptions()
#     options.export_font_resources = True
    
#     # Save the document as HTML
#     return doc.save("datahtml/Doc1.html", options)
  

# def convertTo_html(filePath):
#     # with open(f"document.docx", "rb") as docx_file:
#     with open(f"{filePath}", "rb") as docx_file:
#         result = mammoth.convert_to_html(docx_file)
#         html = result.value #the generated html
#         messages = result.messages #any messages, such as warnings during conversion
#         with open('data/output.html', 'w', encoding= 'utf-8') as htmlFile:
#             # htmlFile.write(result.value)
#             htmlFile.write(html)
            
# # filePath ="C:/Users/Vugatri/Documents/AIMSHTML/data/COMPUTER_BASICS_HANDOUT.docx"
# # convertTo_html(filePath)

# def convertHTML_to_Docx(ttt):
#     # import aspose.words as aw
#     doc = aw.Document(f"{ttt}")
#     return doc.save("Output.docx")

# # convertHTML_to_Docx("output.html")    


# with open('output.html', 'r') as f:

#     contents = f.read()

# soup = BeautifulSoup(contents, 'lxml')

# # print(soup.h2)
# # print(soup.head)
# # print(soup.li)
# # print(f'HTML: {soup.h2}, name: {soup.h2.name}, text: {soup.h2.text}')


# # 54-----------60



# # count2=0
# # count3=0
# # for TraverseTags in soup.recursiveChildGenerator():
# #     if TraverseTags.name not in ['script', 'style','img']:
# #         # print("==================================================")
# #         kk=TraverseTags.name
# #         # count3=count3+1
# #         if TraverseTags.name is not None:
# #             print(TraverseTags.name)
# #             text = TraverseTags.text.strip()
# #             print(text)
# #             if not text:
# #                 continue
# #             splitted_text=""
# #             splitted_list = text.split(".")
# #             for splitted in splitted_list:    
# #                 # Translate the text
# #                 # translated_text = translator.translate(text, dest='fr').text
# #                 translator = GoogleTranslator(source='auto', target='rw')
# #                 translated_text = translator.translate(splitted)
# #                 splitted_text = splitted_text+translated_text
# #             print(splitted_text)
# #             # TraverseTags.string.replace_with(translated_text)
# #             # TraverseTags.string.replace_with(splitted_text)
# #             TraverseTags.string =splitted_text
# #         print("**********************************************************************************")            
# #         print(TraverseTags)
# #         print("=============================================================================================================")
# # print("DONE")
 
            
# #             count2=count2+1
# # print(count2)
# # print(count3) 

# # page_tag = [element for element in soup.find_all() if element.name  ]
# # count1=0
# # for elt in page_tag:
# #     # print(elt.name)
# #     if elt.name == "img":
# #         count1= count1+1
# # ==================================================================================================


# # 104-------------107


# #text_elements = [element for element in soup.find_all(string=True) if element.name not in ['script', 'style','img']]
# text_elements = [element for element in soup.find_all() if element.parent.name not in ['script', 'style','img']]
# for element in text_elements:
#     text = element.get_text(strip=True)
#     # print(text)
    
#     if not text:
#         continue
#         # # Translate the text
#         # translated_text = translator.translate(text, dest='fr').text
#         # print(translated_text)
#     splitted_text=""
#     splitted_list = text.split(".")
#     for splitted in splitted_list:    
#         # Translate the text
#         # translated_text = translator.translate(text, dest='fr').text
#         translator = GoogleTranslator(source='auto', target='rw')
#         translated_text = translator.translate(splitted)
#         splitted_text = splitted_text+translated_text
#     print(splitted_text)
#     # Replace the text in the element
#     element.string.replace_with(splitted_text)
# print("**********************************************************************************")            
# # print(TraverseTags)
# print("=============================================================================================================")
# print("DONE")
 

    
#     # ======================================================================================================
#     # ==============================================================================================================
    
# # import translators as ts
# # from deep_translator import GoogleTranslator
# # from deep_translator import DeeplTranslator
# # q_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
# # q_html = '''<!DOCTYPE html><html><head><title>《季姬击鸡记》</title></head><body><p>还有另一篇文章《施氏食狮史》。</p></body></html>'''

# # ### usage
# # # ts.preaccelerate()  # Optional. Caching sessions in advance, which can help improve access speed.


# # # translators
# # # =================================================


# # # print(ts.translators_pool)
# # print(ts.translate_text(q_text))
# # # ts.translate_html(q_html, translator: str = 'bing', from_language: str = 'auto', to_language: str = 'en', n_jobs: int = -1, if_use_preacceleration: bool = False, **kwargs)
# # # print(help(ts.translate_html))
# # # print(ts.translate_text(q_text, translator: str = 'alibaba', from_language: str = 'en', to_language: str = 'de', **kwargs))
# # print(ts.translate_html(q_html, to_language='fr'))


# # deep-translator
# # =================================================

# # translator = GoogleTranslator(source='auto', target='rw')
# # # perform actual translation
# # print(translator.translate("Welcome to our tutorial!"))

# # print("==========================================================")
# # res = ts.google('Welcome to our tutorial!', to_language='fr')
# # print(res)

# # translator2 = DeeplTranslator(source='auto', target='de')
# # # perform actual translation
# # print(translator2.translate("Welcome to our tutorial!"))
# # usage 
# # from deep_translator import (GoogleTranslator,
# #                              MicrosoftTranslator,
# #                              PonsTranslator,
# #                              LingueeTranslator,
# #                              MyMemoryTranslator,
# #                              YandexTranslator,
# #                              PapagoTranslator,
# #                              DeeplTranslator,
# #                              QcriTranslator,
# #                              single_detection,
# #                              batch_detection)







# 107=======135