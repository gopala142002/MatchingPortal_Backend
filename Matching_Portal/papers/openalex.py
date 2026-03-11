import requests

# ======================================================
# OpenAlex Config
# ======================================================

HEADERS = {
    "User-Agent": "PaperMatchingPortal/1.0 (mailto:your_email@example.com)"
}

OPENALEX_AUTHOR_API = "https://api.openalex.org/authors"


# ======================================================
# Fetch Affiliations for an Author Name
# ======================================================

def fetch_affiliations(author_name: str):
    """
    Fetch affiliations of an author from OpenAlex.

    Returns:
    [
        {
            "openalex_id": "...",
            "name": "...",
            "country": "..."
        }
    ]
    """

    params = {
        "search": author_name,
        "per-page": 5
    }

    try:
        response = requests.get(
            OPENALEX_AUTHOR_API,
            params=params,
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()

    except requests.RequestException:
        return []

    results = response.json().get("results", [])
    affiliations = []

    # ==================================================
    # Collect affiliations from top matching authors
    # ==================================================

    for author in results:

        # ✅ 1. Affiliations list (multiple institutions)
        for aff in author.get("affiliations", []):
            inst = aff.get("institution")

            if inst and inst.get("display_name"):
                affiliations.append({
                    "openalex_id": inst.get("id"),
                    "name": inst.get("display_name"),
                    "country": inst.get("country_code"),
                })

        # ✅ 2. Fallback: last known institution
        inst = author.get("last_known_institution")

        if inst and inst.get("display_name"):
            affiliations.append({
                "openalex_id": inst.get("id"),
                "name": inst.get("display_name"),
                "country": inst.get("country_code"),
            })

    # ==================================================
    # Remove duplicates safely
    # ==================================================

    unique = {}
    for a in affiliations:
        key = a.get("openalex_id") or a.get("name")

        if key:
            unique[key] = a

    return list(unique.values())
