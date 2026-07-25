from shield import Shield

device_id = ""
main_hmac = ""
url       = ""
data      = ""

headers = {}

shield = Shield(
    device_id,
    main_hmac,
)


shield_result = shield.get_shield(url, headers, data)

print(shield)

