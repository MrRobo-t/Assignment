import requests


class Dictionary:
    def search_meaning(self, word):
        '''
        description: This function makes an api call to fetch the JSON response. The JSOn response is then processed to
        get the meaning of the word. The status code explains whether the search for the word was successful or not
        :param word: input string to be processed
        :return: meaning of the word if found else return "String not found"
        '''

        if len(word) == 0:
            return "Invalid String"

        api = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        response = requests.get(api)

        if response.status_code == 200:
            val = response.json()

            meaning = val[0]["word"] + ". " + val[0]['meanings'][0]['partOfSpeech'] + ". " + \
                      val[0]['meanings'][0]['definitions'][0]['definition']

            return meaning

        return "String not found"


dic = Dictionary()
print("Word?")
input_word = input()

print(dic.search_meaning(input_word))
