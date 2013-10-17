#!usr/bin.python

@Path('/tags/{id}')
@Description('Operations on a single tag id')
def doProcessRender(request):
        if request.GET: API.getTag(request, request.id)
        elif request.DELETE: API.deleteTag(request, request.id)
        elif request.PUT: API.putTag(request,request.query)
        elif request.POST: API.postTag(request,request.id,request.query)
        else: raise Error