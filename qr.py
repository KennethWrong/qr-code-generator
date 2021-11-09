import qrcode
import cv2
from pyzbar import pyzbar
import sys

# Link for website
def create_qr_code(obj):
        print(obj, file=sys.stdout)
        from datetime import datetime
        name = obj['name']
        date_pre = datetime.now()
        date = date_pre.strftime("%d-%b-%Y %H:%M")
        #Creating an instance of qrcode
        obj = {
                'name': name,
                'date': date,
        }

        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        qr.add_data(obj)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'./qr_codes/{name}.png')
        return True


def scan_qr_code(frame):
        qrs = pyzbar.decode(frame)
        for qr in qrs:
                x, y , w, h = qr.rect
        #1
        qr_info = qr.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, qr_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        print(qr_info)
        return frame

def open_cam():
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        #2
        while ret:
                ret, frame = camera.read()
                frame = scan_qr_code(frame)
                cv2.imshow('Barcode/QR code reader', frame)
                if cv2.waitKey(1) & 0xFF == 27:
                        break
        #3
        camera.release()
        cv2.destroyAllWindows()

