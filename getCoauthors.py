import requests
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.semanticscholar.org/graph/v1"
HEADERS = {"x-api-key": API_KEY}


def get_author_id(author_name):
    url = f"{BASE_URL}/author/search"
    params = {
        "query": author_name,
        "limit": 1,
        "fields": "name"
    }

    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    data = response.json()
    if not data.get("data"):
        raise ValueError("Author not found")

    return data["data"][0]["authorId"]


def get_last_5_years_coauthors(author_name):
    current_year = datetime.now().year
    start_year = current_year - 5

    # Step 1: Get author ID
    author_id = get_author_id(author_name)
    print(f"Found Author ID: {author_id}")

    # Step 2: Fetch papers
    url = f"{BASE_URL}/author/{author_id}/papers"
    params = {
        "fields": "title,year,authors",
        "limit": 1000  # increase if needed
    }

    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    papers = response.json().get("data", [])

    coauthors = set()

    for paper in papers:
        year = paper.get("year")
        if year and year >= start_year:
            for author in paper.get("authors", []):
                if author["authorId"] != author_id:
                    coauthors.add(author["name"])

    return list(coauthors)


if __name__ == "__main__":
    author_name = input("Enter author name: ")
    collaborators = get_last_5_years_coauthors(author_name)

    print("\nCo-authors in last 5 years:")
    for name in collaborators:
        print("-", name)

    print(f"\nTotal unique collaborators: {len(collaborators)}")