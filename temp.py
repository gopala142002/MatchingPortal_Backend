import requests
HEADERS = {
    "User-Agent": "AffiliationFetcher/1.0 (mailto:temp@example.com)"
}
OPENALEX_AUTHOR_API = "https://api.openalex.org/authors"
def normalize(name: str) -> str:
    return name.lower().replace(".", "").strip()

def get_affiliations_from_openalex(author_name: str):   

    params = {
        "search": author_name,
        "per-page": 10
    }

    try:
        r = requests.get(
            OPENALEX_AUTHOR_API,
            params=params,
            headers=HEADERS,
            timeout=15
        )
        r.raise_for_status()
    except requests.RequestException as e:
        print("OpenAlex request failed:", e)
        return []
    data = r.json().get("results", [])
    input_name = normalize(author_name)
    affiliations = set()
    for author in data:
        display_name = normalize(author.get("display_name", ""))
        if display_name != input_name:
            continue
        for aff in author.get("affiliations", []):
            inst = aff.get("institution", {}).get("display_name")
            if inst:
                affiliations.add(inst)
    return list(affiliations)

if __name__ == "__main__":
    name = input("Enter author name (exact): ").strip()
    result = get_affiliations_from_openalex(name)
    if not result:
        print("NULL")
    else:
        for aff in result:
            print("-", aff)

