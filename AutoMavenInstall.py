#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 20191012

@author: shun
'''
import os
import constance
import subprocess

def installMaven(folder, type):
    files = os.listdir(folder)
    for file in files:
        print (file)
        if str(file).startswith("."):
            continue
        path = os.path.join(folder, file)
        if constance.AAR_INFO.__contains__(file):
            values = constance.AAR_INFO[file]
            version = values["version"]
            artifactId = values["artifactId"]
            print (path, version, artifactId)
            excuteCmd(artifactId, version, path, type)
            

def excuteCmd(artifactId, version, path, type):
    cmd = ""
    if type == "wesdk":
        cmd = constance.MAVEN_CMD % (constance.GROUP_ID_WESDK, artifactId, version, path)
    elif type == "taurusx":
        cmd = constance.MAVEN_CMD % (constance.GROUP_ID_TAURUSX, artifactId, version, path)
    elif type == "adlime":
        cmd = constance.MAVEN_CMD % (constance.GROUP_ID_ADLIME, artifactId, version, path)
    elif type == "fission":
        cmd = constance.MAVEN_CMD % (constance.GROUP_ID_FISSION, artifactId, version, path)
    elif type == "wegame":
        cmd = constance.MAVEN_CMD % (constance.GROUP_ID_WE_GAME, artifactId, version, path)


    # cmd = constance.MAVEN_CMD % (constance.GROUP_ID, artifactId, version, path)
    result = subprocess.call(cmd, shell=True)
    if result == 0 :
        print ("install " + artifactId + " success")
    else:
        print ("install " + artifactId + " failed")

    pass
if __name__ == '__main__':
    aarFolder = os.sys.argv[1]
    buildType = os.sys.argv[2]
    print (constance.AAR_INFO)
    print (len(constance.AAR_INFO))
    installMaven(aarFolder, buildType)
    pass