# Competitive History
Shows User' Competitive History, Including Match ID, Competitive Movement, And Tier after update, TierBeforeUpdate, RankedRatingEarned, and etc.

## Template
Here is how to use `cURL` to get User's Competitive History:
- URL: `https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/competitiveupdates`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`
    - X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
    - X-Riot-ClientVersion: `versionNumber`
- Params:
    - startIndex: 0
    - endIndex: 10

## Example
```http
GET https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/competitiveupdates
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token
X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
X-Riot-ClientVersion: `release-02.01-shipping-6-511946`
Optional Params:
- Indexs must go at a maximum interval of 20 per request so 0-20, 20-40, 40-60, 60-80, 80-100. When you get an error, this means the player has no more matches.

 - startIndex = Usually 0
 - endIndex = Max of 20

{
    {
    "Version": 0,
    "Subject": "PLAYERID",
    "Matches": [
    {
          "MatchID": "290d62cd-5cdd-49fc-bf04-e285512345cf",
          "MapID": "/Game/Maps/Bonsai/Bonsai",
          "MatchStartTime": 1611011859227,
          "TierAfterUpdate": 16,
          "TierBeforeUpdate": 16,
          "RankedRatingAfterUpdate": 37,
          "RankedRatingBeforeUpdate": 57,
          "RankedRatingEarned": -20,
          "RankedRatingPerformanceBonus": 0,
          "CompetitiveMovement": "MOVEMENT_UNKNOWN",
          "AFKPenalty": 0
      },
      {
          "MatchID": "7d1318d1-ff9c-4998-8614-c556de8e29e8",
          "MapID": "/Game/Maps/Ascent/Ascent",
          "MatchStartTime": 1611007612728,
          "TierAfterUpdate": 16,
          "TierBeforeUpdate": 16,
          "RankedRatingAfterUpdate": 57,
          "RankedRatingBeforeUpdate": 77,
          "RankedRatingEarned": -20,
          "RankedRatingPerformanceBonus": 0,
          "CompetitiveMovement": "MOVEMENT_UNKNOWN",
          "AFKPenalty": 0
      },
      {
          "MatchID": "7654efcd-bdf0-43c3-ae05-a49fd5bb46c7",
          "MapID": "/Game/Maps/Bonsai/Bonsai",
          "MatchStartTime": 1611005000820,
          "TierAfterUpdate": 16,
          "TierBeforeUpdate": 16,
          "RankedRatingAfterUpdate": 77,
          "RankedRatingBeforeUpdate": 48,
          "RankedRatingEarned": 29,
          "RankedRatingPerformanceBonus": 0,
          "CompetitiveMovement": "MOVEMENT_UNKNOWN",
          "AFKPenalty": 0
      },
      {
          "MatchID": "da4120e8-64ca-4710-8551-f6dce1629cbd",
          "MapID": "/Game/Maps/Triad/Triad",
          "MatchStartTime": 1610992144578,
          "TierAfterUpdate": 16,
          "TierBeforeUpdate": 16,
          "RankedRatingAfterUpdate": 48,
          "RankedRatingBeforeUpdate": 73,
          "RankedRatingEarned": -25,
          "RankedRatingPerformanceBonus": 0,
          "CompetitiveMovement": "MOVEMENT_UNKNOWN",
          "AFKPenalty": 0
      },
      {
          "MatchID": "9bfe5f5a-e893-4d93-9888-ae94e44da714",
          "MapID": "/Game/Maps/Bonsai/Bonsai",
          "MatchStartTime": 1610989021023,
          "TierAfterUpdate": 16,
          "TierBeforeUpdate": 16,
          "RankedRatingAfterUpdate": 73,
          "RankedRatingBeforeUpdate": 95,
          "RankedRatingEarned": -22,
          "RankedRatingPerformanceBonus": 0,
          "CompetitiveMovement": "MOVEMENT_UNKNOWN",
          "AFKPenalty": 0
      },
      {
          "MatchID": "bf6b97b1-1bd6-4ebc-bc06-ac6190a46fa9",
          "MapID": "/Game/Maps/Duality/Duality",
          "MatchStartTime": 1610986666150,
          "TierAfterUpdate": 16,
          "TierBeforeUpdate": 16,
          "RankedRatingAfterUpdate": 95,
          "RankedRatingBeforeUpdate": 69,
          "RankedRatingEarned": 26,
          "RankedRatingPerformanceBonus": 0,
          "CompetitiveMovement": "MOVEMENT_UNKNOWN",
          "AFKPenalty": 0
      },
    ]
}
}
```
