Clone this repository to a local directory: 

```code
git clone https://github.com/cherevik/excel2csv.git
```

Change to the project directory and run the following commands.

Mac:

```code
> python3 -m pip install --user --upgrade pip
> python3 -m pip install --user virtualenv
> python3 -m virtualenv venv
> source venv/bin/activate
> pip install -r requirements.txt
```

Windows: 

```code
> py -m pip install --user virtualenv
> py -m virtualenv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt
```

Test your installation by running the following command 

```code
python excel2csv.py files/health_systems.xslx files/health_systems.csv
```
