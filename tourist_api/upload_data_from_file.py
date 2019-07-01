from api.models import Location, Place
import csv
"""
    Script to import data from .csv file to Model Database DJango

    This mus to be in same folder of the manage.py file

    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('upload_data_from_file.py').read())
"""
path = 'places_london.csv'

with open(path, encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
        try:

            place = Place.objects.get(name__exact = row['place'])
            
        except:

            break

        p = Location(name = row['location'], latitude = row['latitude'], longitude = row['longitude'], place = place)
        p.save()

exit()