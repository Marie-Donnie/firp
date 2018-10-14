# firp (FIches RolePlay)

This is the code for the site I created for my roleplay guild on World of Warcraft (Eu-Kirin Tor server).

It is built around character sheets for our characters, but there are other "modules" like the display of the spells we are using (based on warcraft rpg) or the display of campaign reports.

___

You can see the resulting site here:
https://www.filsdegarithos.ovh/

![Result1](Screenshot_2017-11-10_18-29-13.png "Result1")


The forum is a simple phpbb.

## How to test locally
Clone this repository, install the dependencies and run the Django server.

You probably want to use a virtualenv to install the dependencies:

```sh
git clone https://github.com/Marie-Donnie/firp.git
cd firp
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then you'll want the JS dependencies:

```sh
cd fiches/static
bower install
```

To initialize the SQLite DB, do:

```sh
python manage.py makemigrations
python manage.py migrate
```

Finally, to run the server:

```sh
python manage.py runserver
```

## How to deploy
Copy the `firp/settings_local.py.sample` to `firp/settings_local.py` and edit
it.  Any deployment-specific configuration should go into this file, as the
`settings.py` file is used for development.

## Images credits

Most images belong to Blizzard, since this is a fansite.
