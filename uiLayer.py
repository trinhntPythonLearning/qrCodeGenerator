import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import logicHandler as logic


class Window:
    def __init__(self) -> None:
        self.ui = tk.Tk()
        self.ui.geometry('350x300')
        self.ui.title('QRCode Generator')

    def configUI(self) -> None:
        # QR Input
        qrTitle = tk.Label(self.ui, text='QR Text')
        qrTitle.grid(row=0, column=0)

        self.qrText = tk.StringVar()
        qrInput = tk.Entry(self.ui, textvariable=self.qrText)
        self.qrText.trace('w', callback=self.onQRTextChanged)
        qrInput.grid(row=0, column=1)

        # Generate Button
        self.genBtn = tk.Button(self.ui, text='Generate',
                                command=self.onGenBtnClicked)
        self.genBtn['state'] = tk.DISABLED
        self.genBtn.grid(row=1, column=1)

        # QR Image
        self.qrItem = None

        # Download Button
        self.downloadBtn = tk.Button(
            self.ui, text='Download', command=self.onDownloadBtnClicked)

    def run(self) -> None:
        print('Run App')

        self.configUI()
        self.ui.mainloop()

    # Event handler
    def onQRTextChanged(self, *args) -> None:
        stdText = self.qrText.get().strip()
        if stdText == '':
            self.genBtn['state'] = tk.DISABLED
        else:
            self.genBtn['state'] = tk.NORMAL

    def onGenBtnClicked(self) -> None:
        qrTxt = self.qrText.get()
        print('Geneate QR: ', qrTxt)

        self.qrItem = logic.genQRCode(qrTxt)

        # Display QRCode Item
        pilImg = self.qrItem.make_image(fill_color='black', back_color='white')
        pilImg = pilImg.resize((150, 150))
        self.tkImage = ImageTk.PhotoImage(pilImg.convert('RGB'))
        qrImgLabel = tk.Label(self.ui, image=self.tkImage)
        qrImgLabel.grid(row=2, column=1)

        # Show Download button
        self.downloadBtn.grid(row=3, column=1)

    def onDownloadBtnClicked(self) -> None:
        fileName = filedialog.asksaveasfilename(defaultextension='.png')
        if fileName:
            logic.saveQRCode(self.qrItem, fileName)
