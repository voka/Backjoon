# import
import gistyc

# Initiate the GISTyc class with the auth token
AUTH_TOKEN = "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"
gist_api = gistyc.GISTyc(auth_token=AUTH_TOKEN)

# Get a list of GISTs
gist_list = gist_api.get_gists()
print(gist_list)