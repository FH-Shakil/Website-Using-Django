from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Comment

def video_list(request):
    query = request.GET.get('q', '')
    if query:
        videos = Video.objects.filter(title__icontains=query)
    else:
        videos = Video.objects.all()
    return render(request, 'video/video_list.html', {'videos': videos, 'query': query})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    comments = video.comments.all()

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(video=video, text=comment_text)
            return redirect('video_detail', video_id=video.id)

    return render(request, 'video/video_detail.html', {'video': video, 'comments': comments})

