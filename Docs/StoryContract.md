# Story Contract
Get Infomation regarding the Contract.

`cURL` = https://pd.na.a.pvp.net/contract-definitions/v2/definitions/story

## Template
Here is how to use `cURL` to get Info on Story Contract:
- URL: `https://pd.na.a.pvp.net/contract-definitions/v2/definitions/story`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`

## Example
```http
GET https://pd.na.a.pvp.net/contract-definitions/v2/definitions/story
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token

{
    {
    "ID": "7b06d4ce-e09a-48d5-8215-df9901376fa7",
    "Name": "WWL Story Contract",
    "RequiredEntitlement": null,
    "ContractType": "story",
    "ProgressionSchedule": {
        "ID": "42b7f246-093d-4327-9c57-26f01972861d",
        "Name": "WWL Story Contract Progression",
        "ProgressionCurrencyID": "8e755510-5d2b-4921-ad75-bed2de113b18",
        "ProgressionDeltaPerLevel": [
            0,
            4000,
            5000,
            6000,
            7000,
            8000,
            9000,
            10000,
            11000,
            12000,
            13000,
            14000,
            15000,
            16000,
            17000,
            18000,
            19000,
            20000,
            21000,
            22000,
            23000,
            24000,
            25000,
            26000,
            27000,
            28000,
            29000,
            30000,
            31000,
            32000,
            33000,
            34000,
            35000,
            36000,
            37000,
            38000,
            39000,
            40000,
            41000,
            42000,
            43000,
            44000,
            45000,
            46000,
            47000,
            48000,
            49000,
            50000,
            51000,
            52000
        ]
    },
    "AlternateProgressionSchedules": [
        {
            "ID": "e539af1d-87b0-40b8-809d-7169974269eb",
            "Name": "WWL Story Contract Direct Purchase Cost",
            "ProgressionCurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
            "ProgressionDeltaPerLevel": [
                {
                    "IsAvailable": false,
                    "ProgressionDelta": 0
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                },
                {
                    "IsAvailable": true,
                    "ProgressionDelta": 300
                }
            ]
        }
    ],
    "RewardSchedules": [
        {
            "ID": "959d0160-7554-4c6b-9c40-a127b3e13d22",
            "Name": "WWL Contract Free",
            "Prerequisites": null,
            "RewardsPerLevel": [
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "cd5e4a23-4a0b-0f31-d87a-a1a2ec3301f4",
                            "Amount": 1
                        },
                        {
                            "ItemTypeID": "de7caa6b-adf7-4588-bbd1-143831e786c6",
                            "ItemID": "9f0ead27-4925-db1e-626f-ab95d9c45845",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "96502717-41f7-5d24-89a1-66aff04bbbbb",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "de7caa6b-adf7-4588-bbd1-143831e786c6",
                            "ItemID": "631f4283-48b1-1855-d646-5e8f80e29821",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "eece70be-4f84-facb-49b0-fe95290eff67",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "5aaa58d8-4567-dc02-dc74-fbaa957fa7cd",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "77dc86dc-4d9c-df35-3921-d18d32355824",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "de7caa6b-adf7-4588-bbd1-143831e786c6",
                            "ItemID": "00d4d326-4edc-3229-7c28-129d3374e3ad",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "bf2188f1-4b0a-a55f-c631-67a54ac1ccc5",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "7944b081-4b0f-81c8-e41f-3aa5c634b782",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "d1c85a2e-450d-f7e0-6ee3-469295cf1951",
                            "Amount": 1
                        },
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "6ab90b28-49f1-9e1b-5083-2da2de61e109",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                }
            ]
        },
        {
            "ID": "226043e7-9ad7-403f-85af-039fb4c28c62",
            "Name": "WWL Contract Premium",
            "Prerequisites": {
                "RequiredEntitlements": [
                    {
                        "ItemTypeID": "f85cb6f7-33e5-4dc8-b609-ec7212301948",
                        "ItemID": "7b06d4ce-e09a-48d5-8215-df9901376fa7"
                    }
                ]
            },
            "RewardsPerLevel": [
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "4caa7fb0-4751-52f3-6eed-6ab6232be131",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "6f7b0b5b-470d-77b0-bd0d-7781ce5fdf07",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "a40f0146-4420-645d-6d53-73a362900af0",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "bd80c562-4c2d-f00a-156e-9190d023098e",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "25d82d17-4739-e206-e8aa-d1bd4fd4dae6",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "0df7158a-46c6-eeb6-9561-e78165756b99",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "1fb0bee0-49db-fb51-b090-bc834babdb2b",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "49fc11b3-40a9-29ff-a701-63a6f59e2a0f",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "86ca5ef3-4f3f-97e7-0f9c-8aa2e9166a7f",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "32570250-4795-981d-bda7-34963aa042f9",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "e88f43b7-4b9a-1050-c1e7-d883a8f706f2",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "84a414f6-4fe4-98ff-8d4e-b5866894c436",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "9d333ff1-47e2-04c7-2a26-688c08e9164d",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "71e8fdca-4099-af1c-fabf-09a35684e2d0",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "3d1e445f-41c6-71a2-4d60-0790dbe97f64",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "115ad37d-4126-20e5-35a5-d691aa97a03c",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "500da6bd-4cf1-3362-be2b-1487ec286b91",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "f3a3c59b-4bf3-461c-f956-d0bc7d95a742",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "9c65bbe6-41da-c50c-be81-839214eede7c",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "a7229cba-4691-62b0-9c40-f59a29817ddc",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "254e3d77-40b8-cfae-232a-f7a36ee27d61",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "b520005e-42cf-169c-ab30-a7a60d7f29f1",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "a75c951f-4822-f85d-44ed-709e413aa5f8",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "49292f21-4f5e-0a1a-3671-54b7ca8fe65a",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "e6a07a97-4c48-421f-515e-288379f7a5be",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "aa3661f1-4eef-e8dd-047b-e5b9ed61403b",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "36ee876c-4918-69c7-9ce4-9dac0b4b929a",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "9466088a-4ad8-cb08-ec9a-45aaba3a6acd",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "27c5fd11-4f69-031a-6ee0-6da838ed7998",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "8bd42b70-4f2f-5c7d-33d3-0f83521c8eb5",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "c8c31580-4315-967b-998b-dfa377bb8843",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "f8cd4279-4530-db62-1e4e-aa82c129b045",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "086acc73-4c6a-26d4-5da6-a2ade411897c",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "706200b9-40bd-8d93-0442-ff94f6a0fd6e",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "31e2cc61-4d9e-2aa1-ff65-76a7a0a7bba1",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "c9ee9a00-453d-a358-8501-3ebb7ca3765e",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                            "ItemID": "d8cfce74-4bb8-42b2-022e-9dbf9d648823",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                            "ItemID": "175d5ea6-43a6-1e39-e720-62805544f5d3",
                            "Amount": 2
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                            "ItemID": "51dcf475-4078-2dce-883b-48bb77670ea8",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                },
                {
                    "EntitlementRewards": null,
                    "WalletRewards": [
                        {
                            "CurrencyID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                            "Amount": 10
                        }
                    ]
                },
                {
                    "EntitlementRewards": [
                        {
                            "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                            "ItemID": "8c2e0f93-4277-fbb8-20c6-e2b2638b6ed4",
                            "Amount": 1
                        }
                    ],
                    "WalletRewards": null
                }
            ]
        }
    ],
    "PremiumContractDetails": {
        "Entitlement": {
            "ItemTypeID": "f85cb6f7-33e5-4dc8-b609-ec7212301948",
            "ItemID": "7b06d4ce-e09a-48d5-8215-df9901376fa7"
        },
        "PurchaseCurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
        "PurchaseCost": 1000
    }
}
}
```



