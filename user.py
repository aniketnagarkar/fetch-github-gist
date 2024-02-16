from flask import Flask, jsonify
import requests

app = Flask("git-hub-users")

GITHUB_API_URL = "https://api.github.com/users/{}/gists"


@app.route('/')
def get_gists():
    # Change 'octocat' to any username you want to fetch Gists for
    username = 'octocat'
    response = requests.get(GITHUB_API_URL.format(username))
    gists = response.json()
    return jsonify(gists)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
