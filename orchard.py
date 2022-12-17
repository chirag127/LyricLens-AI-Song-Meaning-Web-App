import requests
def get_orchard_response(prompt="hi, how are you?"):
    """Generate a response to the user's prompt."""

    headers = {
        'authority': 'api.orchard.ink',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjcxODg1MzM4LCJzdWIiOiI5Y2JjNDJhNS1mNDI5LTQyYjgtOWM3ZC1lNzM0NjNhOWM0MDMiLCJlbWFpbCI6IndoeWlzd2hlbkBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6Imdvb2dsZSIsInByb3ZpZGVycyI6WyJnb29nbGUiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FFZEZUcDZwRU45cnJ1Z19hbkY3eWF5TXV2SXBrRU56ajNRbFlBbXp1bzR6PXM5Ni1jIiwiZW1haWwiOiJ3aHlpc3doZW5AZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZ1bGxfbmFtZSI6IlNBTlRPU0ggU0lOR0hBTCIsImlzcyI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3VzZXJpbmZvL3YyL21lIiwibmFtZSI6IlNBTlRPU0ggU0lOR0hBTCIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BRWRGVHA2cEVOOXJydWdfYW5GN3lheU11dklwa0VOemozUWxZQW16dW80ej1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTEwNTQ4MzE1OTM4NDI2MzMyNjcyIiwic3ViIjoiMTEwNTQ4MzE1OTM4NDI2MzMyNjcyIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE2NzEyODA1Mzh9XSwic2Vzc2lvbl9pZCI6Ijg5YmUxYjQ2LWY4ZGEtNDg2MC05ZjQ5LTk5MjlhYmVjMmE3OCJ9.HaR90EUeTcVB2iPWr7huIvhHKznd9TC65a3qICRzXkw',
        'content-type': 'application/json',
        'origin': 'https://www.orchard.ink',
        'referer': 'https://www.orchard.ink/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
    }

    json_data = {
        'thread': {
            'id': 'default',
            'createdAt': '2022-12-17T12:35:49.207Z',
            'messages': {
                'root': {
                    'id': 'root',
                    'index': 0,
                    'createdAt': '2022-12-17T12:35:49.208Z',
                    'type': 'response',
                    'messageText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'innerText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'childrenIds': [
                        '75a4ae9c-6197-46ce-b14d-be16dfeb1fcc',
                    ],
                    'rejected': False,
                },
                '75a4ae9c-6197-46ce-b14d-be16dfeb1fcc': {
                    'id': '75a4ae9c-6197-46ce-b14d-be16dfeb1fcc',
                    'index': 1,
                    'createdAt': '2022-12-17T12:42:55.305Z',
                    'type': 'instruction',
                    'messageText': prompt,
                    'innerText': "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    'childrenIds': [
                        'cde47bff-8a73-4f23-8f51-74255ff785f4',
                    ],
                    'rejected': False,
                    'templateId': '2c77110a-5644-4a1e-bfe4-f0ed2aebc94a',
                    'iconKey': 'Custom',
                    'parentId': 'root',
                },
                'cde47bff-8a73-4f23-8f51-74255ff785f4': {
                    'id': 'cde47bff-8a73-4f23-8f51-74255ff785f4',
                    'index': 1,
                    'createdAt': '2022-12-17T12:42:55.310Z',
                    'type': 'response',
                    'messageText': 'Loading Response #1...',
                    'innerText': '',
                    'childrenIds': [],
                    'rejected': False,
                    'parentId': '75a4ae9c-6197-46ce-b14d-be16dfeb1fcc',
                },
            },
            'numResponses': 2,
            'numInstructions': 1,
        },
        'template_id': '2c77110a-5644-4a1e-bfe4-f0ed2aebc94a',
        'template_name': 'Custom',
        'document_id': '04ca82c8-9354-4d66-8acd-9cbc5788413b',
        'is_retry': False,
    }

    response = requests.post('https://api.orchard.ink/generate_responses', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"thread":{"id":"default","createdAt":"2022-12-17T12:35:49.207Z","messages":{"root":{"id":"root","index":0,"createdAt":"2022-12-17T12:35:49.208Z","type":"response","messageText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["75a4ae9c-6197-46ce-b14d-be16dfeb1fcc"],"rejected":false},"75a4ae9c-6197-46ce-b14d-be16dfeb1fcc":{"id":"75a4ae9c-6197-46ce-b14d-be16dfeb1fcc","index":1,"createdAt":"2022-12-17T12:42:55.305Z","type":"instruction","messageText":"hi","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["cde47bff-8a73-4f23-8f51-74255ff785f4"],"rejected":false,"templateId":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","iconKey":"Custom","parentId":"root"},"cde47bff-8a73-4f23-8f51-74255ff785f4":{"id":"cde47bff-8a73-4f23-8f51-74255ff785f4","index":1,"createdAt":"2022-12-17T12:42:55.310Z","type":"response","messageText":"Loading Response #1...","innerText":"","childrenIds":[],"rejected":false,"parentId":"75a4ae9c-6197-46ce-b14d-be16dfeb1fcc"}},"numResponses":2,"numInstructions":1},"template_id":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","template_name":"Custom","document_id":"04ca82c8-9354-4d66-8acd-9cbc5788413b","is_retry":false}'
    #response = requests.post('https://api.orchard.ink/generate_responses', headers=headers, data=data)

    # Output:{"run_id":"c13d2237-d971-4cda-b8a7-2dd1a2979a92","responses":[{"innerText":"I'm helping people with their writing and providing them with useful information on a wide range of topics. What kind of help do you need?"}]}

    response_json = response.json()

    # Printing the response from the server.
    # print(response_json)

    innerText = response_json['responses'][0]['innerText']


    return innerText


if __name__ == "__main__":
    print(get_orchard_response("what is your name?"))