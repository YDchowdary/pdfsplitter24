from pdfrw import PdfReader, PdfWriter
import glob

arr = [f for f in glob.glob("*.pdf")]


for i in arr:
	pages = PdfReader(i).pages
	parts = [(1,2),(2,3),(3,4)]
	for part in parts:
		outdata = PdfWriter(f'out/{i}_{part[0]}.pdf')
		for pagenum in range(*part):
			outdata.addpage(pages[pagenum-1])
		outdata.write()







#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory


#pageNumbers = pdf_reader.getNumPages()
#for i in range (pageNumbers):
