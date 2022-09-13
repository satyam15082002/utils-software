from pytube import YouTube

url=input("Enter youtube video url : ")
file_size=1
def download_progress(arg, chunk = None, remaining = None):
    print("called progresss")
    percent = (100*(file_size-remaining))/file_size
    print(f"{percent}%downloaded")

try:
    yt=YouTube(url,on_progress_callback=download_progress)
    print("Index\tResolution\tMimeType\tFileSize")
    streams=yt.streams.filter(progressive=True)
    
    for i,stream in enumerate(streams):
        size=(stream.filesize)/(1024*1024)
        print(f"{i}\t{stream.resolution}\t\t{stream.mime_type}\t{size}Mb")
    index=int(input("Enter index to download video"))
    if index<len(streams):
        file_size=streams[index].filesize
        streams[index].download()
except Exception as e:
    print(f"Error : {e}")