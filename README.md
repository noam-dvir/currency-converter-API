# currency-converter-API
Web API for an online currency converter.
The code is written in Python 3.8.1 using Django framework.

Run instructions:

1)Inside cmd, cd to project folder (where manage.py file resides)
2)Start the server by running the following 2 commands:
pipenv shell
python manage.py runserver

Once executed, a printing output will say:
"Starting development server at http://127.0.0.1:8000/" (might be a different IP)
3)Copy the url (e.g http://127.0.0.1:8000/)
4)Add "/convert/?" followed by the relevant parameters.
5)Paste it in a browser and enter. You should be able to see the output JSON response.
note: “amount”: -1 is returned if any of the input parameters are invalid.

Example API call:
http://127.0.0.1:8000/convert/?amount=3&src_currency=USD&dest_currency=JPY&reference_date=2019-12-05

Example response:
{"amount": 326.36560302866417, "currency": "JPY"}
