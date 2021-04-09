import requests
import json
import random

#from django.views import generic

class YourCharacter():
    #Can't export a global variable
    global recipe
    recipe = random.randrange(1, 150)
    print("Recipe:", recipe)


    def executeQuery(recipe):
        query = """
            query ($recipe:ID!) {
                character(id:$recipe){
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
        variables = {'recipe': recipe}
        r = requests.post(url, json = {'query': query, 'variables': variables})

        body = r.json()
        #print("\nBody:", body)
        return body

    def get_character_info():
        query = YourCharacter.executeQuery(recipe)
        print("\nQuery:", query)
        #global gci_list
        gci_list = []
        for key in query['data']['character']:
            if (key != 'episode'):
                gci = query['data']['character'][key]
                #print(key + ':', query['data']['data']['character'][key])
                print(gci)
                gci_list.append(gci)
        print("\nGCI List:", gci_list)

        return gci_list

    def get_character_episodes():
        query = YourCharacter.executeQuery(recipe)
        #global gce_list
        gce_list = []
        for i in query['data']['character']['episode']:
            gce = i['episode'] + ': ' + i['name']
            #print(gce)
            gce_list.append(gce)
        print("\nGCE List:", gce_list)

        return gce_list

#YourCharacter.executeQuery(recipe)
#print("\nGCI List:", gci_list)
