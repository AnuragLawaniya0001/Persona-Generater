import requests

def extract_username(profile_url):
    if profile_url.endswith('/'):
        profile_url = profile_url[:-1]
    return profile_url.split('/')[-1]

def fetch_reddit_json(username, category, max_items=20):
    url = f"https://www.reddit.com/user/{username}/{category}.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch {category}. Status code: {response.status_code}")
        return []

    data = response.json()
    items = data.get("data", {}).get("children", [])

    results = []
    for item in items[:max_items]:
        kind = item["kind"]
        content = item["data"]

        if category == "comments":
            text = content.get("body", "").strip()
            results.append(f"Comment: {text}")
        elif category == "submitted":
            title = content.get("title", "").strip()
            selftext = content.get("selftext", "").strip()
            full_post = f"{title} - {selftext}" if selftext else title
            results.append(f"Post: {full_post}")

    return results


def scrape_reddit_user(username, max_items=20):
    print(f"Scraping user: {username} via Reddit JSON")

    comments = fetch_reddit_json(username, "comments", max_items)
    posts = fetch_reddit_json(username, "submitted", max_items)

    print(f" Fetched {len(posts)} posts and {len(comments)} comments.")
    return comments + posts



def generate_persona_with_gemini(reddit_texts, username, api_key):
    combined_text = "\n\n".join(reddit_texts)

    prompt = f"""
Using the following Reddit comments and posts, generate a detailed user persona. Include:
- Name 
- Age (guess if possible)
- Occupation
- Location (if inferred)
- Personality
- Behavior & Habits
- Motivations
- Frustrations
- Goals & Needs

For each section, cite which comment or post you used as evidence.

Reddit Data:
{combined_text}
"""


    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(endpoint, headers=headers, json=body)

    if response.status_code == 200:
        data = response.json()
        if "candidates" in data and len(data["candidates"]) > 0:
            result = data["candidates"][0]["content"]["parts"][0]["text"]
            with open(f"{username}_persona.txt", "w", encoding="utf-8") as f:
                f.write(result)
            print(f" Persona saved to {username}_persona.txt")
        else:
            print(" Gemini returned no result.")
    else:
        print(f"Gemini API Error {response.status_code}: {response.text}")


def run(profile_url, api_key):
    username = extract_username(profile_url)
    print(f" Scraping Reddit user: {username}")

    reddit_texts = scrape_reddit_user(username)
    if not reddit_texts:
        print(" No content found for user.")
        return

    print(f" Generating persona using Gemini for {username}...")
    generate_persona_with_gemini(reddit_texts, username, api_key)



if __name__ == "__main__":
    profile_url = "https://www.reddit.com/user/kojied/"
    api_key = "AIzaSyBdczkfr5YO7VPz-KR0_EwHa6cTGaoaps0" 
    run(profile_url, api_key)




