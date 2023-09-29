from pytube import YouTube
yt = YouTube('https://youtu.be/eSCV-_VkE2c')
print(yt.title, yt.length)