from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 80, "Hello world")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("/Users/songeamsela/Documents/ITC_Year5/NLP/NLP_TP/TP7_SongEamSela/Quiz1_SongEam "
                                  "Sela.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("/Users/songeamsela/Documents/ITC_Year5/NLP/NLP_TP/TP7_SongEamSela/FromPython.pdf", "wb")
output.write(outputStream)
outputStream.close()