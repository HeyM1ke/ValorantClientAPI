# Valorant Offer IDs
Recieve a List of all of Valorant's Store IDs for the game.
//Note: You can use [The Id list](https://github.com/RumbleMike/ValorantAPI/blob/v2Development/docsv2/content/ValorantID.md) to correlate which item belongs to which.
## Example
 - cURL: `https://pd.na.a.pvp.net/store/v1/offers/`
 - Method: `GET`
 - Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`
    - X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
    - X-Riot-ClientVersion: `versionNumber`
```http
  GET https://pd.na.a.pvp.net/store/v1/offers/
  Content-Type: application/json
  Authorization: Bearer riot_auth_token
  X-Riot-Entitlements-JWT: riot_entitlement_token
  X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
  X-Riot-ClientVersion: `release-02.01-shipping-6-511946`
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
 }
  ```
