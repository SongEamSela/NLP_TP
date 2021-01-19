import docx

# /Users/songeamsela/Documents/ITC_Year5/SongEam_Sela_MT.docx

def readtxt(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    fullText.append("\n Add more text to Word Document")
    return '\n'.join(fullText)

print(readtxt('/Users/songeamsela/Documents/ITC_Year5/SongEam_Sela_MT.docx'))