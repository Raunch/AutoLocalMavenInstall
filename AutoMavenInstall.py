#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 20191012

@author: shun
'''
import os
import constance
import subprocess

def installMaven(folder):
    files = os.listdir(folder)
    for file in files:
        print (file)
        if str(file).startswith("."):
            continue
        path = os.path.join(folder, file)
        values = constance.AAR_INFO[file]
        version = values["version"]
        artifactId = values["artifactId"]
        print (path, version, artifactId)
        excuteCmd(artifactId, version, path)


def excuteCmd(artifactId, version, path):
    cmd = constance.MAVEN_CMD % (constance.GROUP_ID, artifactId, version, path)
    result = subprocess.call(cmd, shell=True)
    if result == 0 :
        print ("install " + artifactId + " success")
    else:
        print ("install " + artifactId + " failed")

    pass
if __name__ == '__main__':
    aarFolder = os.sys.argv[1]
    print (constance.AAR_INFO)
    installMaven(aarFolder)
    pass