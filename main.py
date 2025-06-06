from audio import recognize_speech
from clien_params import client

if __name__ == "__main__":
    result = recognize_speech()

    response = client.chat.completions.create(
        model = "gpt-4.1-nano",
        messages=[
            {'role':'user','content':result}
        ]
    )

    print(f"Ответ модели: {response.choices[0].message.content}")