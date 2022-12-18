import requests
def get_orchard_response(prompt="hi, how are you?"):
    """Generate a response to the user's prompt."""

    response = line_5(prompt)

    response_json = response.json()
    # print(response_json)

    return response_json['responses'][0]['innerText']

def line_5(prompt):  # sourcery skip: inline-immediately-returned-variable

    headers = {
        'authority': 'api.orchard.ink',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjcxOTQ5MDkyLCJzdWIiOiI0NzUzMDZjNS1jOWEyLTRjNmMtYmE5MS05NGFiODIyYjdkMjgiLCJlbWFpbCI6InN0b3JhZ2VjNTZAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnb29nbGUiLCJwcm92aWRlcnMiOlsiZ29vZ2xlIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BRWRGVHA3QkJWVDRZTlRIYXh2WVhhaWdRdktUa2NCdHFoeWZReEdwRUpENz1zOTYtYyIsImVtYWlsIjoic3RvcmFnZWM1NkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiQ2xvdWQgU3RvcmFnZSIsImlzcyI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3VzZXJpbmZvL3YyL21lIiwibmFtZSI6IkNsb3VkIFN0b3JhZ2UiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUVkRlRwN0JCVlQ0WU5USGF4dllYYWlnUXZLVGtjQnRxaHlmUXhHcEVKRDc9czk2LWMiLCJwcm92aWRlcl9pZCI6IjEwNjcyMTk2Njg1OTI2MzY3MzQ4OSIsInN1YiI6IjEwNjcyMTk2Njg1OTI2MzY3MzQ4OSJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNjcxMzQ0MjkyfV0sInNlc3Npb25faWQiOiI0MjlhZTRhMi1kODllLTQwZWYtOTE4OC1lOGVlYWQ2NTU5OWQifQ.O9lAODgRpBgmXd1sYWCR1xQdnpQ9CZjmD2VO7uePVK0',
        'content-type': 'application/json',
        'origin': 'https://www.orchard.ink',
        'referer': 'https://www.orchard.ink/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    }

    json_data = {
        'thread': {
            'id': 'default',
            'createdAt': '2022-12-15T07:18:26.968Z',
            'messages': {
                'root': {
                    'id': 'root',
                    'index': 0,
                    'createdAt': '2022-12-15T07:18:26.968Z',
                    'type': 'response',
                    'messageText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'innerText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'childrenIds': [
                        'a73979b6-9176-4586-9574-77269167e1a3',
                    ],
                    'rejected': False,
                },
                'a73979b6-9176-4586-9574-77269167e1a3': {
                    'id': 'a73979b6-9176-4586-9574-77269167e1a3',
                    'index': 1,
                    'createdAt': '2022-12-18T06:19:38.179Z',
                    'type': 'instruction',
                    'messageText': prompt,
                    'innerText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'childrenIds': [
                        '0a1fae92-8fa0-4f90-8209-bbbee6fb26f2',
                    ],
                    'rejected': False,
                    'templateId': '2c77110a-5644-4a1e-bfe4-f0ed2aebc94a',
                    'iconKey': 'Custom',
                    'parentId': 'root',
                },
                '0a1fae92-8fa0-4f90-8209-bbbee6fb26f2': {
                    'id': '0a1fae92-8fa0-4f90-8209-bbbee6fb26f2',
                    'index': 1,
                    'createdAt': '2022-12-18T06:19:38.183Z',
                    'type': 'response',
                    'messageText': 'Loading Response #1...',
                    'innerText': '',
                    'childrenIds': [],
                    'rejected': False,
                    'parentId': 'a73979b6-9176-4586-9574-77269167e1a3',
                },
            },
            'numResponses': 2,
            'numInstructions': 1,
        },
        'template_id': '2c77110a-5644-4a1e-bfe4-f0ed2aebc94a',
        'template_name': 'Custom',
        'document_id': 'f8589a2e-c594-498d-8e1a-9ee8fdca3320',
        'is_retry': False,
    }

    response = requests.post('https://api.orchard.ink/generate_responses', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"thread":{"id":"default","createdAt":"2022-12-15T07:18:26.968Z","messages":{"root":{"id":"root","index":0,"createdAt":"2022-12-15T07:18:26.968Z","type":"response","messageText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["a73979b6-9176-4586-9574-77269167e1a3"],"rejected":false},"a73979b6-9176-4586-9574-77269167e1a3":{"id":"a73979b6-9176-4586-9574-77269167e1a3","index":1,"createdAt":"2022-12-18T06:19:38.179Z","type":"instruction","messageText":"j","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["0a1fae92-8fa0-4f90-8209-bbbee6fb26f2"],"rejected":false,"templateId":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","iconKey":"Custom","parentId":"root"},"0a1fae92-8fa0-4f90-8209-bbbee6fb26f2":{"id":"0a1fae92-8fa0-4f90-8209-bbbee6fb26f2","index":1,"createdAt":"2022-12-18T06:19:38.183Z","type":"response","messageText":"Loading Response #1...","innerText":"","childrenIds":[],"rejected":false,"parentId":"a73979b6-9176-4586-9574-77269167e1a3"}},"numResponses":2,"numInstructions":1},"template_id":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","template_name":"Custom","document_id":"f8589a2e-c594-498d-8e1a-9ee8fdca3320","is_retry":false}'
#response = requests.post('https://api.orchard.ink/generate_responses', headers=headers, data=data)    return response

    print(response.text)

    return response


if __name__ == "__main__":
    print(get_orchard_response("what is your name?"))