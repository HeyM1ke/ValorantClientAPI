# Player ID
Get Player's ID

## Template
Here is how to use `cURL` to get User's ID:
- URL: `https://pd.na.a.pvp.net/name-service/v1/players`
- Method: `POST`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement`

## Example
```http
POST https://pd.na.a.pvp.net/name-service/v1/players
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token

{
  {"DisplayName":"","Subject":"PLAYER_ID_SHOULD_BE_HERE","GameName":"","TagLine":""}
}
```
