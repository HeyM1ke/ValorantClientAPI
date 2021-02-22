# Player Store
Get Player's store, Including Items, Prices and Featured Bundles.

## Template
Here is how to use `cURL` to get User's Store:
- URL: `https://pd.na.a.pvp.net/store/v2/storefront/` `PLAYER ID`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`
    - X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
    - X-Riot-ClientVersion: `versionNumber`
## Example
```http
GET https://pd.na.a.pvp.net/store/v2/storefront/PLAYERID
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token
X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
X-Riot-ClientVersion: `release-02.01-shipping-6-511946`

{
    "FeaturedTheme": {
        "ID": "3b90886a-5834-4e47-820e-77429fd768d8",
        "DataAssetID": "fd9fd08f-446f-018f-c632-0e96428f2978",
        "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
        "Items": [
            {
                "Item": {
                    "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                    "ItemID": "ed8a1109-4e48-f077-636b-e98dd332bfcc",
                    "Amount": 1
                },
                "BasePrice": 1775,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 0,
                "IsPromoItem": false
            },
            {
                "Item": {
                    "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                    "ItemID": "90fe45d6-41ea-1c49-8fb9-46b0e98c0077",
                    "Amount": 1
                },
                "BasePrice": 3550,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 1,
                "IsPromoItem": false
            },
            {
                "Item": {
                    "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                    "ItemID": "9bc535dd-4d91-3421-2cd0-7a8fdad3478b",
                    "Amount": 1
                },
                "BasePrice": 1775,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 0,
                "IsPromoItem": false
            },
            {
                "Item": {
                    "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                    "ItemID": "c5dd6298-4928-5d64-5cd0-7fa41ea89d81",
                    "Amount": 1
                },
                "BasePrice": 1775,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 0,
                "IsPromoItem": false
            },
            {
                "Item": {
                    "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                    "ItemID": "d54e0883-4967-5808-e25c-37b3e6313e5c",
                    "Amount": 1
                },
                "BasePrice": 325,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 1,
                "IsPromoItem": false
            },
            {
                "Item": {
                    "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                    "ItemID": "8f8f82f4-4133-82c9-50b2-3c9c67e0f9fb",
                    "Amount": 1
                },
                "BasePrice": 1775,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 0,
                "IsPromoItem": false
            },
            {
                "Item": {
                    "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                    "ItemID": "547c3aa6-4e86-199c-b190-01b75287f30b",
                    "Amount": 2
                },
                "BasePrice": 475,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 1,
                "IsPromoItem": false
            },
            {
                "Item": {
                    "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                    "ItemID": "52d88add-4269-97c1-fde3-36bcac1a436a",
                    "Amount": 1
                },
                "BasePrice": 375,
                "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                "DiscountPercent": 1,
                "IsPromoItem": false
            }
        ]
    },
    "FeaturedBundle": {
        "Bundle": {
            "ID": "3b90886a-5834-4e47-820e-77429fd768d8",
            "DataAssetID": "fd9fd08f-446f-018f-c632-0e96428f2978",
            "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
            "Items": [
                {
                    "Item": {
                        "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                        "ItemID": "ed8a1109-4e48-f077-636b-e98dd332bfcc",
                        "Amount": 1
                    },
                    "BasePrice": 1775,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 0,
                    "IsPromoItem": false
                },
                {
                    "Item": {
                        "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                        "ItemID": "90fe45d6-41ea-1c49-8fb9-46b0e98c0077",
                        "Amount": 1
                    },
                    "BasePrice": 3550,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 1,
                    "IsPromoItem": false
                },
                {
                    "Item": {
                        "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                        "ItemID": "9bc535dd-4d91-3421-2cd0-7a8fdad3478b",
                        "Amount": 1
                    },
                    "BasePrice": 1775,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 0,
                    "IsPromoItem": false
                },
                {
                    "Item": {
                        "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                        "ItemID": "c5dd6298-4928-5d64-5cd0-7fa41ea89d81",
                        "Amount": 1
                    },
                    "BasePrice": 1775,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 0,
                    "IsPromoItem": false
                },
                {
                    "Item": {
                        "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                        "ItemID": "d54e0883-4967-5808-e25c-37b3e6313e5c",
                        "Amount": 1
                    },
                    "BasePrice": 325,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 1,
                    "IsPromoItem": false
                },
                {
                    "Item": {
                        "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                        "ItemID": "8f8f82f4-4133-82c9-50b2-3c9c67e0f9fb",
                        "Amount": 1
                    },
                    "BasePrice": 1775,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 0,
                    "IsPromoItem": false
                },
                {
                    "Item": {
                        "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                        "ItemID": "547c3aa6-4e86-199c-b190-01b75287f30b",
                        "Amount": 2
                    },
                    "BasePrice": 475,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 1,
                    "IsPromoItem": false
                },
                {
                    "Item": {
                        "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                        "ItemID": "52d88add-4269-97c1-fde3-36bcac1a436a",
                        "Amount": 1
                    },
                    "BasePrice": 375,
                    "CurrencyID": "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741",
                    "DiscountPercent": 1,
                    "IsPromoItem": false
                }
            ]
        },
        "BundleRemainingDurationInSeconds": 424932
    },
    "SkinsPanelLayout": {
        "SingleItemOffers": [
            "8e032580-414f-7ab4-7efb-f6ac7d2bc2f1",
            "9ff1a0e6-4f74-0e6d-9117-de8683db4eb5",
            "c7695ce7-4fc9-1c79-64b3-8c8f9e21571c",
            "e57317ac-4a93-50a9-30e9-93a098513fa9"
        ],
        "SingleItemOffersRemainingDurationInSeconds": 3732
    }
}
```
