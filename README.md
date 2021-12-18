# spotify-to-mp3-converter

![image](https://user-images.githubusercontent.com/72354934/146514933-d6280a07-3990-4b45-a589-8e40b5db0d44.png)

You can basically understand the process with just this image but for clarity, these are the steps.

For using the `downloader.exe`, follow these steps:

As soon as you run it you will be asked some questions. Let me guide you through it!

![image](https://user-images.githubusercontent.com/72354934/146515253-296f4059-295a-4bf4-9674-b2336143e228.png)

You need to input the directory where you want your music downloaded in, for example `C:\Users\%USERPROFILE%\Videos\Music`. 

If you dont know how to get your directory, here is how:

1. Open up your file explorer

2. Go to the location where you would like to save the songs.

  ![image](https://user-images.githubusercontent.com/72354934/146515575-20d3082c-e0d5-46c8-8e44-f871f1ead52c.png)
    
3.  click next to music
    
4. Your directory should be highlighted as follows

5. ![image](https://user-images.githubusercontent.com/72354934/146515675-db0d566d-7c10-4317-b7fc-c8b801f3d7f3.png)

6. Simply press `Ctrl + c` and you have your directory copied!!

now you will have to answer this question:
![image](https://user-images.githubusercontent.com/72354934/146515764-88c3fef1-9c29-446f-a7cf-8edfa805c6d3.png)

If you want to download a song, type `song` and press enter. If its a playlist, type `playlist` and press enter.

After that, input the link of the song/playlist 
![image](https://user-images.githubusercontent.com/72354934/146515914-ba5fb91b-5bb3-42c7-8359-0811a880af8f.png)

Voila! your music will be download.

For using source code:

Head over to the `Source` folder and download the code.

install the requirements by `pip install -r requirements.txt`

also download ffmpeg with reference to https://www.youtube.com/watch?v=r1AtmY-RMyQ

Before you run the `downloader.py` create a spotify developer application, to get your `Client Id` and `Client Secret` and copy and paste them in the respective variables in line 54

![image](https://user-images.githubusercontent.com/96326246/146630564-a7934180-cf69-406e-92d7-f093d0d3e507.png)

now run the `downloader.py` with `python downloader.py` in the command prompt and follow the steps mentioned above
