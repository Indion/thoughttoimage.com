import openai
import os
from config import key

openai.api_key=key 
response=openai.Image.create(
    prompt = "red sports car",
    n=1,
    size="512x512"
)
image_url=response['data'][0]['url']
print(image_url)