# 🧠 Image Captioning & Submission Pipeline

This Python script performs a full image-to-caption pipeline:

1. **Scrapes a base64-encoded image** from a webpage.
2. **Sends the image to a captioning model** for inference.
3. **Submits the model output** to a target evaluation endpoint.

---

## 📦 Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`

Install the required dependencies:

```bash
pip install requests beautifulsoup4
TOKEN = "<YOUR_API_TOKEN>"
SCRAPE_URL = "<URL_WITH_BASE64_IMAGE>"
INFERENCIA_URL = "<API_ENDPOINT_FOR_INFERENCE>"
SUBMIT_URL = "<API_ENDPOINT_FOR_SUBMISSION>"
python script.py
