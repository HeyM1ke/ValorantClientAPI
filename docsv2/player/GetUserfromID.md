# Username From ID
Get Username From ID.

## Template
Here is how to use `cURL` to get User's Username from ID:
- URL: `https://pd.NA.a.pvp.net/name-service/v2/players`
- Method: `PUT`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`
    - X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
    - X-Riot-ClientVersion: `versionNumber`
- Body
```
[
	"`PLAYERID`"
]
```

## Example
```http
PUT https://pd.NA.a.pvp.net/name-service/v2/players
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token
X-Riot-ClientPlatform: `ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9`
X-Riot-ClientVersion: `release-02.01-shipping-6-511946`
- Body
[
	"47361c6e-aac0-5206-8617-8019f7502fa3"
]


[{"DisplayName":"voare","Subject":"47361c6e-aac0-5206-8617-8019f7502fa3","GameName":"voare","TagLine":"NA1"}]

```
