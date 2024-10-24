import requests

url = "https://www.virustotal.com/api/v3/files"
api = open('.env', 'r').read().strip()
file_path = input("Enter the path of the file>>> ")

with open(file_path, 'rb') as file:
    headers = {
        "accept": "application/json",
        "x-apikey": api
    }

    response = requests.post(url, files={'file': file}, headers=headers)

    if response.status_code == 200:
        analysis_id = response.json()['data']['id']
        analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

        analysis_response = requests.get(analysis_url, headers=headers)

        if analysis_response.status_code == 200:
            analysis_data = analysis_response.json()
            attributes = analysis_data['data']['attributes']
            status = attributes['status']
            results = attributes['results']
            stats = attributes['stats']
            file_info = analysis_data['meta']['file_info']

            print(f"\nScan Status: {status}")
            print(f"Total Malicious: {stats['malicious']}")
            print(f"Total Undetected: {stats['undetected']}")

            print("\nDetailed Scan Results:")
            for engine, result in results.items():
                print(f"{engine} (Version: {result['engine_version']}):")
                print(f"  Method: {result['method']}")
                print(f"  Category: {result['category']}")
                print(f"  Result: {result['result'] if result['result'] else 'No result'}")
                print(f"  Last Updated: {result['engine_update']}")

            print("\nFile Information:")
            print(f"SHA256: {file_info['sha256']}")
            print(f"MD5: {file_info['md5']}")
            print(f"SHA1: {file_info['sha1']}")
            print(f"File Size: {file_info['size']} bytes")
        else:
            print(f"Error retrieving analysis: {analysis_response.status_code} - {analysis_response.text}")
    else:
        print(f"Error uploading file: {response.status_code} - {response.text}")
