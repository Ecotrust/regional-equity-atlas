from django.shortcuts import render
from django.conf import settings

# Create your views here.
def visualize(request, template=settings.VISUALIZE_PLANNER_TEMPLATE):
    from visualize.views import show_planner
    response_dict = show_planner(request, template, False)

    from data_manager.models import Theme
    headers_list = []
    for theme in Theme.objects.all().order_by('order'):
        # topics_list = settings.HEADER_TOPICS
        # for topic in settings.HEADER_TOPICS:
        #     foci_list = topic['foci']
        #     topics_list.append({'name': topic['name'], 'foci'})
        headers_list.append({'name': theme.display_name, 'id': theme.name, 'topics':settings.HEADER_TOPICS})


    # from rea.models import Header, Topic, Focus, LayerState
    # headers_list = []
    # for header in Header.objects.all().order_by('order'):
    #     topics_list = []
    #     for topic in Topic.objects.filter(header=header).order_by('order'):
    #         foci_list = []
    #         for focus in Focus.objects.filter(topic=topic).order_by('order'):
    #             focus_dict = {
    #                 'name': focus.name,
    #                 'order': focus.order,
    #                 'zoom': focus.zoom,
    #                 'x_coord': focus.x_coord,
    #                 'y_coord': focus.y_coord,
    #                 'state': [x.toDict() for x in LayerState.objects.filter(focus=focus)]
    #             }
    #             foci_list.append(focus_dict)
    #         topic_dict = {
    #             'name': topic.name,
    #             'order': topic.order,
    #             'foci': foci_list
    #         }
    #         topics_list.append(topic_dict)
    #     header_dict = {
    #         'name': header.name,
    #         'order': header.order,
    #         'topics': topics_list
    #     }
    #     headers_list.append(header_dict)
    context = response_dict['context']
    context['headers'] = headers_list
    # import ipdb; ipdb.set_trace()
    return render(request, template, context)
