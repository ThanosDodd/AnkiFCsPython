import pyautogui, os, send2trash, shutil

## The path to your pictures folder which ALSO contains your temporary audio folder
folderWithPics = r'C:\...'
## The path to the folder containing the downloaded audio
folferWithAudio = r'C:\...'
## The path to the folder that will contain the temporary audio
folferWithTempAudio = r'C:\...\TEMP.mp3'

## Use >>> pyautogui.position() to determine the coordinates below
## xSelect - The x location of some grey area on Anki FC creator to make sure it's selected
## ySelect - The y location of some grey area on Anki FC creator to make sure it's selected
xSelect = ...
ySelect = ...
## xWritePicName - The x location of the top Anki tab
## yWritePicName - The y location of the top Anki tab
xWritePicName = ...
yWritePicName = ...
## xCopyPic - The x location of the first picture
## yCopyPic - The y location of the first picture
xCopyPic = ...
yCopyPic = ...
## xPastePic - The x location of the bottom Anki tab
## yPastePic - The y location of the bottom Anki tab
xPastePic = ...
yPastePic = ...
## xCopyAudio - The x location of the TEMP audio file
## yCopyAudio - The y location of the TEMP audio file
xCopyAudio = ...
yCopyAudio = ...
## xPasteAudio - The x location of the paste audio file location
## yPasteAudio - The y location of the paste audio file location
xPasteAudio = ...
yPasteAudio = ...
## xAddFlashcard
## yAddFlashcard
xAddFlashcard = ...
yAddFlashcard = ...  

## OPTIONAL COORDINATES TO CLOSE EVERYTHING OFF

## xXfirstWindow
## yXfirstWindow
xXfirstWindow = ...
yXfirstWindow = ...
## xXSecondWindow
## yXSecondWindow
xXSecondWindow = ...
yXSecondWindow = ...
## xXThirdWindow
## yXThirdWindow
xXThirdWindow = ...
yXThirdWindow = ... 


## Only deal with the .jpg files within
for filename in os.listdir(folderWithPics):
    if filename.endswith('.jpg'):
        ## the first part of the 'split' is the word name. NB!! When you save the picture you must name the picture accordingly
        pic_name = filename.split('.')
        pyautogui.click(xSelect, ySelect, duration=1)
        pyautogui.click(xWritePicName, yWritePicName, duration=1); pyautogui.typewrite(pic_name[0])

        ## copy and paste the image to the flashcard
        pyautogui.click(xCopyPic,yCopyPic, duration=1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(xPastePic,yPastePic, duration=1)
        pyautogui.hotkey('ctrl', 'v')
        

        ## Create a temporary audio file if an Audio file with the same name as the word exists in the Downloads folder
        ## NB!! You must name the audio files the same as you name the picture words
        for item in os.listdir(folferWithAudio):
            if pic_name[0] in item:
                pathToItem = os.path.join(folferWithAudio, item)
                shutil.move(pathToItem, folferWithTempAudio)
        ## And if it does add it to the flashcard
        if os.path.exists(folferWithTempAudio):
            pyautogui.click(xCopyAudio,yCopyAudio, duration=3)
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.click(xPasteAudio,yPasteAudio, duration=1)
            pyautogui.hotkey('ctrl', 'v')


        ## 'Add the flashcard'
        pyautogui.click(xAddFlashcard,yAddFlashcard, duration=1)
      
        ## CREATE THE REVERSE FLASHCARD

        ## Copy the image to the front
        pyautogui.click(xCopyPic,yCopyPic, duration=2)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(xWritePicName,yWritePicName, duration=1)
        pyautogui.hotkey('ctrl', 'v')
        ## type the name in the back
        pyautogui.click(xPastePic, yPastePic, duration=1)
        pyautogui.press('tab')
        pyautogui.typewrite(pic_name[0])
        ## add the audio if it exists
        if os.path.exists(folferWithTempAudio):
            pyautogui.click(xCopyAudio,yCopyAudio, duration=2)
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.click(xPasteAudio, yPasteAudio, duration=1)
            pyautogui.press('tab')
            pyautogui.hotkey('ctrl', 'v')
        ## delete the picture
        picPartFinal = os.path.join(folderWithPics, filename)
        send2trash.send2trash(picPartFinal)
        ## delete the audio file
        send2trash.send2trash(folferWithTempAudio)
        ## add the second flashcard
        pyautogui.click(601,1002, duration=2)

 
pyautogui.click(xXfirstWindow, yXfirstWindow, duration=2)
pyautogui.click(xXSecondWindow, yXSecondWindow, duration=3)
pyautogui.click(xXThirdWindow, yXThirdWindow, duration=4)
