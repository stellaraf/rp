"""Old test code."""

# import json
# import httpx
# from rp.config import params


# def headers():
#     return {"Authorization": f"Token {params.netbox.api_key.get_secret_value()}"}


# def carriers_by_site(site):
#     uri = str(params.netbox.url) + "/circuits/providers"
#     response = httpx.get(uri, headers=headers(), params={"site": site})
#     results = response.json().get("results", [])
#     carriers = []
#     for carrier in results:
#         copied = {
#             "netbox_id": carrier["id"],
#             "name": carrier["name"],
#             "asn": carrier["asn"],
#             "carrier_id": carrier["custom_fields"].get("carrier_id", None),
#         }
#         carriers.append(copied)
#     return carriers


# def devices_by_filter(filter):
#     uri = str(params.netbox.url) + "/dcim/devices"
#     response = httpx.get(uri, headers=headers(), params=filter)
#     results = response.json().get("results", [])
#     devices = []
#     for device in results:
#         if device.get("site") is not None and device["site"]["name"] in params.sites:
#             copied = {
#                 "netbox_id": device["id"],
#                 "name": device["name"],
#                 "router_id": device["custom_fields"].get("edge_router_id"),
#                 "router_number": device["custom_fields"].get("pop_router_number"),
#             }
#             devices.append(copied)
#     return devices


# if __name__ == "__main__":
#     print(json.dumps(devices_by_filter({"role": "edgerouter"}), indent=2))
