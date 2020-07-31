# Username From ID
Get Username From ID.

## Template
Here is how to use `cURL` to get User's Username from ID:
- URL: `https://pd.NA.a.pvp.net/name-service/v2/players`
- Method: `PUT`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`

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

- Body
[
	"47361c6e-aac0-5206-8617-8019f7502fa3"
]


[{"DisplayName":"voare","Subject":"47361c6e-aac0-5206-8617-8019f7502fa3","GameName":"voare","TagLine":"NA1"}]

```
