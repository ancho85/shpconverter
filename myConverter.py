#! /usr/bin/env python
import os
import os.path
import sys
for root,d,files in os.walk("."):
    okDir = "./_ok" #linux
    outDir = "./out" #linux
    if sys.platform.startswith("win"):
        okDir = ".\_ok"
        outDir = ".\out"
    if root.startswith(okDir): continue
    if root.startswith(outDir): continue
    for fn in files:
        if fn[-4:] == ".shp":
            if not os.path.exists("./out/%s" % root):
                os.makedirs("./out/%s" % root)
            print fn
            print "nameindex","codeindex","codesQty"
            try:
                for nameindexer in range(0,10):
                    for codeindexer in range(0,10):
                        #print "current nameindexer %s codeindexer %s" % (nameindexer, codeindexer)
                        execute = "python converter.py "
                        execute += "--projection merc --country_name_index %s --country_code_index %s --name %s --width 310 " % (nameindexer, codeindexer, fn[0:-4])
                        execute += "%s/%s ./out/%s/%s_name%scode%s.js" % (root,fn, root, fn[0:-4], nameindexer, codeindexer)
                        os.system(execute)
            except KeyboardInterrupt:
                print "Se ha detenido los indexers"
            best = ""
            biggest = 0
            qtysf = file("%s.qty" % (fn[0:-4]),"r")
            for linea in qtysf.readlines():
                if int(linea.split("-")[1]) > biggest: 
                    biggest = int(linea.split("-")[1])
                    best = linea.split("-")[0]
            print "el mejor %s" % best
            #params = raw_input("conservar archivos [nameindexcodeindex,] (default best=%s)" % best)
            #if not params: 
            currentOutDirName = root
            if not os.path.exists("./out/%s/best" % currentOutDirName):
                os.makedirs("./out/%s/best" % currentOutDirName)
                print "creando directorio ./out/%s/best" % currentOutDirName
            params = best
            archivos = params.split(",")
            for ar in archivos:
                nam, idx = ar[0], ar[1]
                for root2,d2,files2 in os.walk("./out"):
                    if root2.find("_fixed") > -1: continue
                    for fn2 in files2:
                        if fn2 == "%s_name%scode%s.js" % (fn[0:-4], nam, idx): 
                            #print os.path.getsize(root2+"/"+fn2)
                            try:
                                os.rename("./out/"+currentOutDirName+"/"+fn2, "./out/"+currentOutDirName+"/best/"+ fn2)
                                print "moviendo mejor archivo a best"
                            except:
                                pass
                            break
            print "borrando invalidos .js"
            for root3,d3,files3 in os.walk("./out"):
                if root3.find("_fixed")>-1: continue
                if root3.find("best") > -1: continue
                for fn3 in files3:
                    try:
                        os.remove(root3+"/"+fn3)
                    except:
                        pass
            print "borrando .qty"
            for root4,d4,files4 in os.walk("."):
                for qtyFiles in files4:
                    if qtyFiles[-4:] == ".qty":
                        os.remove("./%s" % qtyFiles)
