from pytube import YouTube #don't name the source file as the library you want to import
yt = YouTube('https://youtu.be/9i8YJrFnM1g') #apparently no longer working
print(yt.title)
print(yt.description)
print(yt.length)
