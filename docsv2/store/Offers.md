# Valorant Offer IDs
Recieve a List of all of Valorant's Store IDs for the game.
//Note: You can use [The Id list](https://github.com/RumbleMike/ValorantAPI/blob/v2Development/docsv2/content/ValorantID.md) to correlate which item belongs to which.
## Example
 - cURL: `https://pd.na.a.pvp.net/store/v1/offers/`
 - Method: `GET`
 - Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`

```http
  GET https://pd.na.a.pvp.net/store/v1/offers/
  Content-Type: application/json
  Authorization: Bearer riot_auth_token
  X-Riot-Entitlements-JWT: riot_entitlement_token

  {
      "Offers": [
          {
              "OfferID": "22c0aaa3-4919-5a7b-90c0-2dacafdc32fe",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867631361Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "22c0aaa3-4919-5a7b-90c0-2dacafdc32fe",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4845a7ab-4120-ae1c-aec1-9e915a7424b1",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867632104Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4845a7ab-4120-ae1c-aec1-9e915a7424b1",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d39a4263-49d3-f2e0-2c13-c299f8644518",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867632269Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "d39a4263-49d3-f2e0-2c13-c299f8644518",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d93ad22d-4db7-b6bc-5e9c-e5959bb9dd76",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867632419Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "d93ad22d-4db7-b6bc-5e9c-e5959bb9dd76",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "bf6df430-4e46-5c51-df6f-c2bc3b1cb4fe",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867632572Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "bf6df430-4e46-5c51-df6f-c2bc3b1cb4fe",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c59442a5-4b74-792c-d996-71a5fb340625",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867632723Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "c59442a5-4b74-792c-d996-71a5fb340625",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d8c9fee3-4e02-bc92-a235-608a556905ae",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867632872Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "d8c9fee3-4e02-bc92-a235-608a556905ae",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c00e786e-4e6f-0ef7-0ce3-32ba9918ba41",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867633035Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "c00e786e-4e6f-0ef7-0ce3-32ba9918ba41",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "fed9c3f3-40a5-da67-4ac9-4683cc5a0eba",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867633189Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "fed9c3f3-40a5-da67-4ac9-4683cc5a0eba",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "7bfab387-4e97-d815-4488-c491e3a5520c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867633336Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "7bfab387-4e97-d815-4488-c491e3a5520c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "df37b069-48b2-0a7c-78ea-5b8eedc684f7",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867633486Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "df37b069-48b2-0a7c-78ea-5b8eedc684f7",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "249b0e46-4a11-f045-51bb-649151cd802a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867633634Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "249b0e46-4a11-f045-51bb-649151cd802a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "e2c84381-4fa6-29b4-37b9-21bba8ae24bf",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867633781Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "e2c84381-4fa6-29b4-37b9-21bba8ae24bf",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "444464f1-445f-8f75-3c8d-a7bd8f24e654",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867633926Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "444464f1-445f-8f75-3c8d-a7bd8f24e654",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "94cf6dd4-42c5-f70e-1652-dca05fa42ad6",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867634076Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "94cf6dd4-42c5-f70e-1652-dca05fa42ad6",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "e57317ac-4a93-50a9-30e9-93a098513fa9",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867634222Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1750
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "e57317ac-4a93-50a9-30e9-93a098513fa9",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4aa31563-44e1-0d9f-f95a-a1b9965ad762",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763437Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4aa31563-44e1-0d9f-f95a-a1b9965ad762",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "3b955119-421c-3319-50cc-1aaf06b42338",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867634516Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "3b955119-421c-3319-50cc-1aaf06b42338",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "7a0374af-42f5-2f99-b535-a997f2179717",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867634663Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "7a0374af-42f5-2f99-b535-a997f2179717",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "fbe265cf-4e3d-9891-791e-5089f1f7f102",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763481Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "fbe265cf-4e3d-9891-791e-5089f1f7f102",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "df3adf8c-4fa3-5f57-544d-eabf8b68713d",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867634958Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "df3adf8c-4fa3-5f57-544d-eabf8b68713d",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "ea65ba94-468d-39a8-5ded-98820d72d19f",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867635104Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "ea65ba94-468d-39a8-5ded-98820d72d19f",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f35f6e13-4b7b-da38-c0de-5c91fffd584b",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763525Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "f35f6e13-4b7b-da38-c0de-5c91fffd584b",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "547c3aa6-4e86-199c-b190-01b75287f30b",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867635396Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "547c3aa6-4e86-199c-b190-01b75287f30b",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "8edf22c5-4489-ab41-769a-07adb4c454d6",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867635542Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "8edf22c5-4489-ab41-769a-07adb4c454d6",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4538bff7-470c-889c-9875-7ba3ebf87c87",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763569Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4538bff7-470c-889c-9875-7ba3ebf87c87",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "21ceb4b1-480f-dddb-1422-8aad73519181",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867635836Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "21ceb4b1-480f-dddb-1422-8aad73519181",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d6e93360-46a2-0103-afa0-8b91e78b6fe8",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867635989Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "d6e93360-46a2-0103-afa0-8b91e78b6fe8",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "1878bbc9-409e-66b4-346b-c3997a54df57",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867636137Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "1878bbc9-409e-66b4-346b-c3997a54df57",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "8e032580-414f-7ab4-7efb-f6ac7d2bc2f1",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867636283Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "8e032580-414f-7ab4-7efb-f6ac7d2bc2f1",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "0ff7ff25-42cf-769a-4e6d-bd833121302d",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867636428Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "0ff7ff25-42cf-769a-4e6d-bd833121302d",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "33d3c906-4305-19cf-8770-1eb5207482cc",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867636574Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "33d3c906-4305-19cf-8770-1eb5207482cc",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "50265ad5-4f14-2b32-924e-02bbed2bea6f",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867636724Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "50265ad5-4f14-2b32-924e-02bbed2bea6f",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "5ff3a862-4e89-84dd-6e47-bda2cd2a5cec",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867636872Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "5ff3a862-4e89-84dd-6e47-bda2cd2a5cec",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4049dc82-495b-cecc-8e34-4dbf35753129",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763702Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4049dc82-495b-cecc-8e34-4dbf35753129",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "65ed014b-4279-8ba5-01d3-f48d4e7f115c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867637185Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "65ed014b-4279-8ba5-01d3-f48d4e7f115c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "ea441610-42da-e46f-8d7b-1b9759c105cd",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763733Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 4350
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "ea441610-42da-e46f-8d7b-1b9759c105cd",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "ca2f7bc0-4270-7f76-4623-8596a5584d06",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763748Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "ca2f7bc0-4270-7f76-4623-8596a5584d06",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "cdc130c2-4b12-3702-c8f6-5a8920746395",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867637628Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "cdc130c2-4b12-3702-c8f6-5a8920746395",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "6e3d1cd3-4494-8b21-cbc7-0797e8de75db",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867637776Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "6e3d1cd3-4494-8b21-cbc7-0797e8de75db",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "549b06bb-4704-25ce-19d5-c9b70b10de19",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867637929Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "549b06bb-4704-25ce-19d5-c9b70b10de19",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "52d88add-4269-97c1-fde3-36bcac1a436a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867638076Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "52d88add-4269-97c1-fde3-36bcac1a436a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f38b2545-4498-48b3-150e-1589e25e7aa7",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867638223Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "f38b2545-4498-48b3-150e-1589e25e7aa7",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "7cf3af0b-4556-a0db-2e04-eea4368b354b",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763837Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "7cf3af0b-4556-a0db-2e04-eea4368b354b",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "88d7c503-477f-c881-af2c-53bbab55807c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867638519Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "88d7c503-477f-c881-af2c-53bbab55807c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d3759a6a-4d5c-a322-092f-7290b52566ef",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867638666Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "d3759a6a-4d5c-a322-092f-7290b52566ef",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "d1d528ae-4dcc-e693-68e2-e8a475df83a4",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867638818Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "d1d528ae-4dcc-e693-68e2-e8a475df83a4",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "04dbf8e5-44fc-73f7-0655-8ca05a47739c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867638968Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "04dbf8e5-44fc-73f7-0655-8ca05a47739c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "8a1b2c5b-4692-78ae-9d5c-cdac6a61e4f4",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763912Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "8a1b2c5b-4692-78ae-9d5c-cdac6a61e4f4",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "ed95e342-4116-f07c-88b9-368a5fadb224",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86763927Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "ed95e342-4116-f07c-88b9-368a5fadb224",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "03e03718-4c65-8a47-fb8b-78ba233cecd1",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867639422Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "03e03718-4c65-8a47-fb8b-78ba233cecd1",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "7d3c0ac4-42ce-7111-2c86-43be3d2e86a7",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867639568Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "7d3c0ac4-42ce-7111-2c86-43be3d2e86a7",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4a5ad8cd-4684-a47c-b393-ce9c6760d21a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867639716Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4a5ad8cd-4684-a47c-b393-ce9c6760d21a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "cfeb4b7a-4310-796c-db4e-fb9844823992",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867639865Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "cfeb4b7a-4310-796c-db4e-fb9844823992",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "9bc535dd-4d91-3421-2cd0-7a8fdad3478b",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867640018Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "9bc535dd-4d91-3421-2cd0-7a8fdad3478b",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "ec3745c4-432a-8173-8150-cfbb4841c121",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867640167Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "ec3745c4-432a-8173-8150-cfbb4841c121",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "1d0fe8d7-42dd-6f77-50b0-798d1ff90bef",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867640316Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "1d0fe8d7-42dd-6f77-50b0-798d1ff90bef",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "84f8d0f4-4442-5892-6a20-8f83e65a5e96",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867640464Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "84f8d0f4-4442-5892-6a20-8f83e65a5e96",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4276d2b5-4b1c-b636-aff0-4ea579d875d7",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867640611Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4276d2b5-4b1c-b636-aff0-4ea579d875d7",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d7a02a43-47a5-556c-a69f-ec9cf6ede66d",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86764076Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "d7a02a43-47a5-556c-a69f-ec9cf6ede66d",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "9336ab9d-445c-0872-a283-9f9b61a0098a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867640909Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "9336ab9d-445c-0872-a283-9f9b61a0098a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "6d4766d0-41f0-8493-93eb-a4902a0c6034",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867641059Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "6d4766d0-41f0-8493-93eb-a4902a0c6034",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d59590fa-4389-125a-6c53-c7bd026acb01",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867641204Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "d59590fa-4389-125a-6c53-c7bd026acb01",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "7d43477d-465a-67fc-561e-f2a2ebea697d",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86764135Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "7d43477d-465a-67fc-561e-f2a2ebea697d",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "68564c51-4f7e-67d1-fd0d-4e9d216356e8",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.8676415Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "68564c51-4f7e-67d1-fd0d-4e9d216356e8",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "353c1e5f-4258-c49a-c0d6-319ad33bffea",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867641647Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "353c1e5f-4258-c49a-c0d6-319ad33bffea",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "5bf17117-4ead-a0a8-2961-288d38985e93",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867641794Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "5bf17117-4ead-a0a8-2961-288d38985e93",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "5a773352-456e-ef0b-35ab-c99ead159264",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867641941Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "5a773352-456e-ef0b-35ab-c99ead159264",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c7695ce7-4fc9-1c79-64b3-8c8f9e21571c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86764209Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "c7695ce7-4fc9-1c79-64b3-8c8f9e21571c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "8f8f82f4-4133-82c9-50b2-3c9c67e0f9fb",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86764224Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "8f8f82f4-4133-82c9-50b2-3c9c67e0f9fb",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "481a5abb-45d7-818d-798f-d18d988b6dc1",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867642392Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "481a5abb-45d7-818d-798f-d18d988b6dc1",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "b3d3ff38-4202-20d8-2f41-c783477e5636",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867642541Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "b3d3ff38-4202-20d8-2f41-c783477e5636",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "5546f723-4056-6700-80b8-f1b8d42e4952",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867642687Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "5546f723-4056-6700-80b8-f1b8d42e4952",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "369c7cda-4133-b3ab-2c8b-3e8f371cb181",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867642835Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "369c7cda-4133-b3ab-2c8b-3e8f371cb181",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "880d5de5-4268-769d-5407-55921ad2db12",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867642983Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "880d5de5-4268-769d-5407-55921ad2db12",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "ba42fe63-457a-78ce-4499-47950a698129",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867643148Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "ba42fe63-457a-78ce-4499-47950a698129",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "29be6d9e-48b2-1229-4f7d-4da1c20deda9",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867643295Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "29be6d9e-48b2-1229-4f7d-4da1c20deda9",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "48ce4a70-4207-623b-4739-bfb937812432",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867643439Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 4350
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "48ce4a70-4207-623b-4739-bfb937812432",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "2e37f837-425d-45f2-22a2-71a9af5c118f",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867643583Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "2e37f837-425d-45f2-22a2-71a9af5c118f",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "73e91435-4a2a-2552-d541-eb961e168f2c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867643732Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "73e91435-4a2a-2552-d541-eb961e168f2c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "1b300b91-41bb-d468-f65f-f68ec0861bd6",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867643879Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "1b300b91-41bb-d468-f65f-f68ec0861bd6",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "e5a2e04a-4805-1244-5376-06b40d7c6cbb",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867644033Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "e5a2e04a-4805-1244-5376-06b40d7c6cbb",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c9678d8c-4327-f397-b0ec-dca3c3d6fb15",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867644181Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "c9678d8c-4327-f397-b0ec-dca3c3d6fb15",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "9fbe39c6-42d7-b1db-9048-f0951ce2ff94",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86764433Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "9fbe39c6-42d7-b1db-9048-f0951ce2ff94",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "fbfc273b-4c12-961a-a4fb-978b43be81a9",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867644479Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "fbfc273b-4c12-961a-a4fb-978b43be81a9",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "37851a69-4719-d8ae-d305-49bcee8d853c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867644627Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "37851a69-4719-d8ae-d305-49bcee8d853c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "a2950772-447a-f2db-be24-19b0e0ed736f",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867644775Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "a2950772-447a-f2db-be24-19b0e0ed736f",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "66f68f67-4f5e-8188-8ba8-b183e25e93e7",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867644926Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "66f68f67-4f5e-8188-8ba8-b183e25e93e7",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c5dd6298-4928-5d64-5cd0-7fa41ea89d81",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867645075Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "c5dd6298-4928-5d64-5cd0-7fa41ea89d81",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "a83ac09d-4c19-fda6-8e4d-c1b77dc2b479",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867645223Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "a83ac09d-4c19-fda6-8e4d-c1b77dc2b479",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "b8bc5d1b-44aa-aa83-0246-b1a6bb496177",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86764537Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "b8bc5d1b-44aa-aa83-0246-b1a6bb496177",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "0abecac7-411f-71c0-9504-2d81df0acd71",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867645517Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "0abecac7-411f-71c0-9504-2d81df0acd71",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "80bbcdff-4b2c-2370-0806-498c0f4e1d06",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867645667Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "80bbcdff-4b2c-2370-0806-498c0f4e1d06",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "9a657204-4376-ed61-ad3e-0a8b7bbecd18",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867645815Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "9a657204-4376-ed61-ad3e-0a8b7bbecd18",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4c053776-467f-2c6a-b609-0ba3ea371a14",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867645963Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4c053776-467f-2c6a-b609-0ba3ea371a14",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c8652efa-462f-d455-20b0-699dd00a9e2a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867646109Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "c8652efa-462f-d455-20b0-699dd00a9e2a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "40308b30-4689-9713-52fb-6f8a3534213f",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867646258Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "40308b30-4689-9713-52fb-6f8a3534213f",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "5c273d0e-47fa-bb8c-d914-728de95da30e",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867646405Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "5c273d0e-47fa-bb8c-d914-728de95da30e",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "2484e328-45e9-a5c0-960f-ad8b0f620d0e",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867646553Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "2484e328-45e9-a5c0-960f-ad8b0f620d0e",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "fa3d6a11-46c4-2caf-f7e4-10a5013c034b",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867646699Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "fa3d6a11-46c4-2caf-f7e4-10a5013c034b",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "a2045403-40f7-2926-f955-028b6867c79a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867646845Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "a2045403-40f7-2926-f955-028b6867c79a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "df639108-4e9d-7fc1-51da-4dbb810ba011",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867646993Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "df639108-4e9d-7fc1-51da-4dbb810ba011",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "90fe45d6-41ea-1c49-8fb9-46b0e98c0077",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867647143Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "90fe45d6-41ea-1c49-8fb9-46b0e98c0077",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "9ff1a0e6-4f74-0e6d-9117-de8683db4eb5",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867647291Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "9ff1a0e6-4f74-0e6d-9117-de8683db4eb5",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c2f90c55-49be-93a5-daf4-6393d9d3f6fc",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867647437Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "c2f90c55-49be-93a5-daf4-6393d9d3f6fc",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "0d73596b-478a-dae0-49ca-2fa588f78f13",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867647588Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "0d73596b-478a-dae0-49ca-2fa588f78f13",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4e4ebb8d-41d0-c326-595a-1f9b257e91fa",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867647731Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4e4ebb8d-41d0-c326-595a-1f9b257e91fa",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f9fab42c-46bf-1bf0-dba5-32988be03fc2",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867647879Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "f9fab42c-46bf-1bf0-dba5-32988be03fc2",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "ed333b00-4e88-a9c5-d309-acae85438e93",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867648029Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "ed333b00-4e88-a9c5-d309-acae85438e93",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "a88a4c80-4913-a111-0fba-878adddd381a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867648174Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "a88a4c80-4913-a111-0fba-878adddd381a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "3e32c58e-4347-e4b1-4502-6dab0dc516a8",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867648321Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "3e32c58e-4347-e4b1-4502-6dab0dc516a8",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "3710f62c-4e0c-65fd-848d-8da25d2fb833",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867648469Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "3710f62c-4e0c-65fd-848d-8da25d2fb833",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "5a0cd3b5-4249-bf6f-d009-17a81532660e",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867648618Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "5a0cd3b5-4249-bf6f-d009-17a81532660e",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4b74b3ee-4a63-7339-a28f-8b8be010ca5a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867648765Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4b74b3ee-4a63-7339-a28f-8b8be010ca5a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "e34039b6-441d-3e17-2773-bdaf5c3d2faa",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867648911Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 3550
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "e34039b6-441d-3e17-2773-bdaf5c3d2faa",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "3bf9d39f-46b4-ba23-e079-488d799b9416",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867649058Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "3bf9d39f-46b4-ba23-e079-488d799b9416",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "8bbdc250-4ffc-f6ba-61a0-0d84c4756a4e",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867649203Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "8bbdc250-4ffc-f6ba-61a0-0d84c4756a4e",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "aeca98db-4737-5e0f-3476-7eb8a16eb696",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867649351Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 375
              },
              "Rewards": [
                  {
                      "ItemTypeID": "3f296c07-64c3-494c-923b-fe692a4fa1bd",
                      "ItemID": "aeca98db-4737-5e0f-3476-7eb8a16eb696",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f4bfff96-487a-cf9e-08cc-d590d962c4e6",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867649499Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "f4bfff96-487a-cf9e-08cc-d590d962c4e6",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f3594bcc-43a9-4a74-8c40-98a4e4a4569a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867649647Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 4950
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "f3594bcc-43a9-4a74-8c40-98a4e4a4569a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "fee2c305-40d1-1cca-08b8-46bceda98eca",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867649797Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "fee2c305-40d1-1cca-08b8-46bceda98eca",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "d54e0883-4967-5808-e25c-37b3e6313e5c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867649943Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "d54e0883-4967-5808-e25c-37b3e6313e5c",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "b2128a8c-49bd-09b1-7b4c-f2b9d2f92508",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.86765009Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "b2128a8c-49bd-09b1-7b4c-f2b9d2f92508",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "ed8a1109-4e48-f077-636b-e98dd332bfcc",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867650241Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "ed8a1109-4e48-f077-636b-e98dd332bfcc",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "1658e811-4084-8775-28df-5a9feabc52d8",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867650388Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "1658e811-4084-8775-28df-5a9feabc52d8",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "3aeef60b-48fb-02aa-31b1-068aeb351213",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867650533Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "3aeef60b-48fb-02aa-31b1-068aeb351213",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "e6eee5ec-4f6f-e764-1c4d-048ce271be27",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867650681Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "e6eee5ec-4f6f-e764-1c4d-048ce271be27",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "735e6c3c-4899-532d-60cf-1ba0ce1a450d",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867650829Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "735e6c3c-4899-532d-60cf-1ba0ce1a450d",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "642ee168-4f9e-1f5f-be72-01b3a41ac086",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867650976Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "642ee168-4f9e-1f5f-be72-01b3a41ac086",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "4a3b4aaf-4cdd-d5cf-b776-0593c3d2bf9a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867651122Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "4a3b4aaf-4cdd-d5cf-b776-0593c3d2bf9a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "eb35e4e1-4138-9ece-08e2-69bd414cf598",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867651288Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "eb35e4e1-4138-9ece-08e2-69bd414cf598",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "19b20b51-472b-e837-e5da-f8a348110dbf",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867651437Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "19b20b51-472b-e837-e5da-f8a348110dbf",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f00520c8-4b70-7255-d23c-c0a4887656a2",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867651585Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "f00520c8-4b70-7255-d23c-c0a4887656a2",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "1b94d997-4db6-014f-4cb8-c1b4df7d7ebc",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867651732Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "1b94d997-4db6-014f-4cb8-c1b4df7d7ebc",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "0221e96d-49be-a601-52d6-ef8270773276",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867651878Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "0221e96d-49be-a601-52d6-ef8270773276",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f2ef87c7-4ff5-54f8-e038-cea4e54eefdd",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867652033Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "f2ef87c7-4ff5-54f8-e038-cea4e54eefdd",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "a6d41f01-4b8b-444d-b9da-3eaaf3d7e262",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867652185Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "a6d41f01-4b8b-444d-b9da-3eaaf3d7e262",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "712c7a37-4524-0b27-dfdd-4e95181dd36e",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867652332Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2175
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "712c7a37-4524-0b27-dfdd-4e95181dd36e",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "c9f0ea7f-4bed-b10e-62d2-0394444feed1",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867652479Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "c9f0ea7f-4bed-b10e-62d2-0394444feed1",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "b6768f01-4d72-f0f1-65b5-71b751536490",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867652625Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1750
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "b6768f01-4d72-f0f1-65b5-71b751536490",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "bad7ae62-4f6a-8974-ab73-7ba6405ca898",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867652774Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "bad7ae62-4f6a-8974-ab73-7ba6405ca898",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "b8bb264c-4578-2410-8dfa-6aacfeb318b0",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867652921Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "b8bb264c-4578-2410-8dfa-6aacfeb318b0",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "3800390c-4192-92d1-1703-33ba231fc226",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867653067Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1275
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "3800390c-4192-92d1-1703-33ba231fc226",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "5dcdc42b-4398-0a62-1351-9b8cfdd2892c",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867653217Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "5dcdc42b-4398-0a62-1351-9b8cfdd2892c",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "71d260ca-4bad-81f2-0298-44860341a7a6",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867653367Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "71d260ca-4bad-81f2-0298-44860341a7a6",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f344bead-bb25-4226-a990-b5d9694d475d",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867653515Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 475
              },
              "Rewards": [
                  {
                      "ItemTypeID": "dd3bf334-87f3-40bd-b043-682a57a8dc3a",
                      "ItemID": "f344bead-bb25-4226-a990-b5d9694d475d",
                      "Quantity": 2
                  }
              ]
          },
          {
              "OfferID": "1091d2cc-430b-56ca-a82b-279b70026193",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867653665Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 325
              },
              "Rewards": [
                  {
                      "ItemTypeID": "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475",
                      "ItemID": "1091d2cc-430b-56ca-a82b-279b70026193",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "2b555f97-46bb-5949-3531-979f5bc817f0",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867653813Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "2b555f97-46bb-5949-3531-979f5bc817f0",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "24c73c29-443c-2440-d6db-838086f2451a",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867653957Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1775
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "24c73c29-443c-2440-d6db-838086f2451a",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "1bfea917-4262-37ba-3a76-04b937f2d0be",
              "IsDirectPurchase": true,
              "StartDate": "2020-11-24T19:56:42.867654106Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 875
              },
              "Rewards": [
                  {
                      "ItemTypeID": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
                      "ItemID": "1bfea917-4262-37ba-3a76-04b937f2d0be",
                      "Quantity": 1
                  }
              ]
          },
          {
              "OfferID": "f9cfa034-c7e1-4995-904c-1a296e7b1760",
              "IsDirectPurchase": true,
              "StartDate": "2020-01-01T00:00:00Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1600
              },
              "Rewards": [
                  {
                      "ItemTypeID": "ea6fcd2e-8373-4137-b1c0-b458947aa86d",
                      "ItemID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                      "Quantity": 20
                  }
              ]
          },
          {
              "OfferID": "da0edbc8-31fb-468e-95a8-27ac25cd76ed",
              "IsDirectPurchase": true,
              "StartDate": "2020-01-01T00:00:00Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 2800
              },
              "Rewards": [
                  {
                      "ItemTypeID": "ea6fcd2e-8373-4137-b1c0-b458947aa86d",
                      "ItemID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                      "Quantity": 40
                  }
              ]
          },
          {
              "OfferID": "a61e8526-bb1f-4135-b7df-95e67b416efe",
              "IsDirectPurchase": true,
              "StartDate": "2020-01-01T00:00:00Z",
              "Cost": {
                  "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 4800
              },
              "Rewards": [
                  {
                      "ItemTypeID": "ea6fcd2e-8373-4137-b1c0-b458947aa86d",
                      "ItemID": "e59aa87c-4cbf-517a-5983-6e81511be9b7",
                      "Quantity": 80
                  }
              ]
          }
      ],
      "UpgradeCurrencyOffers": [
          {
              "OfferID": "f9cfa034-c7e1-4995-904c-1a296e7b1760",
              "StorefrontItemID": "187c8a5e-47de-f4ca-b02b-7697611cff5b"
          },
          {
              "OfferID": "da0edbc8-31fb-468e-95a8-27ac25cd76ed",
              "StorefrontItemID": "9483b151-4f66-298b-fb32-b58224324e67"
          },
          {
              "OfferID": "a61e8526-bb1f-4135-b7df-95e67b416efe",
              "StorefrontItemID": "f86f9999-452b-3d4c-788a-cda895ddf923"
          }
      ]
  }
  ```
