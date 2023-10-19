from pyfpdf import FPDF

pdf = FPDF(orientation="P",unit="mn",format="A4")

print(type(pdf))

pdf.add_pages()

pdf.output("output.pdf")
