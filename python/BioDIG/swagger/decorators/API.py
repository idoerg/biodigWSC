#!usr/bin/python

@Method('GET')
@PathParam('id','Integer')
@QueryParam('fields','String')
@Summary('Get the tag based on id')
@Type('Tag') #generated from models.py
def get Tag(request, id):
        return #something

@Method('DELETE')
@PathParam('id','Integer')
@QueryParam('fields','String')
@Summary('Delete the tag with provided id')
@Type('Tag')
def delete Tag(request,id):
        return #the deleted Tag info

@Method('PUT')
@QueryParam('query','TagQuery')
@Summary('Add new tag with provided query')
@Type('Tag')
def put Tag(request,query):
        return #success or not


@Method('POST')
@PathParam('id','Integer')
@QueryParam('query','TagQuery')
@Summary('Modified the tag with provided query')
@Type('Tag')
def post Tag(request,id,query):
        return #success or not

@Method('GET')
@PathParam('id','Integer')
@QueryParam('fields','String')
@Summary('Get the TagGroup based on id')
@Type('TagGroup') #generated from models.py
def get TagGroup(request, id):
        return #something