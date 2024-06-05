import speedtest
import socket
import subprocess

# Helper function to convert bytes to megabits
def convertBytesToMb(b):
    kb = 1024
    mb = kb * 1024
    return b / mb

# Helper function to scan network for devices
def scanNetwork():
    return "Not implemented yet"

st = speedtest.Speedtest()

print("Press 1 to do a wifi speed test: ")
print("Press 2 to do a scan to see what devices are on the network: ")
start = input()

if start == "1":
    print("Testing download speed...")
    downloadSpeedInBytes = st.download()

    print("Testing upload speed...")
    uploadSpeedInBytes = st.upload()

    print("Testing ping...")
    ping = st.results.ping

    downloadSpeedInMb = convertBytesToMb(downloadSpeedInBytes)
    uploadSpeedInMb = convertBytesToMb(uploadSpeedInBytes)

    # Print results
    print(f"Download Speed: {downloadSpeedInMb:.2f} Mb/s")
    print(f"Upload Speed: {uploadSpeedInMb:.2f} Mb/s")
    print(f"Ping: {ping} ms")

elif start == "2":
    scanNetwork()
