from django.shortcuts import render
import youtube_dl

# Create your views here.
def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
        with ydl:
            result = ydl.extract_info(
                'https://youtu.be/G1uv5ofzszw',
                download=False  # We just want to extract the info
            )
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result['requested_formats'][1]['url']

        print(video)
        context = {
            'link': link,
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')