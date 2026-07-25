from shield import Shield

shield = Shield(
    device_id,
    main_hmac,
)

headers = {
    ...
}


print(
    shield.get_shield(
        url,
        headers,
        data
    )
)
