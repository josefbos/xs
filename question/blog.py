import os
import openai
import config


openai.api_key = config.OPENAI_API_KEY


def answer(prompt1):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt="reply to this quetions : {} \n1.".format(prompt1),
      temperature=0.8,
      max_tokens=700,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


