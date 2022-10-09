#libreries
import tkinter,os,cv2
from tkinter import filedialog
from pyzbar.pyzbar import decode


def choiceqr():

   scanme = tkinter.Tk()
   scanme.withdraw() #use to hide tkinter window
   currdir = os.getcwd() #fa un pwd quindi directory corrente
   finalgroup = ["errore","errore di selezione del file"]
   filename =filedialog.askopenfilename(parent=scanme, initialdir=currdir, title='Please select a file', filetypes=(("png files","*.png"),("all files","*.*")))
   if len(filename) > 0:
      group1 = []
      group2 = []
      finalgroup = ["errore","QR code non riconosciuto"]
      image = cv2.imread(filename)
      decodedObjects = decode(image)
      #mi ricavo i data dal qrcode
      for obj in decodedObjects:
         decdata=str(obj.data)
      data, vertices_array, binary_qrcode = cv2.QRCodeDetector().detectAndDecode(image)

      if "WIFI" in decdata:#wifi
         print("wifi")
         group1 = str(data).split(":")
         for s in group1 :
            split1 = s.split(";")
            group2+=split1
         if group2[8] == "false" or "":
            hidden ="è visibile"
         else:
            hidden ="è nascosta"
         finalgroup = ["wifi", f"Crittografia: {group2[2]};\nSSID / Nome wireless: {group2[4]};\nPassword: {group2[6]};\nLa rete {hidden};"]
      elif "mailto" in decdata:
         print("mail")
         group1 = decdata.split(sep="'")
         group1.remove(group1[0])
         group1.remove(group1[-1])
         for s in group1:
            split1 = s.split(":")
            group2 += split1
         group3 = []
         for s in group2:
            split1 = s.split("=")
            group3 += split1
         group4 = []
         for s in group3:
            split1 = s.split("?")
            group4 += split1
         group5 = []
         for s in group4:
            split1 = s.split("&")
            group5 += split1
         finalgroup = ["mail-to",f"A: {group5[1]}\nOggetto: {group5[3]};\nTesto: {group5[5]}"]
      elif "BEGIN:VEVENT" in decdata:# calendar
         group1 = str(data).split(sep=":")
         for s in group1:
            split1 = s.split(";")
            group2 += split1
         # print(f"final group: {group2}")
         group3 = []
         for a in group2:
            split2 = a.split("\n")
            group3 += split2
         start = group3[7]
         end = group3[9]
         finalgroup = ["evento", f"Nome evento: {group3[3]};\nIndirizzo: {group3[5]};\nData di inzio: {start[6:8]}/{start[4:6]}/{start[:4]} all'ora: {start[9:11]}:{start[11:13]}:{start[13:15]};\nData di fine: {end[6:8]}/{end[4:6]}/{end[:4]} all'ora: {end[9:11]}:{end[11:13]}:{end[13:15]};"]
      elif "tel" in decdata:#telefono
         group1 = decdata.split(sep="'")
         group1.remove(group1[0])
         group1.remove(group1[-1])
         for s in group1:
            split1 = s.split(":")
            group2 += split1
         numbt = group2[1]
         finalgroup = ["numero di telefono",f"Prefisso: {numbt[:4]};\nNumero: {numbt[3:]};"]
      elif "https" or "http" or "www." in decdata:#url link
         finalgroup = ["link", data]
   else:
      print("errore di selezione del file")
   return finalgroup

# print(choiceqr())
