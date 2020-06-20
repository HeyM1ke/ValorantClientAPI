# Player MMR
Get Player's MMR, Including Competitve Rank, and more.

## Template
Here is how to use `cURL` to get User's MMRs:
- URL: `https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/competitiveupdates`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`

## Example
```http
GET https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/competitiveupdates
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token


{
    "Version": 1591752354289,
    "Subject": "`PLAYERID`",
    "NewPlayerExperienceFinished": true 
    "QueueSkills": {
        "competitive": {
            "CompetitiveTier": 0,
            "TotalGamesNeededForRating": 5, 
            "RecentGamesNeededForRating": 1,
            "SeasonalInfoBySeasonID": null
        },
        "custom": {
            "CompetitiveTier": 0,
            "TotalGamesNeededForRating": 0,
            "RecentGamesNeededForRating": 0,
            "SeasonalInfoBySeasonID": {
                "0df5adb9-4dcb-6899-1306-3e9860661dd3": {
                    "SeasonID": "0df5adb9-4dcb-6899-1306-3e9860661dd3",
                    "NumberOfWins": 5,
                    "TopWins": [
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "RankIndex": 2,
                    "CapstoneWins": 5
                }
            }
        },
        "seeding": {
            "CompetitiveTier": 0,
            "TotalGamesNeededForRating": 4,
            "RecentGamesNeededForRating": 1,
            "SeasonalInfoBySeasonID": {}
        },
        "spikerush": {
            "CompetitiveTier": 0,
            "TotalGamesNeededForRating": 0,
            "RecentGamesNeededForRating": 0,
            "SeasonalInfoBySeasonID": {
                "0df5adb9-4dcb-6899-1306-3e9860661dd3": {
                    "SeasonID": "0df5adb9-4dcb-6899-1306-3e9860661dd3",
                    "NumberOfWins": 13,
                    "TopWins": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "RankIndex": 6, 
                    "CapstoneWins": 13
                }
            }
        },
        "unrated": {
            "CompetitiveTier": 0,
            "TotalGamesNeededForRating": 0,
            "RecentGamesNeededForRating": 0,
            "SeasonalInfoBySeasonID": {
                "": {
                    "SeasonID": "",
                    "NumberOfWins": 2,
                    "TopWins": [
                        0,
                        0
                    ],
                    "RankIndex": 1,
                    "CapstoneWins": 2
                },
                "0df5adb9-4dcb-6899-1306-3e9860661dd3": {
                    "SeasonID": "0df5adb9-4dcb-6899-1306-3e9860661dd3",
                    "NumberOfWins": 9,
                    "TopWins": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "RankIndex": 4,
                    "CapstoneWins": 9
                },
                "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3": {
                    "SeasonID": "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
                    "NumberOfWins": 0,
                    "TopWins": null,
                    "RankIndex": 0,
                    "CapstoneWins": 0
                }
            }
        }
    },
    "LatestCompetitiveUpdate": {
        "MatchID": "94484eae-ba72-439c-b118-15f6267f810c",
        "MatchStartTime": 1591750167517,
        "TierAfterUpdate": 0,
        "CompetitiveMovement": "MOVEMENT_UNKNOWN"
    }
}
```
