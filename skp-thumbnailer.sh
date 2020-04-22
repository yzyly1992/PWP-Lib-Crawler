 #!/bin/bash
if test -z "$1"; then FOLDER="."; else FOLDER="$1"; fi

find $FOLDER -name '*.skp' | while read fn; do FILE_PATH=$(readlink -f "$fn"); echo "$FILE_PATH"; THUMB_PATH=`python -c "import gnome.ui, gnomevfs, os.path; print gnome.ui.thumbnail_path_for_uri(gnomevfs.get_uri_from_local_path(os.path.abspath('$FILE_PATH')), 'normal')"`; echo "-> $THUMB_PATH"; python "/usr/bin/skp-thumbnailer.py" "$FILE_PATH" "$THUMB_PATH"; done

exit 0
