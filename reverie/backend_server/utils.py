from dotenv import load_dotenv
from os import getenv

load_dotenv()
# Set your OPENAI_API_KEY as environment variable
#
# If you are using GitHub Codespace, you can set it as one of your GitHub Secret
# https://docs.github.com/en/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces
openai_api_key = getenv("OPENAI_API_KEY")

# Put your name
key_owner = "<Name>"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose
debug = True
