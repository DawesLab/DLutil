"""
Save Qfig data as .png of qfunc and .npy of array of complex max values of fft's
Creates a folder with today's date: 01-13-2014
If folder for today doesn't exist, create it; else navigate to appropriate folder
"""
import datetime
import os

ROOT_PATH = "/home/photon/Dropbox/Data/"
TARGET_FOLDER = datetime.datetime.now().strftime("%m-%d-%Y")
if not os.path.exists(ROOT_PATH + TARGET_FOLDER):
    os.makedirs(ROOT_PATH + TARGET_FOLDER)
os.chdir(ROOT_PATH + TARGET_FOLDER)

filename = datetime.datetime.now().strftime("%H-%M-%S")# based on time and date

fullfilename = ROOT_PATH + TARGET_FOLDER + filename
