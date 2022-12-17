from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

# Create file
file1 = drive.CreateFile({'title': 'test1.txt'}) #Nama file yang ingin dibuat
file1.SetContentString('Hallo ges') #Isi dari file tersebut
file1.Upload()

#Upload file
file2 = drive.CreateFile()
file2.SetContentFile('test1.txt') #Ganti test.txt menjadi file yang kamu ingin upload
file2.Upload()
print('Created file %s with mimeType %s' % (file2['title'],
file2['mimeType']))

#Download file
file3 = drive.CreateFile({'id': file2['id']})
print('Downloading file %s from Google Drive' % file3['title'])
file3.GetContentFile('test.txt')  # Ganti test.txt menjadi file yang kamu ingin downalod