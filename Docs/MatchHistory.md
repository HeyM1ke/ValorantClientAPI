# Player Match History
Get Player's Match History.

## Template
Here is how to use `cURL` to get User's Match History:
- URL: `https://pd.na.a.pvp.net/match-history/v1/history/`PLAYERID`?startIndex=0&endIndex=10`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`
Params
 - startIndex = 0
 - endIndex = 10 (MAX 20)

## Example
```http
GET https://pd.na.a.pvp.net/match-history/v1/history/`PLAYERID`?startIndex=0&endIndex=10
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token

Params
 - startIndex = 0
 - endIndex = 10


{
    "Subject": "`PLAYERID`",
    "BeginIndex": 0,
    "EndIndex": 10,
    "Total": 74,
    "History": [
        {
            "MatchID": "d30314c7-4bdc-48bc-82f6-b27b6f3522e0",
            "GameStartTime": 1593051973449,
            "TeamID": "Red"
        },
        {
            "MatchID": "337c3e4b-1e4d-461d-b046-022733636430",
            "GameStartTime": 1593049455306,
            "TeamID": "Blue"
        },
        {
            "MatchID": "ca65500c-aa69-4e37-8e45-91cf8fe13e24",
            "GameStartTime": 1593044723451,
            "TeamID": "Blue"
        },
        {
            "MatchID": "49252f81-58cf-4d45-b37f-16cd146e46d3",
            "GameStartTime": 1593042279159,
            "TeamID": "Red"
        },
        {
            "MatchID": "d7d27ce8-5478-473d-88e3-e34bf723dc0e",
            "GameStartTime": 1593037448334,
            "TeamID": "Red"
        },
        {
            "MatchID": "1c508951-1516-4ec7-a640-431bbd567916",
            "GameStartTime": 1593035342618,
            "TeamID": "Blue"
        },
        {
            "MatchID": "d04acfb6-2f8b-49dd-a1ab-bfe9cce9c9fa",
            "GameStartTime": 1593032670758,
            "TeamID": "Blue"
        },
        {
            "MatchID": "f181fced-3b74-4682-a8b0-dc49d722c85c",
            "GameStartTime": 1592956257945,
            "TeamID": "Blue"
        },
        {
            "MatchID": "f7d4d413-440b-4ed7-9f7c-3d75589c33e0",
            "GameStartTime": 1592954303602,
            "TeamID": "Blue"
        },
        {
            "MatchID": "93d46223-8fcf-44dd-852d-c2ca3a8a4d7f",
            "GameStartTime": 1592951479707,
            "TeamID": "Red"
        }
    ]
}
```
