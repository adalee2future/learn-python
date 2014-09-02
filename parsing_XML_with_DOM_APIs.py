# import
from xml.dom.minidom import parse
import xml.dom.minidom

# open XML document using minidom parser
DOMTree = parse('movies.xml')
collection = DOMTree.documentElement
if collection.hasAttribute('shelf'):
    print 'Root element:', collection.getAttribute('shelf')
    
# Get all the movies in the collection
movies = collection.getElementsByTagName('movie')

# print detail of each movie.
for movie in movies:
    print '*******Movie*********'
    if movie.hasAttribute('title'):
        print 'Title:', movie.getAttribute('title')
    
    type = movie.getElementsByTagName('type')[0]
    print 'Type:', type.childNodes[0].data
    format = movie.getElementsByTagName('format')[0]
    print 'Type:', format.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    print 'Type:', rating.childNodes[0].data 
    description = movie.getElementsByTagName('description')[0]
    print 'Type:', description.childNodes[0].data  



