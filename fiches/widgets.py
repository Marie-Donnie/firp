from django.forms import widgets


class DynamicSelect(widgets.Select):
    template_name = 'widgets/dynamic-select.html'


class LimitedTextarea(widgets.Textarea):
    template_name = 'widgets/limited-text-area.html'

    class Media:
        js = ('widgets/count_chars.js',)
