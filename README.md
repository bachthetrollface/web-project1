# Clothing Shop Website - Project I

# Installation
1. **Clone the repository**

```
git clone https://github.com/bachthetrollface/web-project1.git
```

Then, move to the directory of the repo for next steps:

```
cd web-project1
```

2. **Install requirements**

Make sure you have Python 3.12 or newer to run the website. Then, run the following script to install required libraries:

```
pip install -r requirements.txt
```

Alternatively, you can check out `requirements.txt` and manually install libraries if needed.

# Run the website

From the directory of the repository, run the following:

```
cd xlgshop
python3 manage.py runserver
```

You may need to use `python` instead of `python3`, depending on your system.

Once the above script executes successfully, the local server will be launched. Open the following link in your web browser to view the website:

```
localhost:8000/
```
or
```
127.0.0.1:8000/
```

To close the server, press `control + C` (for MacOS) or `control + break` (for Windows) while on the terminal window. The key combination may vary depending on your OS, and is provided on the terminal when you launch the server.

# Admin mode

You can open the admin site to view the database in a user-friendly GUI. Open the following link:

```
localhost:8000/admin/
```
or
```
127.0.0.1:8000/admin/
```

Then, log in using the following credentials:
- Username: `admin`
- Password: `notacommonpassword1`
