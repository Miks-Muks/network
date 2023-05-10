from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View
from django.utils import timezone



from .models import TopicKaif, CommentTopic
from users.models import Profile
from .forms import CommentForm, TopicForm


# Create your views here.


class IndexView(TemplateView):
    template_name = 'network/index.html'


class TopicsView(ListView):
    queryset = TopicKaif.objects.all()
    template_name = 'network/topics.html'
    context_object_name = 'topics'


class TopicDetail(DetailView):
    model = TopicKaif
    template_name = 'network/detail.html'
    context_object_name = 'topic'

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["topics"] = TopicKaif.objects.all()
        context["commets"] = CommentTopic.objects.filter(topic=self.kwargs['pk'])
        context['form'] = CommentForm

        return context


class TopicCreate(View):
    def get(self, request):
        form = TopicForm
        return render(request, 'network/topic_create.html', {'form': form})

    def post(self, request):
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('network:topics')
        else:
            return render(request,'network/topic_create.html', {'form': form})


class CommentCreate(View):
    def post(self, request, pk_topic):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment = form.cleaned_data['comment']
            user = request.user
            comment.user_set = user
            comment.date = timezone.now()
            comment.topic = TopicKaif.objects.get(pk=pk_topic)
            comment.save()
            return redirect('network:topics', )
