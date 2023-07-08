# OpenAI API Reference 

This repository contains OpenAI API reference examples. 
* [OpenAI API Reference](https://platform.openai.com/docs/api-reference)


To install the official Python bindings, run the following command:
```bash
pip install openai
```
To install the official Node.js library, run the following command in your Node.js project directory:
```bash
npm install openai
```

# API Keys and Auth

To use the OpenAI API, you need an API key. You can get one for free by signing up for an OpenAI account.
```bash
https://platform.openai.com/account/api-keys
```
* Update the API key in the _open_api_key.py file.

# Models

List and describe the various models available in the API.

```bash
python3 openai_model_list.py
```

# Create chat completion

Given a list of messages comprising a conversation, the model will return a response.

```bash
python3 openai_chat_completion_create.py
```

# Create Image

Given a prompt and/or an input image, the model will generate a new image.

```bash
python3 openai_image_create.py
```

# Create Image Edit

Creates an edited or extended image given an original image and a prompt.

```bash
python3 openai_image_create_edit.py
```

# Create Image Variation

Creates a variation of a given image.

```bash
python3 openai_image_create_variation.py
```

# Create Audio

Turn audio into text

```bash
python3 openai_audio_transcribe.py
```