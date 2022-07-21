# New Endpoints and updated documentation are being added over time.

# Community Developer Discord: https://discord.gg/a9yzrw3KAm

# Valorant Client API

Research on Valorant's In-Game|In-Client API, All of the Information I currently have are provided within the [Docs](https://github.com/RumbleMike/ValorantAPI/tree/master/Docs) Folder.

## PSA

- Please understand that Riot has their servers split up between regions, so each region has their own URL.
- (Listed below are the ones i know. If you know other regions id's please send a message over to me on discord 'RumbleMike#5406')
- All examples within [Docs](https://github.com/RumbleMike/ValorantAPI/tree/master/Docs) are directed to the NA Region.

| Region        | URL                      |
| ------------- | ------------------------ |
| North America | https://pd.NA.a.pvp.net/ |
| Europe        | https://pd.EU.a.pvp.net/ |
| Asia Pacific  | https://pd.AP.a.pvp.net/ |
| Korea         | https://pd.KR.a.pvp.net/ |

## Authentication

Each API Request requires 2 Headers for authentication.
`X-Riot-Entitlements-JWT` & `Authentication`

# Table of Contents

This is here to make your life easier, whenever there is a new addition it gets added here. (Categories will be added in the future.)
Please check out [Getting Started](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/GettingStarted.md) for an easy Python script that replicates RSO and provides your X-Riot-Entitlements-JWT & Authentication Token.

- [Getting Started](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/GettingStarted.md)
- User API's
  - [Player ID](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/PlayerID.md)
  - [User Balance](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/UserBalance.md)
  - [Competitive History](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/CompetitiveHistory.md)
  - [Player MMR](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/PlayerMMR.md)
  - [Player Store](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/PlayerStore.md)
  - [Player Inventory | Coming Soon](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/PlayerInventory.md)
- Information API's
  - [Story Contract](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/StoryContract.md)
  - [ID List](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/IDList.md)
  - [Client Versions](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/ClientVersions.md)
  - [**Username From ID**](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/GetUserfromID.md)
- Match Information APIs
  - [Match History](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/MatchHistory.md)
  - [Match Info | Coming Soon]()
