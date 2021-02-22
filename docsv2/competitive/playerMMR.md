# Player MMR
Get Player's MMR, Including Competitve Rank, and more.

## Template
Here is how to use `cURL` to get User's MMRs:
- URL: `https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`
    - X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
    - X-Riot-ClientVersion: `release-02.01-shipping-6-511946`
## Example
```http
GET https://pd.na.a.pvp.net/mmr/v1/players/`PLAYERID`/
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token
X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
X-Riot-ClientVersion: `release-02.01-shipping-6-511946`


{
    "Version": 1611024462530,
    "Subject": "[PLAYERID]",
    "NewPlayerExperienceFinished": true,
    "QueueSkills": {
        "competitive": {
            "CompetitiveTier": 16,
            "TierProgress": 37,
            "TotalGamesNeededForRating": 0,
            "CurrentSeasonGamesNeededForRating": 0,
            "TotalGamesNeededForLeaderboard": 0,
            "SeasonalInfoBySeasonID": {
                "0530b9c4-4980-f2ee-df5d-09864cd00542": {
                    "SeasonID": "0530b9c4-4980-f2ee-df5d-09864cd00542",
                    "NumberOfWins": 14,
                    "NumberOfWinsWithPlacements": 17,
                    "NumberOfGames": 38,
                    "TopWins": [
                        18,
                        18,
                        17,
                        17,
                        17,
                        17,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16
                    ],
                    "TotalWinsNeededForRank": 0,
                    "Rank": 16,
                    "CapstoneWins": 2,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 17,
                    "RankedRating": 0
                },
                "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3": {
                    "SeasonID": "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
                    "NumberOfWins": 48,
                    "NumberOfWinsWithPlacements": 49,
                    "NumberOfGames": 96,
                    "TopWins": [
                        17,
                        17,
                        17,
                        17,
                        17,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        14,
                        14,
                        14,
                        14,
                        14,
                        14,
                        14,
                        13,
                        13,
                        13
                    ],
                    "TotalWinsNeededForRank": 0,
                    "Rank": 16,
                    "CapstoneWins": 5,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 17,
                    "RankedRating": 0
                },
                "46ea6166-4573-1128-9cea-60a15640059b": {
                    "SeasonID": "46ea6166-4573-1128-9cea-60a15640059b",
                    "NumberOfWins": 38,
                    "NumberOfWinsWithPlacements": 39,
                    "NumberOfGames": 79,
                    "TopWins": [
                        18,
                        18,
                        18,
                        18,
                        18,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        17,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        14
                    ],
                    "TotalWinsNeededForRank": 0,
                    "Rank": 17,
                    "CapstoneWins": 5,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 18,
                    "RankedRating": 1832
                },
                "97b6e739-44cc-ffa7-49ad-398ba502ceb0": {
                    "SeasonID": "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
                    "NumberOfWins": 20,
                    "NumberOfWinsWithPlacements": 21,
                    "NumberOfGames": 44,
                    "TopWins": [
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        16,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        15,
                        14,
                        14,
                        14
                    ],
                    "TotalWinsNeededForRank": 0,
                    "Rank": 15,
                    "CapstoneWins": 7,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 16,
                    "RankedRating": 37
                }
            }
        },
        "custom": {
            "CompetitiveTier": 0,
            "TierProgress": 0,
            "TotalGamesNeededForRating": 0,
            "CurrentSeasonGamesNeededForRating": 3,
            "TotalGamesNeededForLeaderboard": 4,
            "SeasonalInfoBySeasonID": {
                "0530b9c4-4980-f2ee-df5d-09864cd00542": {
                    "SeasonID": "0530b9c4-4980-f2ee-df5d-09864cd00542",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 3,
                    "NumberOfGames": 4,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "0df5adb9-4dcb-6899-1306-3e9860661dd3": {
                    "SeasonID": "0df5adb9-4dcb-6899-1306-3e9860661dd3",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 5,
                    "NumberOfGames": 8,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3": {
                    "SeasonID": "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 3,
                    "NumberOfGames": 29,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "46ea6166-4573-1128-9cea-60a15640059b": {
                    "SeasonID": "46ea6166-4573-1128-9cea-60a15640059b",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 3,
                    "NumberOfGames": 3,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "97b6e739-44cc-ffa7-49ad-398ba502ceb0": {
                    "SeasonID": "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 2,
                    "NumberOfGames": 2,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                }
            }
        },
        "deathmatch": {
            "CompetitiveTier": 0,
            "TierProgress": 0,
            "TotalGamesNeededForRating": 0,
            "CurrentSeasonGamesNeededForRating": 0,
            "TotalGamesNeededForLeaderboard": 18,
            "SeasonalInfoBySeasonID": {
                "0530b9c4-4980-f2ee-df5d-09864cd00542": {
                    "SeasonID": "0530b9c4-4980-f2ee-df5d-09864cd00542",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 0,
                    "NumberOfGames": 15,
                    "TopWins": null,
                    "TotalWinsNeededForRank": 0,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "46ea6166-4573-1128-9cea-60a15640059b": {
                    "SeasonID": "46ea6166-4573-1128-9cea-60a15640059b",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 0,
                    "NumberOfGames": 11,
                    "TopWins": null,
                    "TotalWinsNeededForRank": 0,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "97b6e739-44cc-ffa7-49ad-398ba502ceb0": {
                    "SeasonID": "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 0,
                    "NumberOfGames": 6,
                    "TopWins": null,
                    "TotalWinsNeededForRank": 0,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                }
            }
        },
        "seeding": {
            "CompetitiveTier": 0,
            "TierProgress": 0,
            "TotalGamesNeededForRating": 4,
            "CurrentSeasonGamesNeededForRating": 5,
            "TotalGamesNeededForLeaderboard": 49,
            "SeasonalInfoBySeasonID": {
                "97b6e739-44cc-ffa7-49ad-398ba502ceb0": {
                    "SeasonID": "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 0,
                    "NumberOfGames": 0,
                    "TopWins": null,
                    "TotalWinsNeededForRank": 0,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                }
            }
        },
        "spikerush": {
            "CompetitiveTier": 0,
            "TierProgress": 0,
            "TotalGamesNeededForRating": 0,
            "CurrentSeasonGamesNeededForRating": 5,
            "TotalGamesNeededForLeaderboard": 0,
            "SeasonalInfoBySeasonID": {
                "0530b9c4-4980-f2ee-df5d-09864cd00542": {
                    "SeasonID": "0530b9c4-4980-f2ee-df5d-09864cd00542",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 5,
                    "NumberOfGames": 9,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "0df5adb9-4dcb-6899-1306-3e9860661dd3": {
                    "SeasonID": "0df5adb9-4dcb-6899-1306-3e9860661dd3",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 13,
                    "NumberOfGames": 23,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3": {
                    "SeasonID": "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 15,
                    "NumberOfGames": 32,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "46ea6166-4573-1128-9cea-60a15640059b": {
                    "SeasonID": "46ea6166-4573-1128-9cea-60a15640059b",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 17,
                    "NumberOfGames": 34,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "97b6e739-44cc-ffa7-49ad-398ba502ceb0": {
                    "SeasonID": "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 0,
                    "NumberOfGames": 0,
                    "TopWins": null,
                    "TotalWinsNeededForRank": 0,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                }
            }
        },
        "unrated": {
            "CompetitiveTier": 0,
            "TierProgress": 0,
            "TotalGamesNeededForRating": 0,
            "CurrentSeasonGamesNeededForRating": 2,
            "TotalGamesNeededForLeaderboard": 0,
            "SeasonalInfoBySeasonID": {
                "": {
                    "SeasonID": "",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 2,
                    "NumberOfGames": 4,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "0530b9c4-4980-f2ee-df5d-09864cd00542": {
                    "SeasonID": "0530b9c4-4980-f2ee-df5d-09864cd00542",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 6,
                    "NumberOfGames": 11,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "0df5adb9-4dcb-6899-1306-3e9860661dd3": {
                    "SeasonID": "0df5adb9-4dcb-6899-1306-3e9860661dd3",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 9,
                    "NumberOfGames": 25,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3": {
                    "SeasonID": "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 9,
                    "NumberOfGames": 22,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "46ea6166-4573-1128-9cea-60a15640059b": {
                    "SeasonID": "46ea6166-4573-1128-9cea-60a15640059b",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 13,
                    "NumberOfGames": 28,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                },
                "97b6e739-44cc-ffa7-49ad-398ba502ceb0": {
                    "SeasonID": "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
                    "NumberOfWins": 0,
                    "NumberOfWinsWithPlacements": 1,
                    "NumberOfGames": 3,
                    "TopWins": [],
                    "TotalWinsNeededForRank": 9,
                    "Rank": 0,
                    "CapstoneWins": 0,
                    "LeaderboardRank": 0,
                    "CompetitiveTier": 0,
                    "RankedRating": 0
                }
            }
        }
    },
    "LatestCompetitiveUpdate": {
        "MatchID": "c266f625-4fa5-4e4e-a689-7fdc4f65356e",
        "MapID": "/Game/Maps/Triad/Triad",
        "MatchStartTime": 1611023187983,
        "TierAfterUpdate": 0,
        "TierBeforeUpdate": 0,
        "RankedRatingAfterUpdate": 0,
        "RankedRatingBeforeUpdate": 0,
        "RankedRatingEarned": 0,
        "RankedRatingPerformanceBonus": 0,
        "CompetitiveMovement": "MOVEMENT_UNKNOWN",
        "AFKPenalty": 0
    },
    "IsLeaderboardAnonymized": false
}
```
