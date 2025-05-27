import serial
import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# Arduino'nun bağlı olduğu COM portu buraya yaz (Windows için "COMX", Linux/macOS için "/dev/ttyUSB0")
SERIAL_PORT = "COM3"  # Windows'ta Aygıt Yöneticisi'nden bakarak doğru COM portunu gir
BAUD_RATE = 9600

# Seri bağlantıyı başlat
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Arduino'nun bağlantıyı başlatması için bekle

# Ses kontrolü için pycaw ayarları
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

while True:
    try:
        data = ser.readline().decode().strip()  # Arduino'dan veri oku
        if data:
            pot_value = int(data)  # Gelen değeri sayıya çevir
            volume_level = pot_value / 1023  # 0.0 - 1.0 aralığına getir
            volume.SetMasterVolumeLevelScalar(volume_level, None)  # Ses seviyesini ayarla
            print(f"Ses Seviyesi: {volume_level * 100:.2f}%")
    except Exception as e:
        print("Hata:", e)
