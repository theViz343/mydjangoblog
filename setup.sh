#! /bin/bash
echo "Please wait. This may take several minutes..."
python3 -m venv venv1
source venv1/bin/activate
pip3 install django
pip3 install django-newsletter
pip3 install django-summernote
deactivate