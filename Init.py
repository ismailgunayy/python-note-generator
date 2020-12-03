from selenium import webdriver
import pandas as pd
import os
from staticFiles.Note import Note


def scrapeNotes():

    url = 'https://pages.mtu.edu/~suits/notefreqs.html'
    driver = webdriver.Chrome()
    driver.get(url)

    noteList = []

    for index in range(17, 110):

        noteName = driver.find_element_by_xpath(
            '/html/body/center/center/table/tbody/tr[{}]/td[1]'.format(index)).text

        noteFrequency = driver.find_element_by_xpath(
            '/html/body/center/center/table/tbody/tr[{}]/td[2]'.format(index)).text

        note = {
            'noteName': noteName,
            'noteFrequency': noteFrequency
        }

        noteList.append(note)

    df = pd.DataFrame(noteList)
    df.to_csv('.\\staticFiles\\Notes.csv', index=False, header=False)


def formatNotes():

    csvFile = open('.\\staticFiles\\Notes.csv', 'r')
    noteList = csvFile.readlines()
    csvFile = open('.\\staticFiles\\Notes.csv', 'w')
    pyFile = open('.\\staticFiles\\ALL_NOTES.py', 'w')

    pyFile.write("from Note import Note\n\n")

    for index in range(len(noteList)):

        lineElements = noteList[index].split(',')
        noteName = lineElements[0]
        noteFrequency = lineElements[1]

        # Note Name Format
        noteName = noteName.split('/')[0].strip()
        if ('#' in noteName):
            noteName = noteName.replace('#', 'S')

        # Note Frequency Format
        noteFrequency = noteFrequency.split('.')[0]

        pyFile.write(noteName + '\t = Note(' + '\'{}\''.format(noteName) + ', ' + noteFrequency + ')' + '\n')

        lineElements = noteName + ',' + noteFrequency + '\n'
        csvFile.write(lineElements)

    csvFile.close()
    pyFile.close()
    os.remove(".\\staticFiles\\Notes.csv")


if __name__ == "__main__":
    scrapeNotes()
    formatNotes()
