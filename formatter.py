#! /usr/bin/env python
import os
import os.path
import sys
import re
dirSep = "/"
outDir = "./out" #linux
if sys.platform.startswith("win"):
    outDir = ".\out"
    dirSep = "\\"
for root,d,files in os.walk(outDir):
    if root.startswith(outDir + dirSep + "_fixed"): continue
    for fn in files:
        if fn[-3:] == ".js":
            with open(root+"/"+fn) as originFile:
                with open(root+"/"+fn[0:-3]+".fix", "w") as outFile: 
                    for line in originFile.readlines():
                        newLine = re.sub(r',{"width"', ',{\n    "width"', line)
                        newLine = re.sub(r', "pathes":', ',\n    "pathes":', newLine)
                        newLine = re.sub(r'": {"', '":\n        {"', newLine)
                        newLine = re.sub(r'"}, "', '"},\n         "', newLine)
                        newLine = re.sub(r'{"path":', '    {"path":', newLine)
                        newLine = re.sub(r', "name":', ',\n             "name":', newLine)
                        newLine = re.sub(r'}, "projection":', '},\n    "projection":', newLine)
                        newLine = re.sub(r'}, "height"', '},\n    "height"', newLine)
                        newLine = re.sub(r'}\);', '\n});', newLine)
                        outFile.write(newLine)
