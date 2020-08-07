# AnkiFCsPython
Use this simple python script to automate Flashcard creation in Anki.

![screenshot](./word.jpg?raw=true "Screenshot")

You will first need to create a folder that contains another folder. In the screenshot above, the top right is the parent (for the pictures) and the bottom right is the containing folder (with the temporary audio files). **It's very important to name the picture file the same as the desired flashcard name!** Do this when you're saving it.
</br>
</br>
*Note - The folder within will contain a temporary audio file (this is created by the script and is **optional**, there's nothing to change in the script) for the flashcard. I use this script for language learning and get my audio from forvo. The audio can simply be downloaded to your normal download folder, **but you MUST name the audio file the same as the picture file.*** Do this when you're downloading it.
</br>
</br>
Within the script you need to enter a couple of things, namely the coordinates for the mouse clicks and the filepaths. These coordinates can be seen in the screenshot above.
</br>
</br>
The coordinates can be found by **importing pyautogui and running pyautogui.position()** when your cursor is at the desired position. The positions are described in the script.
</br>
</br>
They are:
1. The top of the flashcard creation box (to ensure its selection)
2. The location of the first picture (you only need this position as the pictures get **deleted** as the flashcards are created)
3. Some point on the far right of the first and second tabs of the flascard window
4. The location of the audio file (this will be created within the bottom right folder above and get **deleted** after use)
5. For those like me, you can finish everything off by adding the coordinates to close all three windows on completion of the task.
</br>
</br>
The script creates 2 flashcards per word. One with word/audio => picture and the reverse. If there is no audio file, the script runs normally.
