import PyPDF2
import tkinter as tk
from tkinter import filedialog

def merge_pdfs(pdf_list, page_order, output):
    pdf_writer = PyPDF2.PdfWriter()

    for index in page_order:
        pdf = pdf_list[int(index) - 1]
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def select_pdfs():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    pdf_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")], title="Select PDFs to merge")
    if pdf_files:
        print("Selected files:")
        for i, pdf in enumerate(pdf_files, start=1):
            print(f"{i}: {pdf}")

        order_input = input("Enter the order of pages from the selected files (e.g., 1 2 3 1 2): ")
        page_order = order_input.split()

        output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save merged PDF as")
        if output_pdf:
            merge_pdfs(pdf_files, page_order, output_pdf)
            print(f"PDFs merged into {output_pdf}")

if __name__ == "__main__":
    select_pdfs()
