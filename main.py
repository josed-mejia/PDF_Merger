import PyPDF2

from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def agregar_archivo(merger, archivos):
    archivo_pdf = filedialog.askopenfilename(filetypes=(("Archivo PDF", ".pdf"), ("All files", "*")))
    if not archivo_pdf.endswith(".pdf"):
        print("Archivo no es PDF")
    elif archivo_pdf != "":
        print("merged")
        merger.append(archivo_pdf)

    for label in archivos:
        if label.cget("text") == "-----------------":
            label.configure(text=archivo_pdf)
            break


root = Tk()
root.title("Unir archivos PDF")

marco = ttk.Frame(root, padding=20)
marco.grid()

pdf_merger = PyPDF2.PdfFileMerger()

nuevo_nombre_pdf = "merged.pdf"

labels_archivos = []
cantidad_archivos = 10

for _ in range(cantidad_archivos):
    labels_archivos.append(ttk.Label(marco, text="-----------------"))

marco.columnconfigure(0, weight=1)
marco.columnconfigure(1, weight=10)
marco.columnconfigure(2, weight=30)

for row in range(11):
    marco.rowconfigure(row, weight=1)

boton_buscar = ttk.Button(marco, text="Buscar archivo", command=lambda: agregar_archivo(pdf_merger, labels_archivos))
boton_buscar.configure(width=15)
boton_buscar.grid(column=1, row=4)

boton_crear = ttk.Button(marco, text="Crear archivo", command=lambda: pdf_merger.write(nuevo_nombre_pdf))
boton_crear.configure(width=15)
boton_crear.grid(column=1, row=6)

for row in range(cantidad_archivos):
    labels_archivos[row].grid(column=2, row=1 + row)
marco.mainloop()
