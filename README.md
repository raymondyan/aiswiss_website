# System Setup

### update APT

```bash
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install build-essential python python-dev tcl
```

### install git

```bash
sudo apt-get install git
```

### install mysql server

```bash
# you need to set the password for root user
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev #mysql_config
```

### create database

```bash
mysql -u root -p
#input your password
mysql> CREATE DATABASE voting;
```

### install redis

```bash
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
sudo cp src/redis-server /usr/local/bin/
sudo cp src/redis-cli /usr/local/bin/
redis-server
```

you need to git clone this repo to your server

### install pip

```bash
sudo apt-get install python-pip
```

### install virtualenv

```bash
pip install virtualenv
```

### build virtualenv

```bash
cd path/to/Voting
virtualenv env
source env/bin/activate
```

### install python package

```bash
pip install -r requirements.txt
```

### do migrate and create superuser

```bash
cd path/toVoting
python manage.py migrate
python manage.py createsuperuser #you need to input username and  password, and please remember that
```

### do staticfiles collect

```bash
python manage.py collectstatic #you need to make confirm on the command, input `yes`
```

### install nginx

```bash
sudo apt-get install nginx # install nginx
sudo /etc/init.d/nginx start    # start nginx
```

Symlink to this file from /etc/nginx/sites-enabled so nginx can see it:

```bash
sudo ln -s ~/path/to/Voting/nginx.conf /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
```

maybe you need to change the user to 'root' in `/etc/nginx/nginx.conf` to make sure all the file can be visited.

uswgi knowledge: http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

Have a good day.