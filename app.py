from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def analyze_url(url: str) -> str:
    lower_case_url = url.lower()

    # Basic phishing detection criteria
    suspicious_domains = ['phishingsite.com', 'fakebank.com', 'secure-login.com']
    has_suspicious_domain = any(domain in lower_case_url for domain in suspicious_domains)
    lacks_https = not lower_case_url.startswith('https://')

    if has_suspicious_domain or lacks_https:
        return 'Phishing'
    return 'Safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url', '')
    result = analyze_url(url)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)