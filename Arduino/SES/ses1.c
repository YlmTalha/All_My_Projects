#include <stdio.h>
#include <windows.h>
#include <mmsystem.h>
#include <conio.h>

#define COM_PORT "COM3"  // Arduino’nun bağlı olduğu seri portu güncelle!

void setVolume(int volume) {
    // Ses seviyesi değişimini yapmak için Windows API çağrısı
    waveOutSetVolume(0, MAKELONG(volume, volume));
}

int main() {
    FILE *serialPort;
    int potValue;
    int volumeLevel;

    serialPort = fopen(COM_PORT, "r");  // Seri portu aç

    if (serialPort == NULL) {
        printf("Seri port açılamadı!\n");
        return 1;
    }

    printf("Arduino'dan veri okunuyor...\n");

    while (1) {
        fscanf(serialPort, "%d", &potValue);  // Seri porttan potansiyometre verisini oku
        volumeLevel = (potValue * 65535) / 1023;  // 0-1023 değerini 0-65535’e ölçekle

        setVolume(volumeLevel);  // Windows ses seviyesini güncelle
        printf("Ses Seviyesi: %d%%\n", (volumeLevel * 100) / 65535);

        Sleep(200);  // Gereksiz güncellemeleri önlemek için 200ms bekle
    }

    fclose(serialPort);
    return 0;
}
