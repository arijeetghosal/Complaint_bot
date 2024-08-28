import requests


pipedrive_api_key = 'Your_Key'
openai_api_key = "Your_key"

def get_pipedrive_data(deal_id):
    url = f'https://api.pipedrive.com/v1/deals/{deal_id}?api_token={pipedrive_api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['data']
    else:
        return f"Error: {response.status_code} - {response.text}"

def extract_timeline(pipedrive_data):
    activities = pipedrive_data.get('activities', [])
    timeline = ""
    for activity in activities:
        date = activity.get('due_date', 'Unknown Date')
        summary = activity.get('subject', 'No subject')
        timeline += f"- {date}: {summary}\n"
    return timeline or "No recorded activities."

def generate_complaint_report(deal_id, complaint_subject):
    pipedrive_data = get_pipedrive_data(deal_id)
    
    if isinstance(pipedrive_data, str):  
        return pipedrive_data
    
    
    complaint_details = pipedrive_data.get('title', 'No title found')

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a complaint bot. Generate a report based on Pipedrive data for a lawyer."},
            {"role": "user", "content": f"Given the following data: {complaint_details}, generate a complaint report."}
        ],
        "max_tokens": 4096
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

