import openai
import _open_api_key
openai.api_key = _open_api_key.get_api_key()
import webbrowser

#####################################################

def open_image(url):
    webbrowser.open(url)

#  ##### Create a simple image # required parameters: prompt
createImage = openai.Image.create(
            prompt="my dog driving a sports car",
            n=1, # The number of images to generate
            size="1024x1024",
            user="MichaelAI", # name of the user
            response_format="url" # url is default but can also be 'b64_json'
        )
image_url_3 = createImage['data'][0]['url']
open_image(image_url_3)
