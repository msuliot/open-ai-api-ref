import openai

def get_completion(prompt, model="gpt-3.5-turbo",temperature=0): 
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
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
        return response.choices[0].message["content"]




def audio_to_text(audio_file):
    try:
        audio= open(audio_file, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio)
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
        return transcript["text"]


def create_prompt(transcript):
    prompt = f"""
        Your task is to generate a short summary of a conversation between a customer service agent, and a customer.
        You need to also give the sentiment of the customer at the end of the conversation.

        Conversation Summary:
        Sentiment:

        Summarize the conversation below, delimited by triple 
        backticks, in at most 10 words. 

        Conversation: ```{transcript}```
        """
    return prompt   