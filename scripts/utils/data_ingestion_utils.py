import json
import requests
import time

# Questa funzione invia le credenziali di accesso a NiFi
def  access_to_nifi():
    url = "https://localhost:8443/nifi-api/access/token"
    payload = {"username":"admin", "password":"ProgettoSabd2026."}
    response = requests.post(url, data = payload, verify = False)
    response.raise_for_status()

    return response.text

# Questa funzione avvia un processor group
def start_processor_group(token, proc_group_id):
    url = f"https://localhost:8443/nifi-apiflow/processor-groups/{proc_group_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-type": "application/json"
    }

    payload = {
        "id": proc_group_id,
        "state": "RUNNING"
    }
    
    response = requests.put(url,
                           headers = headers,
                           data = json.dumps(payload))

    response.raise_for_status()


# Questa funzione controlla che il flusso di esecuzione di NiFi abbia terminato facendo polling sul numero di
def wait_for_completion(token, proc_group_id):
    url = f"https://localhost:8443/nifi-api/flow/process-groups/{proc_group_id}/status"

    headers = {
        "Authentication": f"Bearer {token}"
    }


    nifi_running = True

    while nifi_running:
        time.sleep(10)

        response = requests.get(url, headers = headers)
        response.raise_for_status()

        response = response.json()

        active_threads = int(response["processGroupStatus"]["aggregateSnapshot"]["activeThreadCount"])
        queued_count = int(response["processGorupStatus"]["aggregateSnapshot"]["queuedCount"])

        if active_threads == 0 and queued_count == 0:
            nifi_running = False