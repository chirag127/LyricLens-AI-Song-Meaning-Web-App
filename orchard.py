import requests


def get_orchard_response(prompt="hi, how are you?"):
    """Generate a response to the user's prompt."""

    response = line_5(prompt)

    response_json = response.json()
    # print(response_json)

    return response_json["responses"][0]["innerText"]


def line_5(prompt):  # sourcery skip: inline-immediately-returned-variable

    headers = {
        "authority": "api.orchard.ink",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjcxOTUyMjA1LCJzdWIiOiIwZWRhYTg2MS1hNzNkLTRhZTMtOGRjYS04ZTk2MjA2NmE0MDgiLCJlbWFpbCI6Inl0dHViZTM1QGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUVkRlRwN0dKTHRBaGZRc2puTndUNjhaektGRkVFN2Vzel8za3FfendHbGM9czk2LWMiLCJlbWFpbCI6Inl0dHViZTM1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJBYmhpbmF2IEdveWFsIiwiaXNzIjoiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vdXNlcmluZm8vdjIvbWUiLCJuYW1lIjoiQWJoaW5hdiBHb3lhbCIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BRWRGVHA3R0pMdEFoZlFzam5Od1Q2OFp6S0ZGRUU3ZXN6XzNrcV96d0dsYz1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTAzNTAwMTQ2NjI3MDg2NzA0MDE4Iiwic3ViIjoiMTAzNTAwMTQ2NjI3MDg2NzA0MDE4In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE2NzEzNDc0MDV9XSwic2Vzc2lvbl9pZCI6IjQ1YzlhZjVkLWQwNjktNGRmZS1hMjM4LWM3ZTI3MmIxMmZiZiJ9.Jh9V_eSd7mwUoPulvLgHJ10uM4TrDWzJjopsCIJID8U",
        "content-type": "application/json",
        "origin": "https://www.orchard.ink",
        "referer": "https://www.orchard.ink/",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    }

    json_data = {
        "thread": {
            "id": "default",
            "createdAt": "2022-12-18T07:11:21.315Z",
            "messages": {
                "root": {
                    "id": "root",
                    "index": 0,
                    "createdAt": "2022-12-18T07:11:21.315Z",
                    "type": "response",
                    "messageText": "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    "innerText": "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    "childrenIds": [
                        "47fa4041-cd68-46cc-b901-532ecbeb71e2",
                    ],
                    "rejected": False,
                },
                "47fa4041-cd68-46cc-b901-532ecbeb71e2": {
                    "id": "47fa4041-cd68-46cc-b901-532ecbeb71e2",
                    "index": 1,
                    "createdAt": "2022-12-18T07:48:29.298Z",
                    "type": "instruction",
                    "messageText": prompt,
                    "innerText": "Hi, I'm Orchard! Ask me anything. If you want to edit your writing, select some text and you'll see a preview of it below. Try using a template from the dropdown!",
                    "childrenIds": [
                        "2159a744-9696-4a66-b020-d2a082452e05",
                    ],
                    "rejected": False,
                    "templateId": "2c77110a-5644-4a1e-bfe4-f0ed2aebc94a",
                    "iconKey": "Custom",
                    "parentId": "root",
                },
                "2159a744-9696-4a66-b020-d2a082452e05": {
                    "id": "2159a744-9696-4a66-b020-d2a082452e05",
                    "index": 1,
                    "createdAt": "2022-12-18T07:48:29.302Z",
                    "type": "response",
                    "messageText": "Loading Response #1...",
                    "innerText": "",
                    "childrenIds": [],
                    "rejected": False,
                    "parentId": "47fa4041-cd68-46cc-b901-532ecbeb71e2",
                },
            },
            "numResponses": 2,
            "numInstructions": 1,
        },
        "template_id": "2c77110a-5644-4a1e-bfe4-f0ed2aebc94a",
        "template_name": "Custom",
        "document_id": "f3560a80-d099-46c4-9c25-63f83b04527b",
        "is_retry": False,
    }

    response = requests.post(
        "https://api.orchard.ink/generate_responses", headers=headers, json=json_data
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"thread":{"id":"default","createdAt":"2022-12-18T07:11:21.315Z","messages":{"root":{"id":"root","index":0,"createdAt":"2022-12-18T07:11:21.315Z","type":"response","messageText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["47fa4041-cd68-46cc-b901-532ecbeb71e2"],"rejected":false},"47fa4041-cd68-46cc-b901-532ecbeb71e2":{"id":"47fa4041-cd68-46cc-b901-532ecbeb71e2","index":1,"createdAt":"2022-12-18T07:48:29.298Z","type":"instruction","messageText":"hi","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["2159a744-9696-4a66-b020-d2a082452e05"],"rejected":false,"templateId":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","iconKey":"Custom","parentId":"root"},"2159a744-9696-4a66-b020-d2a082452e05":{"id":"2159a744-9696-4a66-b020-d2a082452e05","index":1,"createdAt":"2022-12-18T07:48:29.302Z","type":"response","messageText":"Loading Response #1...","innerText":"","childrenIds":[],"rejected":false,"parentId":"47fa4041-cd68-46cc-b901-532ecbeb71e2"}},"numResponses":2,"numInstructions":1},"template_id":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","template_name":"Custom","document_id":"f3560a80-d099-46c4-9c25-63f83b04527b","is_retry":false}'
    # response = requests.post('https://api.orchard.ink/generate_responses', headers=headers, data=data)
    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"thread":{"id":"default","createdAt":"2022-12-15T07:18:26.968Z","messages":{"root":{"id":"root","index":0,"createdAt":"2022-12-15T07:18:26.968Z","type":"response","messageText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["a73979b6-9176-4586-9574-77269167e1a3"],"rejected":false},"a73979b6-9176-4586-9574-77269167e1a3":{"id":"a73979b6-9176-4586-9574-77269167e1a3","index":1,"createdAt":"2022-12-18T06:19:38.179Z","type":"instruction","messageText":"j","innerText":"Hi, I\'m Orchard! Ask me anything. If you want to edit your writing, select some text and you\'ll see a preview of it below. Try using a template from the dropdown!","childrenIds":["0a1fae92-8fa0-4f90-8209-bbbee6fb26f2"],"rejected":false,"templateId":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","iconKey":"Custom","parentId":"root"},"0a1fae92-8fa0-4f90-8209-bbbee6fb26f2":{"id":"0a1fae92-8fa0-4f90-8209-bbbee6fb26f2","index":1,"createdAt":"2022-12-18T06:19:38.183Z","type":"response","messageText":"Loading Response #1...","innerText":"","childrenIds":[],"rejected":false,"parentId":"a73979b6-9176-4586-9574-77269167e1a3"}},"numResponses":2,"numInstructions":1},"template_id":"2c77110a-5644-4a1e-bfe4-f0ed2aebc94a","template_name":"Custom","document_id":"f8589a2e-c594-498d-8e1a-9ee8fdca3320","is_retry":false}'
    # response = requests.post('https://api.orchard.ink/generate_responses', headers=headers, data=data)    return response

    print(response.text)

    return response


if __name__ == "__main__":
    print(get_orchard_response("what is your name?"))
