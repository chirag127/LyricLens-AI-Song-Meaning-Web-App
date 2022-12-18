import requests
def get_orchard_response(prompt="hi, how are you?"):
    """Generate a response to the user's prompt."""

    headers = {
        'authority': 'api.orchard.ink',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjcxOTQ3MzkxLCJzdWIiOiIwZWRhYTg2MS1hNzNkLTRhZTMtOGRjYS04ZTk2MjA2NmE0MDgiLCJlbWFpbCI6Inl0dHViZTM1QGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUVkRlRwN0dKTHRBaGZRc2puTndUNjhaektGRkVFN2Vzel8za3FfendHbGM9czk2LWMiLCJlbWFpbCI6Inl0dHViZTM1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJBYmhpbmF2IEdveWFsIiwiaXNzIjoiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vdXNlcmluZm8vdjIvbWUiLCJuYW1lIjoiQWJoaW5hdiBHb3lhbCIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BRWRGVHA3R0pMdEFoZlFzam5Od1Q2OFp6S0ZGRUU3ZXN6XzNrcV96d0dsYz1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTAzNTAwMTQ2NjI3MDg2NzA0MDE4Iiwic3ViIjoiMTAzNTAwMTQ2NjI3MDg2NzA0MDE4In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE2NzEzNDI1OTF9XSwic2Vzc2lvbl9pZCI6IjgzMDUxMWI3LThjYjItNGQ5Ny1hODJkLWNlOGQwZmI4NzA0ZiJ9.AUXDF4_XuXLmNmdZsiDcDVsDHm9k3kHWFjHBxNI00hc',
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
            'createdAt': '2022-12-18T05:49:59.327Z',
            'messages': {
                'root': {
                    'id': 'root',
                    'index': 0,
                    'createdAt': '2022-12-18T05:49:59.328Z',
                    'type': 'response',
                    'messageText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'innerText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'childrenIds': [
                        '10da039a-9db5-4ea8-a5bf-38b9fee940ef',
                    ],
                    'rejected': False,
                },
                '10da039a-9db5-4ea8-a5bf-38b9fee940ef': {
                    'id': '10da039a-9db5-4ea8-a5bf-38b9fee940ef',
                    'index': 1,
                    'createdAt': '2022-12-18T05:50:10.712Z',
                    'type': 'instruction',
                    'messageText': prompt,
                    'innerText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'childrenIds': [
                        '97e3c14c-0a54-4783-9265-84d6110edcf9',
                    ],
                    'rejected': False,
                    'templateId': '2c77110a-5644-4a1e-bfe4-f0ed2aebc94a',
                    'iconKey': 'Custom',
                    'parentId': 'root',
                },
                '97e3c14c-0a54-4783-9265-84d6110edcf9': {
                    'id': '97e3c14c-0a54-4783-9265-84d6110edcf9',
                    'index': 1,
                    'createdAt': '2022-12-18T05:50:10.718Z',
                    'type': 'response',
                    'messageText': 'Loading Response #1...',
                    'innerText': '',
                    'childrenIds': [],
                    'rejected': False,
                    'parentId': '10da039a-9db5-4ea8-a5bf-38b9fee940ef',
                },
            },
            'numResponses': 2,
            'numInstructions': 1,
        },
        'template_id': '2c77110a-5644-4a1e-bfe4-f0ed2aebc94a',
        'template_name': 'Custom',
        'document_id': 'df83e486-7e09-4aaa-8226-46d9415e86f6',
        'is_retry': False,
    }

    response = requests.post('https://api.orchard.ink/generate_responses', headers=headers, json=json_data)

    response_json = response.json()
    # print(response_json)

    return response_json['responses'][0]['innerText']


if __name__ == "__main__":
    print(get_orchard_response("what is your name?"))