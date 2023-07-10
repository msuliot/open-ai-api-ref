import openai
import open_api_key
openai.api_key = open_api_key.get_api_key()
import webbrowser

#####################################################

def open_image(url):
    webbrowser.open(url)

#  ##### Edit a image by adding something to the transparency layer
try:
    editImage = openai.Image.create_edit(
    image=open("images/michael.png", "rb"), # Original image = exact size as the Mask image
    mask=open("images/transparency.png", "rb"), # Modified image with Mask = exact same size as the original image
    prompt="And some mountains along the horizon, and then the sky is a nebula",
    n=1, # The number of images to generate
    size="1024x1024",
)
except openai.error.APIError as e:
    #Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
    pass
except openai.error.APIConnectionError as e:
    #Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")
    pass
except openai.error.RateLimitError as e:
    #Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")
    pass
except openai.error.AuthenticationError as e:
    #Handle authentication error (e.g. invalid credentials)
    print(f"OpenAI API request failed due to invalid credentials: {e}")
    pass
except openai.error.InvalidRequestError as e:
    #Handle invalid request error (e.g. required parameter missing)
    print(f"OpenAI API request failed due to invalid parameters: {e}")
    pass
except openai.error.ServiceUnavailableError as e:
    #Handle service unavailable error
    print(f"OpenAI API request failed due to a temporary server error: {e}")
    pass
else:
    # code to execute if no exception was raised
    for item in editImage["data"]:
      open_image(item["url"])