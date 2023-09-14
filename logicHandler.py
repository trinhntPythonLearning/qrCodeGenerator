import qrcode as qr


def genQRCode(qrContent: str) -> qr.QRCode:
    qrItem = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qrItem.add_data(qrContent)
    qrItem.make(fit=True)

    return qrItem


def saveQRCode(qrItem: qr.QRCode, des: str) -> None:
    qrImage = qrItem.make_image(fill_color='black', back_color='white')
    qrImage.save(des)
