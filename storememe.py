import os
from db import add_object
from logs import log
from werkzeug.utils import secure_filename

# Directory where memes are stored (inside the project)
BASE_DIR = os.path.dirname(__file__)
MEMES_DIR = os.path.join(BASE_DIR, 'memes')
os.makedirs(MEMES_DIR, exist_ok=True)


def store_meme_image(image_data, image_name, image_category, original_filename=None):
    """Save image_data (bytes) to the project's memes/ directory.

    - image_name: friendly name provided by user (used as 'name' in JSON)
    - original_filename: optional original filename to preserve extension
    Returns a dict with status and stored relative path.
    """
    # sanitize the provided image name for a filename base
    base_name = secure_filename(str(image_name)) or 'meme'

    # keep extension from original filename when available
    ext = ''
    if original_filename:
        _, ext = os.path.splitext(original_filename)

    if not ext:
        # default to .jpg when extension cannot be determined
        ext = '.jpg'

    filename = f"{base_name}{ext}"
    file_path = os.path.join(MEMES_DIR, filename)

    # write bytes to file
    with open(file_path, 'wb') as f:
        f.write(image_data)

    # store a project-relative path (matches existing entries like 'memes/dog.jpg')
    rel_path = os.path.join('memes', filename).replace('\\', '/')

    new_meme = {
        "name": image_name,
        "path": rel_path,
        "category": image_category,
    }
    add_object(new_meme)
    log(f"ISIS : Meme stored - {image_name}", "green")
    return {"status": "success", "message": f"Meme '{image_name}' stored successfully.", "path": rel_path}
