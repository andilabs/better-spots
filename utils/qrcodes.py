import qrcode
import qrcode.image.svg


def make_qrcode(data, version=1, box_size=3, border=4):

    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=int(box_size),
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    return img


def make_svg_qrcode(data, box_size=10):
    img = qrcode.make(
        data,
        image_factory=qrcode.image.svg.SvgPathImage,
        box_size=box_size)

    return img
