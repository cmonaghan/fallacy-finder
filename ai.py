import os
import inspect

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # take environment variables from .env.

client = OpenAI(
  # This is the default and can be omitted
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_fallacies(user_input):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "system",
        "content": [
          {
            "text": "You are a professor who can read a passage a text, and pick out logical fallacies by fallacy type. You will return each excerpt of text that uses this fallacy, grouped by fallacy type. Fallacy types you should consider include Ad Hominem, Red Herring, Straw Man, Equivocation, Slippery Slope, Hasty Generalization, Appeal to Authority, False Dilemma, Bandwagon Fallacy, Appeal to Ignorance, Circular Argument, Sunk Cost Fallacy, Appeal to Pity, Causal Fallacy, and Appeal to Hypocrisy, but you may include other types detected outside this list. You should return this in json format according to the following schema, and only include an entry if a fallacy of that type was detected:{\"fallacies\":[{\"type\":\"Ad hominem\",\"text\":\"Katherine is a bad choice for mayor because she didn’t grow up in this town.\",\"explanation\":\"This is an ad hominem because xyz reason\"},{\"type\":\"Red herring\",\"text\":\"Losing a tooth can be scary, but have you heard about the Tooth Fairy?\",\"explanation\":\"This is a red herring because xyz reason\"},{\"type\":\"Straw man\",\"text\":\"Erin thinks we need to stop using all plastics, right now, to save the planet from climate change.\",\"explanation\":\"This is a straw man because xyz reason\"}]}",
            "type": "text"
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "text": "Katherine is a bad choice for mayor because she didn’t grow up in this town. ",
            "type": "text"
          }
        ]
      },
      {
        "role": "assistant",
        "content": [
          {
            "text": "{\"fallacies\":[{\"type\":\"Ad hominem\",\"text\":\"Katherine is a bad choice for mayor because she didn’t grow up in this town.\",\"explanation\":\"An ad hominem fallacy is one that attempts to invalidate an opponent’s position based on a personal trait or fact about the opponent rather than through logic.\"}]}",
            "type": "text"
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "text": "Losing a tooth can be scary, but have you heard about the Tooth Fairy? Now let us change to a different topic altogether. Erin thinks we need to stop using all plastics, right now, to save the planet from climate change.",
            "type": "text"
          }
        ]
      },
      {
        "role": "assistant",
        "content": [
          {
            "text": "{\"fallacies\":[{\"type\":\"Red herring\",\"text\":\"Losing a tooth can be scary, but have you heard about the Tooth Fairy?\",\"explanation\":\"A red herring is an attempt to shift focus from the debate at hand by introducing an irrelevant point.\"},{\"type\":\"Straw man\",\"text\":\"Erin thinks we need to stop using all plastics, right now, to save the planet from climate change.\",\"explanation\":\"A straw man argument is one that argues against a hyperbolic, inaccurate version of the opposition rather than their actual argument.\"}]}",
            "type": "text"
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "text": user_input,
            "type": "text"
          }
        ]
      },
    ],
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
      "type": "json_object"
    }
  )
  return response.choices[0].message.content
