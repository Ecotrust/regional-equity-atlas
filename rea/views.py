from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def visualize(request, template=settings.VISUALIZE_PLANNER_TEMPLATE):
    from visualize.views import show_planner
    response_dict = show_planner(request, template, False)

    from data_manager.models import Theme
    headers_list = []
    # for theme in Theme.objects.all().order_by('order'):
    #     topics_list = settings.HEADER_TOPICS
    #     for topic in settings.HEADER_TOPICS:
    #         foci_list = topic['foci']
    #         topics_list.append({'name': topic['name'], 'foci'})
    #     headers_list.append({'name': theme.display_name, 'id': theme.name, 'topics':settings.HEADER_TOPICS})


    from rea.models import Topic, Focus
    headers_list = []
    for header in Theme.objects.all().order_by('order'):
        # for header in Header.objects.all().order_by('order'):
        topics_list = []
        # for topic in Topic.objects.filter(header=header).order_by('order'):
        for topic in Topic.objects.order_by('order'):
            foci_list = []
            for focus in Focus.objects.filter(topic=topic).order_by('order'):
                focus_dict = {
                    'pk': focus.pk,
                    'name': focus.name,
                    'order': focus.order,
                    # 'zoom': focus.zoom,
                    # 'x_coord': focus.x_coord,
                    # 'y_coord': focus.y_coord,
                    # 'state': [x.toDict() for x in LayerState.objects.filter(focus=focus)]
                }
                foci_list.append(focus_dict)
            topic_dict = {
                'pk': topic.pk,
                'name': topic.name,
                'order': topic.order,
                'foci': foci_list
            }
            topics_list.append(topic_dict)
        header_dict = {
            'pk': header.pk,
            'name': header.display_name,
            # 'name': header.name,
            'order': header.order,
            'topics': topics_list
        }
        headers_list.append(header_dict)
    context = response_dict['context']
    context['headers'] = headers_list
    context['MAP_TECH'] = settings.MAP_TECH
    return render(request, template, context)

def get_content(request):
    from data_manager.models import Theme
    from rea.models import ThemeContent, Content, Focus
    focus_id = request.GET.get('focus_id', default=False)
    header_id = request.GET.get('header_id')
    theme = Theme.objects.get(pk=header_id)
    if not focus_id in [False, 'false']:      # can't use 'if focus' in case focus is numeric
        focus = Focus.objects.get(pk=focus_id)
        content = Content.objects.get(theme_content__theme__pk=header_id, focus=focus_id)
        title = "<h1>%s<br/>%s</h1>" % (focus.name, theme.display_name)
    else:
        content = Content.objects.get(theme_content__theme__pk=header_id, focus=None)
        title = "<h1>%s</h1>" % (theme.display_name)
    if not content.content == None:
        content_text = str(content.content)
    else:
        content_text = ''
    return HttpResponse("%s%s" % (title, content_text))
