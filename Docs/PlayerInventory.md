# Player Inventory
Get Player's Current Inventory Loadout. (Please Refer to [ID List](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/IDList.md) to match IDS with Skins.)

## Template
Here is how to use `cURL` to get User's MMRs:
- URL: `https://pd.na.a.pvp.net/personalization/v2/players/`PLAYERID`/playerloadout`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`

## Example
```http
GET https://pd.na.a.pvp.net/personalization/v2/players/`PLAYERID`/playerloadout
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token

{
    "Subject": "`PLAYERID`",
    "Version": 38,
    "Guns": [
        {
            "ID": "63e6c2b6-4a8e-869c-3d4c-e38355226584",
            "SkinID": "f454efd1-49cb-372f-7096-d394df615308",
            "SkinLevelID": "d91fb318-4e40-b4c9-8c0b-bb9da28bac55",
            "ChromaID": "2f93861d-4b2f-2175-af0c-3ba0c736e257",
            "Attachments": []
        },
        {
            "ID": "55d8a0f4-4274-ca67-fe2c-06ab45efdf58",
            "SkinID": "5305d9c4-4f46-fbf4-9e9a-dea772c263b5",
            "SkinLevelID": "0f5f60f4-4c94-e4b2-ceab-e2b4e8b41784",
            "ChromaID": "b33de820-4061-8b85-31ce-808f1a2c58f5",
            "Attachments": []
        },
        {
            "ID": "9c82e19d-4575-0200-1a81-3eacf00cf872",
            "SkinID": "b9ee2457-481c-6776-3f5b-0ca8e8f90c89",
            "SkinLevelID": "22821a32-4e04-ad4a-1893-95904c08b264",
            "ChromaID": "cd3ebdc1-4858-efda-6cee-c683726f8ca9",
            "CharmInstanceID": "54c0efe7-eb74-4296-b315-c3f30d618190",
            "CharmID": "57bc159c-4bf9-1963-884a-a387e69013be",
            "CharmLevelID": "cc4be40d-47e0-7f1e-2e30-9b90ce2607cd",
            "Attachments": []
        },
        {
            "ID": "ae3de142-4d85-2547-dd26-4e90bed35cf7",
            "SkinID": "199b8536-488a-09e6-8592-ff9cf21b4ceb",
            "SkinLevelID": "49fc11b3-40a9-29ff-a701-63a6f59e2a0f",
            "ChromaID": "561fa49e-465e-51eb-4517-93ab0105ff44",
            "Attachments": []
        },
        {
            "ID": "ee8e8d15-496b-07ac-e5f6-8fae5d4c7b1a",
            "SkinID": "8db507b5-4d57-96e0-000e-2d8c8af79550",
            "SkinLevelID": "d39a4263-49d3-f2e0-2c13-c299f8644518",
            "ChromaID": "2e3b98b6-46e9-e233-1e1b-269ebd84598a",
            "CharmInstanceID": "a65a559c-a64f-412e-89cc-062c95fd301c",
            "CharmID": "57bc159c-4bf9-1963-884a-a387e69013be",
            "CharmLevelID": "cc4be40d-47e0-7f1e-2e30-9b90ce2607cd",
            "Attachments": []
        },
        {
            "ID": "ec845bf4-4f79-ddda-a3da-0db3774b2794",
            "SkinID": "acd26127-48ff-8b9e-7ba6-b989af8a4b24",
            "SkinLevelID": "6942d8d1-4370-a144-2140-22a6d2be2697",
            "ChromaID": "b71ae8d6-44bb-aa4c-0d2a-dc9ed9e66410",
            "Attachments": []
        },
        {
            "ID": "910be174-449b-c412-ab22-d0873436b21b",
            "SkinID": "75e55415-45ce-b48b-b471-84bef2368e33",
            "SkinLevelID": "4caa7fb0-4751-52f3-6eed-6ab6232be131",
            "ChromaID": "8bb9c93c-4f27-89f8-3bf7-06b9101daa85",
            "Attachments": []
        },
        {
            "ID": "44d4e95c-4157-0037-81b2-17841bf2e8e3",
            "SkinID": "08bfb08f-48cc-2699-2f5c-aabec43dd43a",
            "SkinLevelID": "9d333ff1-47e2-04c7-2a26-688c08e9164d",
            "ChromaID": "67db243d-4393-f827-50ab-69badca7b162",
            "Attachments": []
        },
        {
            "ID": "29a0cfab-485b-f5d5-779a-b59f85e204a8",
            "SkinID": "24aee897-4cdc-b0fd-e596-1ba90fa6d1b2",
            "SkinLevelID": "51cbccad-487c-50ed-2ffd-c88b4240fab3",
            "ChromaID": "4b2d5b4f-4955-4208-286c-abadec250cdd",
            "Attachments": []
        },
        {
            "ID": "1baa85b4-4c70-1284-64bb-6481dfc3bb4e",
            "SkinID": "1c63b43b-43c4-04e4-01c9-7aa1bffa5ac1",
            "SkinLevelID": "0a7e786c-444e-6a80-8bda-e2b714d68332",
            "ChromaID": "947a28b6-4e0f-61fb-e795-bc9a5e7b7129",
            "Attachments": []
        },
        {
            "ID": "e336c6b8-418d-9340-d77f-7a9e4cfe0702",
            "SkinID": "1ef6ba68-4dbe-30c7-6bc8-93a6c6f13f04",
            "SkinLevelID": "feaf05a1-492f-d154-a9f5-0eb1fe9a603e",
            "ChromaID": "5a59bd61-48a9-af61-c00f-4aa21deca9a8",
            "Attachments": []
        },
        {
            "ID": "42da8ccc-40d5-affc-beec-15aa47b42eda",
            "SkinID": "48ad078a-4dae-2b85-a945-f4b6d1efecbb",
            "SkinLevelID": "a7f92a1c-4465-5ea3-7745-bd876117f4a7",
            "ChromaID": "95608504-4c8b-1408-1612-0f8200421c49",
            "Attachments": []
        },
        {
            "ID": "a03b24d3-4319-996d-0f8c-94bbfba1dfc7",
            "SkinID": "d1f2920f-469a-3431-ad96-96afbd0017f2",
            "SkinLevelID": "88cba358-4f4d-4d0e-69fc-b48f4c65cb2d",
            "ChromaID": "4914f50d-49f9-6424-ca80-9486c45a138d",
            "Attachments": []
        },
        {
            "ID": "4ade7faa-4cf1-8376-95ef-39884480959b",
            "SkinID": "3bf1e8e0-47e8-f27a-6054-929575f41a54",
            "SkinLevelID": "414d888a-41ce-fcf0-e545-c49018ec9cf4",
            "ChromaID": "0f934388-418a-a9e7-42a7-21b27402e46c",
            "Attachments": []
        },
        {
            "ID": "c4883e50-4494-202c-3ec3-6b8a9284f00b",
            "SkinID": "6f48f7ff-40a5-cc9e-1320-bdaa388f5cbf",
            "SkinLevelID": "115ad37d-4126-20e5-35a5-d691aa97a03c",
            "ChromaID": "727bb66d-40e5-49e4-6368-44b95c56e8e0",
            "Attachments": []
        },
        {
            "ID": "462080d1-4035-2937-7c09-27aa2a5c27a7",
            "SkinID": "30b19f29-419b-1adc-3561-40be2b1f7841",
            "SkinLevelID": "bd80c562-4c2d-f00a-156e-9190d023098e",
            "ChromaID": "10da9310-479f-df03-8229-809a69115ff3",
            "Attachments": []
        },
        {
            "ID": "f7e1b454-4ad4-1063-ec0a-159e56b58941",
            "SkinID": "598bb272-4bfd-ae82-0242-6490cc6f721e",
            "SkinLevelID": "84a414f6-4fe4-98ff-8d4e-b5866894c436",
            "ChromaID": "802491b0-4a8b-f3d9-317f-088c5b0dedd6",
            "Attachments": []
        },
        {
            "ID": "2f59173c-4bed-b6c3-2191-dea9b58be9c7",
            "SkinID": "12cc9ed2-4430-d2fe-3064-f7a19b1ba7c7",
            "SkinLevelID": "854938f3-4532-b300-d9a2-379d987d7469",
            "ChromaID": "cac83e5c-47a1-3519-5420-1db1fdbc4892",
            "Attachments": []
        }
    ],
    "Sprays": [
        {
            "EquipSlotID": "04af080a-4071-487b-61c0-5b9c0cfaac74",
            "SprayID": "6983ae7c-4cb5-835c-8f62-b7affbaae20e",
            "SprayLevelID": null
        },
        {
            "EquipSlotID": "5863985e-43ac-b05d-cb2d-139e72970014",
            "SprayID": "da814168-4ab3-98fb-847a-29967fa91c42",
            "SprayLevelID": null
        },
        {
            "EquipSlotID": "0814b2fe-4512-60a4-5288-1fbdcec6ca48",
            "SprayID": "6983ae7c-4cb5-835c-8f62-b7affbaae20e",
            "SprayLevelID": null
        }
    ],
    "PlayerCard": {
        "ID": "e9dcc215-4b83-90e4-ba3b-4f8d32568eb6"
    },
    "PlayerTitle": {
        "ID": "e3ca05a4-4e44-9afe-3791-7d96ca8f71fa"
    }
}
```
