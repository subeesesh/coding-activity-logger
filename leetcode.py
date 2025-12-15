import requests

LEETCODE_SESSION = "ADD YOUR LEETCODE SESSION"

def get_recent_leetcode(username, limit=20):
    url = "https://leetcode.com/graphql"

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}",
        "Referer": f"https://leetcode.com/u/{username}/"
    }

    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        title
        titleSlug
        timestamp
      }
    }
    """

    res = requests.post(
        url,
        headers=headers,
        json={
            "query": query,
            "variables": {
                "username": username,
                "limit": limit
            }
        }
    )

    return res.json().get("data", {}).get("recentAcSubmissionList", [])
