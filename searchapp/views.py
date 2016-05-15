from django.shortcuts import render
from .models import Category, Paper, Keyword, PaperUpload, Reference, Author
from django.shortcuts import get_object_or_404
from haystack.query import SearchQuerySet

from django.shortcuts import render_to_response
from django.http import HttpResponse

import logging

logr = logging.getLogger(__name__)

# Create your views here.

## Search View
def search_page(request):
    categories = Category.objects.all()
    context = dict(categories=categories)
    if 'normal_search' in request.GET:
        search_text = request.GET.get('search-text', '')
        context['search_text'] = search_text
        context['query'] = search_text
        ## Full document search
        context['papers'] = SearchQuerySet().filter(title=context['search_text'])      
        print "papersss", context['papers']
        context['paper_id'] = []
        for obj in context['papers']:
            print "here", obj, obj.object.id, obj.object.abstract
            k = obj.object.id
            print k
            obj.object.abstract = obj.object.abstract[:300]
            p_upload_obj = PaperUpload.objects.get(pk = k)
            p_upload_id = getattr(p_upload_obj, 'id')
            context['paper_id'].append(str(p_upload_id))
            print context['paper_id']
        
    elif 'adv_search' in request.GET:
        print request.GET.get('author-q', '')
        print request.GET.get('year-q', '')
        print request.GET.get('search-text', '')
        if (request.GET.get('author-q', '') != ''):

            search_text = request.GET.get('author-q', '')
            context['search_text'] = search_text
            context['papers'] = SearchQuerySet().filter(document=context['search_text'])
            print "1",context['papers']  
            # for obj in context['papers']:
            # print "here", obj, obj.object.id, obj.object.abstract
            # k = obj.object.id
            # print k
            # obj.object.abstract = obj.object.abstract[:300]
            # p_upload_obj = PaperUpload.objects.get(pk = k)
            # p_upload_id = getattr(p_upload_obj, 'id')
            # context['paper_id'].append(str(p_upload_id))
            # print context['paper_id']        
        elif (request.GET.get('year-q', '') != ''):
            search_text = request.GET.get('year-q', '')
            context['search_text'] = search_text                
            context['papers'] = SearchQuerySet().filter(publishedYear=context['search_text'])   
            print "2", context['papers']
        else:
            search_text = request.GET.get('search-text', '')
            context['search_text'] = search_text
            context['papers'] = SearchQuerySet().filter(document=context['search_text'])   
            print "3", context['papers']
        context['search_text'] = search_text
        context['query'] = search_text
        ## Full document search
        # context['papers'] = SearchQuerySet().filter(document=context['search_text'])   
        print "papersss", context['papers']
        context['paper_id'] = []
        for obj in context['papers']:
            print "here", obj, obj.object.id, obj.object.abstract
            k = obj.object.id
            print k
            obj.object.abstract = obj.object.abstract[:300]
            p_upload_obj = PaperUpload.objects.get(pk = k)
            p_upload_id = getattr(p_upload_obj, 'id')
            context['paper_id'].append(str(p_upload_id))
            print context['paper_id']

    print context
    return render_to_response('searchapp/search_page.html', context) 
    
def display_paper(request, object_id):
    
    print object_id
    context = dict(paper_id = object_id)
    MEDIA_BASEPATH = '../../media/papers/'
    print PaperUpload.objects.all()

    paper_upload_obj = PaperUpload.objects.get(pk = object_id)
    
    papers = Paper.objects.get(paper_upload=paper_upload_obj)
    print "paper is", papers
    print "papers are: ", papers 
    title = getattr(papers, 'title')
    print title  
    context['paper_path'] = MEDIA_BASEPATH + object_id + '.pdf'
    
    ## Full document search
    print context['paper_path']
    
    
    context['paper_details'] = papers
    authors = []
    for a in getattr(papers, 'author').all():
        authors.append(a.name)
    context['paper_authors'] = authors
    author_papers = []
    
    ref_papers = getattr(papers, 'references')
    context['reference_papers'] = ref_papers.all()
    
    rec_all = SearchQuerySet().models(Paper).more_like_this(papers)#[]
    print "rec_all", rec_all.all()
    rec_papers = []
    count = 0
    for item in rec_all.all():
        if count == 0:
            count = count + 1
            continue

        if (count < 4):
            rec_papers.append(item)
            count = count + 1
        else:
            break
    #     if isinstance(item, Paper):
    #         print "paper found!!"
    #         rec_papers.append(item)
    #     else :
    #         if isinstance(item, Author):
    #             print "author found!!", getattr(item, 'name')
    #         else:
    #             print "jaane kya"
    #keywords = Keyword.objects.filter(paper = object_id)
    #print keywords
    #for kw in keywords:
    #    rec_papers.extend(SearchQuerySet().filter(title=kw.keyword))
    #    print rec_papers
    print rec_papers

    context['paper_id'] = []
    for obj in rec_papers:
        print "here", obj, obj.object.id, obj.object.abstract
        k = obj.object.id
        print k
        obj.object.abstract = obj.object.abstract[:300]
        p_upload_obj = PaperUpload.objects.get(pk = k)
        p_upload_id = getattr(p_upload_obj, 'id')
        context['paper_id'].append(str(p_upload_id))
        print context['paper_id']

    context['recommended_papers'] = rec_papers 
    
    return render_to_response('searchapp/display_paper.html', context) 
   