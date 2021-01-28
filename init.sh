#! /bin/sh

file=db.sqlite3
if [ -e "$file" ]; then
  # Control will enter here if $file exists
  rm $file
fi

# User credentials

email=admin@docker.com
password=TestDoeCI

python3 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$email', '$password')" | python3 manage.py shell
