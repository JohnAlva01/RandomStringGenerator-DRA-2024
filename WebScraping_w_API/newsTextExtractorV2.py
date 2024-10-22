import requests

# Your GNews API key
API_KEY = "b4eaec330f9b48b1fd64c6d0b0424dfa"

# Define the endpoint and parameters
url = 'https://gnews.io/api/v4/search'
# can define parameters which api will use to filter reponses
params = {
    'q': 'energy',  # Search query with what we want to find
    'token': API_KEY,      # Your API key
    'lang': 'en',          # Language of the news articles
    'max': 100,              # Maximum number of articles to retrieve
    'expand': 'content'
}

# Make the request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)
    articles = data.get('articles', [])
    
    # Extract and print the title and content of each article
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Content: {article['content']}\n")
else:
    print(f"Error: {response.status_code}")
