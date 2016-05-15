from searchapp.models import Paper, Keyword

def keyword_addition(paper_id, keywords):
    paper = Paper.objects.get(pk=paper_id)
    print "Extracting from..", paper
    #extract top 20
    keywords = keywords[:20]
    print keywords
    count = 0
    for items in keywords:
        kw = Keyword(keyword= items[0], paper= paper)
        kw.save()
        count = count + 1
    print count, " keywords stored"

def get_latest_paper():
    return Paper.objects.latest('id')