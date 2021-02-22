# Valorant Store Entitlements
Get Entitlement for store item.
//Note: You can use [The Id list](https://github.com/RumbleMike/ValorantAPI/blob/v2Development/docsv2/content/ValorantID.md) to correlate which item belongs to which.
## Example
 - cURL: `https://pd.na.a.pvp.net/store/v1/entitlements/playerId/itemTypeId`
 - Method: `GET`
 - Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`
    - X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
    - X-Riot-ClientVersion: `versionNumber`
```http
  GET https://pd.na.a.pvp.net/store/v1/entitlements/playerId/itemTypeId
  Content-Type: application/json
  Authorization: Bearer riot_auth_token
  X-Riot-Entitlements-JWT: riot_entitlement_token
  X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
  X-Riot-ClientVersion: `release-02.01-shipping-6-511946`
  {"ItemTypeID":"dd3bf334-87f3-40bd-b043-682a57a8dc3a","Entitlements":[{"ItemID":"4b5417ed-49de-7076-e0fb-12a5b43957ce","InstanceID":"a95b9f3b-4e7b-4b24-8fba-d9fad9d4da34"},{"ItemID":"4b5417ed-49de-7076-e0fb-12a5b43957ce","InstanceID":"48d11985-3735-4e12-bdce-36e5a15ac97b"}]}

  ```
