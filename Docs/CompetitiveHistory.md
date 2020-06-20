# Competitive History
Shows User' Competitve History, Including Match ID, Competitve Movement, And Tier after update.

**When RANKED Releases, I will update the page with actual competitve movements.**

## Template
Here is how to use `cURL` to get User's Competitve History:
- URL: `https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/competitiveupdates`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement
- Params:
    - startIndex: 0
    - endIndex: 10

## Example
```http
GET https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/competitiveupdates
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token

Optional Params:
 - startIndex = Usually 0
 - endIndex = Max of 10

{
    {
    "Version": 0,
    "Subject": "PLAYERID",
    "Matches": [
        {
            "MatchID": "94484eae-ba72-439c-b118-15f6267f810c",
            "MatchStartTime": 1591750167517,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "dc970654-05e7-44ec-be6e-178149e6ca39",
            "MatchStartTime": 1591583339273,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "d09968e3-36a9-4c3d-a72a-f22d20a83632",
            "MatchStartTime": 1591582913084,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "88aba068-744b-4165-9b47-3df22930d48c",
            "MatchStartTime": 1591582295482,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "262d0fcf-9ec1-4599-a000-dace92c884b0",
            "MatchStartTime": 1591581747411,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "ca5af5fd-01ef-4c8f-92f9-038c37c422ca",
            "MatchStartTime": 1591581119954,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "e9764cdc-9da9-4a33-8682-789225e09cd1",
            "MatchStartTime": 1591579039702,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "9eab26b7-5cf9-487a-97c0-d24f5ed2286e",
            "MatchStartTime": 1591576548603,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "0e5e1618-1f55-46e2-b52f-d21de45ad032",
            "MatchStartTime": 1591575863434,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        },
        {
            "MatchID": "4d0ae2b6-fb25-4904-b247-c0aebee28d53",
            "MatchStartTime": 1591574936253,
            "TierAfterUpdate": 0,
            "CompetitiveMovement": "MOVEMENT_UNKNOWN"
        }
    ]
}
}
```
