from django.shortcuts import render
from django.views.generic import TemplateView

from account.forms import commentboxform
from account.models import CommentBox


def HomePage(request):
    if request.method == 'POST':
        form =commentboxform(request.POST,request.FILES)
        if form.is_valid():
            commentform = form.save()
            print(commentform)
            new_form=commentboxform()
        else:
            note="failed.Try again!!"
        return render(request,'index.html',{'form': new_form})
    else:
        form = commentboxform()
        print(form)
        return render(request,'index.html', {'form':form})

# class HomePage(TemplateView):
#     model = CommentBox
#     template_name = 'index.html'

class TestPage(TemplateView):
    template_name='test.html'

class ThankstPage(TemplateView):
    template_name='thanks.html'

class AboutPage(TemplateView):
    template_name = 'about.html'
