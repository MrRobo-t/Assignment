import subprocess
from wireless import Wireless


class Wifi:
    def find_best_wifi(self):
        best_wifi = "a"

        # using the check_output() for having the network term retrival
        devices_data = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

        # decode it to strings
        devices_data = devices_data.decode('ascii')
        devices_data = devices_data.replace("\r", "")

        network = []

        lines = devices_data.split("\n")
        for line in lines:
            if "SSID" in line:
                network.append(line.split(":")[1])

        connect_wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'interface'])
        connect_wifi = connect_wifi.decode('ascii')
        connect_wifi = connect_wifi.replace("\r", "")

        i=1
        for wifi in network:
            print("[" + str(i) + "] " + wifi)
            i = i + 1
        select_wifi = input()

        wire = Wireless()
        wire.connect(ssid=network[int(select_wifi)-1], password='hitman123')
        print(network[int(select_wifi)-1])

w = Wifi()
w.find_best_wifi()

