import requests

LEETCODE_SESSION = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMTMzOTAyNzMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImFlNDhmM2I1ZWYxOWYwNDE3NGY3ZWEyNzA1MmIwOTc1MzliY2I1YTgyM2YwNmE3YWE3M2YyZGM0NDRhMDc0MmIiLCJzZXNzaW9uX3V1aWQiOiJlNTAyM2I5NCIsImlkIjoxMzM5MDI3MywiZW1haWwiOiJzdWJlZXNlc2gwMkBnbWFpbC5jb20iLCJ1c2VybmFtZSI6InN1YmVlXzAyIiwidXNlcl9zbHVnIjoic3ViZWVfMDIiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvc3ViZWVfMDIvYXZhdGFyXzE3MTYxMTQ1NzMucG5nIiwicmVmcmVzaGVkX2F0IjoxNzY1NzY5NDU2LCJpcCI6IjI0MDI6M2E4MDoxMzNiOjM4MzQ6YTQ2ODoxMGZlOjU2YjpiMmJiIiwiaWRlbnRpdHkiOiI4OWRiNzI5Y2ZjZGMxMjkxMTFmMDE3YjBlN2FjMzI0YSIsImRldmljZV93aXRoX2lwIjpbIjU3MDE2Yjk2MzVmNzAxMmYzYjgxYmZmM2JlOWU1MWM5IiwiMjQwMjozYTgwOjEzM2I6MzgzNDphNDY4OjEwZmU6NTZiOmIyYmIiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.03TkcSBIz3tRf87xPTVpmcWlI3ZozbHIYoW4ZmOsbiU"

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
