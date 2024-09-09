import mimetypes
import requests
from flask import Flask, Response, request

app = Flask(__name__)

HOSTS_URL = 'https://raw.githubusercontent.com/neoapps-dev/potatoes-hosts/main/HOSTS.txt'

def fetch_hosts():
    try:
        response = requests.get(HOSTS_URL)
        if response.status_code == 200:
            hosts_mapping = {}
            for line in response.text.splitlines():
                if line.strip():
                    potato_domain, destination = line.strip().split(': ')
                    hosts_mapping[potato_domain] = destination
            return hosts_mapping
        else:
            return None
    except Exception as e:
        print(f"Error fetching HOSTS.txt: {str(e)}")
        return None

def fetch_github_content(user, repo, branch):
    url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/web.potato"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "GitHub content not found", response.status_code

def fetch_url_content(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else "URL content not found", response.status_code

@app.route('/<pdomain>.potato', defaults={'subpath': ''})
@app.route('/<pdomain>.potato/<path:subpath>')
def resolve_potato(pdomain, subpath):
    hosts_mapping = fetch_hosts()

    if hosts_mapping is None:
        return "Error fetching HOSTS.txt", 500

    domain = f"{pdomain}.potato"
    query_params = request.query_string.decode()

    if domain in hosts_mapping:
        destination = hosts_mapping[domain]
        if destination.startswith("gh/"):
            try:
                _, user, repo, branch = destination.split('/')
                content, status_code = fetch_github_content(user, repo, branch)
                mimetype, _ = mimetypes.guess_type('web.potato')
                return Response(content, status=status_code, mimetype=mimetype or 'text/html')
            except Exception as e:
                return f"Error processing GitHub entry: {str(e)}", 500
        elif destination.startswith("http"):
            try:
                target_url = f"{destination}/{subpath}" if subpath else destination
                if query_params:
                    target_url = f"{target_url}?{query_params}"
                content, status_code = fetch_url_content(target_url)
                mimetype, _ = mimetypes.guess_type(target_url)
                return Response(content, status=status_code, mimetype=mimetype or 'text/html')
            except Exception as e:
                return f"Error fetching URL: {str(e)}", 500

    return "Invalid .potato domain", 404

if __name__ == "__main__":
    app.run(port=8080)
