# Importing library
import qrcode

def wifiG(ssid, password, encri, hidden, nameimg):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=7, border=3)
    code = f"WIFI:T:{encri};S:{ssid};P:{password};H:{hidden};"
    print(code)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{nameimg}.png")

def urlG(url, nameimg):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=3)
    code = str(url)
    print(code)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{nameimg}.png")

def calendarG(NameEvent, location, startDateDay, startDatemonth, startDateyear, startTimeHour, startTimeMinute, startTimeSecond, endDateDay, endDatemonth, endDateyear, endTimeHour, endTimeMinute, endTimeSecond, nameimg):
    start = startDateyear+startDatemonth+startDateDay+"T"+startTimeHour+startTimeMinute+startTimeSecond
    end = endDateyear+endDatemonth+endDateDay+"T"+endTimeHour+endTimeMinute+endTimeSecond
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=7, border=3)
    code = f"BEGIN:VEVENT\nSUMMARY:{NameEvent}\nLOCATION:{location}\nDTSTART:{start}\nDTEND:{end}\nEND:VEVENT\n"
    print(code)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{nameimg}.png")

def telG(prefix, number, nameimg):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=3)
    code = f"tel:{prefix} {number}"
    print(code)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{nameimg}.png")

def mailG(to,subj,text,nameimg):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=7, border=3)
    code = f"mailto:{to}?subject={subj}&body={text}"
    print(code)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{nameimg}.png")

