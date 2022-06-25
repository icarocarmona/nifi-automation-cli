import requests
import fire
import json
import os

USER = os.getenv('NIFI_USER')
PWD = os.getenv('NIFI_PWD')


def get_token(url, username, password):
    payload = f"username={username}&password={password}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.request(
        "POST", f"{url}/nifi-api/access/token", data=payload, headers=headers, verify=False)
    token = response.text
    return token


def get_variables(url, groupId, token):
    full_url = f"{url}/nifi-api/process-groups/{groupId}/variable-registry"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.request("GET", full_url, headers=headers, verify=False)
    data = response.json()
    return data


def set_variables(url, token, pgId, clientId, version, variable):
    headers = {
        'Authorization': f"Bearer {token}",
    }

    json_data = {
        'processGroupRevision': {
            'clientId': clientId,
            'version': version,
        },
        'variableRegistry': {
            'processGroupId': pgId,
            'variables': [
                {
                    'variable': {
                        'name': variable['key'],
                        'value': variable['value'],
                    },
                },
            ],
        },
    }

    response = requests.post(f'{url}/nifi-api/process-groups/{pgId}/variable-registry/update-requests',
                             headers=headers, json=json_data, verify=False)

    return response.text


def get_pgRevision(processGroup):
    data = {
        'clientId': processGroup['processGroupRevision']['clientId'],
        'version': processGroup['processGroupRevision']['version']
    }
    return data


def get_file(path):
    f = open(path)
    return json.load(f)


def import_vars(nifi_uri, path_json, pgid):
    token = get_token(nifi_uri, USER, PWD)
    processGroup = get_variables(nifi_uri, pgid, token)
    pgRevision = get_pgRevision(processGroup)

    data = get_file(path_json)
    for key in data:
        variable = {
            'key': key,
            'value': data[key]
        }
        res = set_variables(
            nifi_uri, token, pgid, pgRevision['clientId'], pgRevision['version'], variable
        )
        print(res)


def set_var_context(url, token):
    headers = {
        'Authorization': f"Bearer {token}",
    }

    json_data = {
        "component": {
            "name": "teste123",
            "description": "TESTE",
            "parameters": []
        },
        "revision": {
            "clientId": "8196f974-0181-1000-b07d-330bc4887bdc",
            "version": 0
        }
    }

    response = requests.post(f'{url}/nifi-api/parameter-contexts',
                             headers=headers, json=json_data, verify=False)
    print(response.text)
    return response.text


if __name__ == '__main__':
    fire.Fire()
