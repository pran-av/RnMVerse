from django.shortcuts import render
from django.views import generic, View

# Create your views here.
from .models import YourCharacter

class ShowQuery(generic.DetailView):
    model = YourCharacter
    template_name = 'home.html'

    #context = ["Hello","Yo"]

    def executeQuery(self, **kwargs):
        query = """
            query {
              character(id: 125){
                name
                image
                type
                status
                species
                episode{
                  episode
                  name
                }
              }
            }
        """
        url = 'https://rickandmortyapi.com/graphql'

        r = requests.post(url, json = {'query': query})
        context = json.loads(r.text)
        #status = r.status_code
        id_ = self.kwargs.get("id")
        return get_object_or_404(YourCharacter, id =id_)
