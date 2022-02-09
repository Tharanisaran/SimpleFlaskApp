from flask import Flask, request
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
possible_pages = ["contact","contactus","signup","signin","login","register","account","home"]

users = {
    "tharani" : generate_password_hash("captcha$0lver")
}

@auth.verify_password
def verify_password(username,password):
    if username in users and \
        check_password_hash(users.get(username),password):
        return username

@app.route('/api/v1.0/get/candidate_urls_from_domain', methods=['POST'])
@auth.login_required
def get_candidateUrls():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        result_array = ["https://www."+json['domain']+"/"+url for url in possible_pages]
        print(result_array)
        message={
            "result": result_array
        }
        response = jsonify(message)
        return response
    else:
        return {"error":"Content type not supported"}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005)