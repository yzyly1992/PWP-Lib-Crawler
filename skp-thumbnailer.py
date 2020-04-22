#! /usr/bin/python
#
# Use this script as thumbnailer with Sketchup in Wine @ Linux:
# 1. Save the script in /usr/bin
#    (for example open the terminal and type: gksudo nautilus /usr/bin)
# 2. Register this thumbnailer in the Gnome configuration using these commands in the terminal:
# gconftool-2 -s /desktop/gnome/thumbnailers/application@x-wine-extension-skp/enable --type=bool true
# gconftool-2 -s /desktop/gnome/thumbnailers/application@x-wine-extension-skp/command --type=string "python /usr/bin/skp-thumbnailer.py %i %o"
#
#
import sys
import struct
import os
counter=0
def pngcopy(infile, outfile):
# copy header
    header = infile.read(8)
#    if header != "\211PNG\r\n\032\n":
#        raise IOError("not a valid PNG file")
    outfile.write(header)
    print(header)
# copy chunks, until IEND
    global counter
    while 1:
        chunk = infile.read(8)
        size, cid = struct.unpack("!l4s", chunk)
        print(counter,chunk)
        outfile.write(chunk)
        outfile.write(infile.read(size))
        outfile.write(infile.read(4)) # checksum
        counter+=1
        if cid == "IEND":
            break


infile = open("./test.skp", "rb")
infile.seek(0x76d)
outfile = open("./test.png", "wb")
pngcopy(infile, outfile)
outfile.close()
# remove the thumbnail if it is empty (ie. because of not working png exporter in Sketchup in Wine)
if counter<=5:
    os.remove(sys.argv[2])
infile.close()
