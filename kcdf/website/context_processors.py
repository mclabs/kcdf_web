def header_context(request):
    values = {'body_class': "bg-body-inner",}
    if request.path == "/program/shabaa/":
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "shabaa_masthead"
    if request.path == "/program/ustawi/":
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "bg-body-inner"
    if request.path == "/program/arts-culture/":
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "bg-body-inner"
    if request.path == "/program/girl-child/":
        ## Don't really use an if block, it's just nasty.
        values['body_class'] = "girl-child_masthead"

    return values
