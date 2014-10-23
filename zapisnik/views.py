# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from zapisnik.models import LogEntry, LogComment
from django.contrib.auth.decorators import login_required


def logentry_list(request):
    entries = LogEntry.objects.filter(visible=True)
    return render(request, 'zapisnik/list.html', {
        'entries': entries,
        })


@login_required
def add_comment(request, entry_id):
    entry = get_object_or_404(LogEntry, id=entry_id)
    comment = LogComment (
        author=request.user,
        comment_text=request.POST['comment'],
        log_entry=entry)
    entry.logcomment_set.add(comment)
    entry.save()
    return redirect('zapisnik:logentry_list')


def del_comment(request, entry_id, comment_id):
    entry = get_object_or_404(LogEntry, id=entry_id)
    commment = get_object_or_404(entry.logcomment_set.filter(id=comment_id))
    commment.delete()
    return redirect('zapisnik:logentry_list')