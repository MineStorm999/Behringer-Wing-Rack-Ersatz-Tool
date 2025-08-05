import wave

import sys

import datetime

import os

import numpy as np

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import subprocess

import math

density = 1
fontSize = int(20 / density)

hasOrdner = False
hasWav = False
wavFile = ""

def ChannelNum(channelCount):
    #return channelCount
    if(channelCount > 16):
        return 32
    elif(channelCount > 8):
        return 16
    else:
        return 8

class WavHeader:
    Riff = "RIFF" #// = "Riff";
    wavsize = np.uint32(0) 			#// size of WAVE sub-chunk
    Wave = "WAVE" 				#// = "WAVE"
    ufmt = "fmt"				#// = "fmt ";
    Sixteen = np.uint32(16)			#// = 16;
    One = np.uint16(1)				#// = 1;
    num_channels = np.uint16(0)		#// number of channels in multichannel data (8, 16 or 32)
    audio_samprate = np.uint32(0)		#// sample rate
    dwAvgBytesPerSec = np.uint32(0)	#// average bytes per second
    wBlockAlign = np.uint16(0)		#// alignment
    BitDepth = np.uint16(32)			#// = 32;
    Junk = "JUNK"				#// = "JUNK";
    Junk_bytes = np.uint32(32716)	

    def __init__(self, nChannels, smpRate, smpWidth, smpCount):
        self.Riff = "RIFF"                                                 #// = "Riff";
        self.wavsize = np.uint32(smpWidth * smpCount * ChannelNum(nChannels) + 44 + 32716)            #// size of WAVE sub-chunk
        self.Wave = "WAVE" 				                                   #// = "WAVE"
        self.ufmt = "fmt"				                                   #// = "fmt ";
        self.Sixteen = np.uint32(16)			                           #// = 16;
        self.One = np.uint16(1)				                               #// = 1;
        self.num_channels = np.uint16(ChannelNum(nChannels))		                   #// number of channels in multichannel data (8, 16 or 32)
        self.audio_samprate = np.uint32(smpRate)		                   #// sample rate
        self.dwAvgBytesPerSec = np.uint32(smpRate * smpWidth * ChannelNum(nChannels))  #// average bytes per second
        self.wBlockAlign = np.uint16(ChannelNum(nChannels) * smpWidth)	               #// alignment
        self.BitDepth = np.uint16(smpWidth * 8)			                   #// = bit depth;
        self.Junk = "JUNK"				                                   #// = "JUNK";
        self.Junk_bytes = np.uint32(32716)	                               #// = 32716

    def Print(self):
        print(self.Riff)
        print(self.wavsize)
        print(self.Wave)
        print(self.ufmt)
        print(self.Sixteen)
        print(self.One)
        print(self.num_channels)
        print(self.audio_samprate)
        print(self.dwAvgBytesPerSec)
        print(self.wBlockAlign)
        print(self.BitDepth)
        print(self.Junk)
        print(self.Junk_bytes)

    def Write(self, stream):
        stream.write(self.Riff.encode("utf-8"))
        stream.write(self.wavsize.tobytes())
        stream.write(self.Wave.encode("utf-8"))
        stream.write(self.ufmt.encode("utf-8"))
        stream.write(int(32).to_bytes(1, "little"))
        stream.write(self.Sixteen.tobytes())
        stream.write(self.One.tobytes())
        stream.write(self.num_channels.tobytes())
        stream.write(self.audio_samprate.tobytes())
        stream.write(self.dwAvgBytesPerSec.tobytes())
        stream.write(self.wBlockAlign.tobytes())
        stream.write(self.BitDepth.tobytes())
        stream.write(self.Junk.encode("utf-8"))
        stream.write(self.Junk_bytes.tobytes())

def GetWavFile():
    global wavFile
    global feedBack
    global feedBack2
    global getWavButton
    wavFile = filedialog.askopenfilename(title=".wav datei auswählen", filetypes=[("Waves", "*wav")])
    print("Ausgewählte Datei:", wavFile)
    hasWav = True
    feedBack.configure(text="", background="grey")
    feedBack2.configure(text="", background="grey")
    getWavButton.configure(bg="lime green", fg="red")

def GetOutFolder():
    global outFolder
    global feedBack
    global feedBack2
    global getOutOrdnerButton
    outFolder = filedialog.askdirectory(title="Output Ordner auswählen")
    print("Ausgewählter Ordner:", outFolder)
    hasOrdner = True
    feedBack.configure(text="", background="grey")
    feedBack2.configure(text="", background="grey")
    getOutOrdnerButton.configure(bg="lime green", fg="red")

def Convertieren():
    global feedBack
    global feedBack2
    global session_name
    global n_channels
    global sample_width
    global framerate
    global n_frames
    dt = datetime.datetime.now()

    year = dt.year - 1980
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second // 2  # DOS speichert Sekunden in 2-Sek-Schritten

    

    timestamp = ((year) << 25) | (month << 21) | (day << 16) | (hour << 11) | (minute << 5) | second

    session_name = np.uint32(timestamp)
    

    outPath = os.path.join(outFolder, ("{:X}".format(session_name)))
    outWav = os.path.join(outPath, "00000001.wav")
    outLog = os.path.join(outPath, "SE_LOG.BIN")

    print(wavFile)
    
    print(outWav)
    os.makedirs(os.path.dirname(outWav), exist_ok=True)


    with wave.open(wavFile, "rb") as wav:
        n_channels = wav.getnchannels()
        sample_width = wav.getsampwidth()  # in Bytes
        framerate = wav.getframerate()
        n_frames = wav.getnframes()
        
        
        print("Anzahl Kanäle:", n_channels)
        print("Sample-Breite (Bytes):", sample_width)
        print("Sample-Rate:", framerate)
        print("Anzahl Samples:", n_frames)  # DAS ist die gesuchte Zahl

        seconds = n_frames / framerate
        
        print("Minuten: ", math.floor(seconds / 60))
        print("Sekunden: ", seconds % 60)

        data = wav.readframes(n_frames)
        
    #shutil.copy2(wavFile, outWav)
    one = 1
    zero = 0
    t32 = 0
    
    with open(outWav, "wb") as outW:
        wHeader = WavHeader(n_channels, framerate, sample_width, n_frames)
        wHeader.Print()
        wHeader.Write(outW)
        for i in range(0, int(460)):
            outW.write(t32.to_bytes(1, "little"))
        
        fillChannels = ChannelNum(n_channels) - n_channels

        print("Empty Channels will be generated: ", fillChannels)
        print(wHeader.wavsize)
        

        
        print(sample_width * n_frames * n_channels)
        outW.write("data".encode("utf-8"))
        outW.write(int(sample_width * n_frames * n_channels).to_bytes(4, "little"))

        for i in range(0, int(wHeader.Junk_bytes - 468)):
            outW.write(t32.to_bytes(1, "little"))
        
        outW.write("data".encode("utf-8"))
        outW.write(len(data).to_bytes(4, "little"))
        if (fillChannels < 1):
            outW.write(data)
        else:
            for frame in range(0, n_frames):
                for b in range(0, sample_width * n_channels):
                    outW.write(data[(int(frame) * sample_width * n_channels) + b].to_bytes(1, "little"))
                for i in range(0, fillChannels):
                    outW.write(int(0).to_bytes(sample_width, "little"))
                print(frame)
                    

    shortName = eingabe.get()[:16]

    with open(outLog, "wb") as f:
        

        audioDataSize = n_frames * (sample_width) * ChannelNum(n_channels)
        takeSize = int((audioDataSize & 0xffff8000) / sample_width)

        f.write(session_name.tobytes())
        f.write(ChannelNum(n_channels).to_bytes(4, "little"))
        f.write(framerate.to_bytes(4, "little"))
        f.write(session_name.tobytes())
        f.write(one.to_bytes(4, "little"))
        f.write(zero.to_bytes(4, "little"))
        f.write(n_frames.to_bytes(4, "little"))

        # more than one take
        f.write(takeSize.to_bytes(4, "little"))
        for i in range(0, (255 * 2)):
            f.write(zero.to_bytes(2, "little"))
          
        for i in range(0, 125 * 2):
            f.write(zero.to_bytes(2, "little"))

        
        
        
        chars = len(shortName)

        print(shortName)
        f.write(shortName.encode("utf-8"))

        while (chars < 16):
            f.write(zero.to_bytes(1, "little"))
            chars += 1

        for i in range(0, 120):
            f.write(zero.to_bytes(4, "little"))
        
        feedBack.configure(text=  "" + shortName, background="purple")
        feedBack2.configure(text=  "Erfolgreich erstellt", background="purple")
    

    ordner_pfad = outPath
    anzeigename = shortName

    if (sys.platform.startswith("win")):
        # Pfad zur Desktop.ini
        desktop_ini_pfad = os.path.join(ordner_pfad, "Desktop.ini")

        with open(desktop_ini_pfad, "w", encoding="utf-8") as f:
            f.write("[.ShellClassInfo]\n")
            f.write(f"LocalizedResourceName={anzeigename}\n")

        subprocess.call(["attrib", "+s", ordner_pfad])

        subprocess.call(["attrib", "+h", desktop_ini_pfad])



# Fenster erstellen
root = tk.Tk()
root.title("WavToXLive")
root.geometry("250x400")

style = ttk.Style(root)
print(style.theme_names())
style.theme_use('clam')


root.configure(background="grey")
root.focus = True
root.tk.call('tk', 'scaling', density)

getWavButton = tk.Button(root, text="Wav auswählen", command=GetWavFile, font=("Arial", fontSize), background="red", fg="lime green")
getWavButton.pack(pady=10)

getOutOrdnerButton = tk.Button(root, text="Ordner Auswählen", command=GetOutFolder, font=("Arial", fontSize), background="red", fg="lime green")
getOutOrdnerButton.pack(pady=10)


# Eingabefeld
titel = tk.Label(root, text ="Name",  font=("Arial", fontSize), background="purple", fg="lime green")
titel.pack(pady=16)

eingabe = tk.Entry(root, font=("Arial", fontSize), background="purple", fg="lime green")
eingabe.pack(pady=16)

convertButton = tk.Button(root, text="Convertieren", command=Convertieren, font=("Arial", fontSize), background="purple", fg="lime green")
convertButton.pack(pady=10)

feedBack = tk.Label(root, text="", font=("Arial", int(fontSize)), background="grey", fg="lime green")
feedBack.pack(pady=1)
feedBack2 = tk.Label(root, text="", font=("Arial", int(fontSize)), background="grey", fg="lime green")
feedBack2.pack(pady=10)


root.mainloop()