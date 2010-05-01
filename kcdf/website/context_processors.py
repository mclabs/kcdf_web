import re
def header_context(request):
    values = {'body_class': "bg-body-home",}
    #if request.path == "/program/shabaa/":
    if re.search("/program/youth",request.path):
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "shabaa_masthead"
    if re.search("/program/ustawi",request.path):
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "bg-body-inner"
    if re.search("/program/arts",request.path):
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "bg-body-home"
    if re.search("/program/the-girl",request.path):
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "girl-child_masthead"
    if re.search("/program/education",request.path):
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "masthead-education"
    if re.search("/program/early",request.path):
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "masthead-ECD"

    return values
