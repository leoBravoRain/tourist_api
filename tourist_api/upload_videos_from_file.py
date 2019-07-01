from api.models import Videos_Location, Location
import csv
"""
    Script to import data from .csv file to Model Database DJango

    This mus to be in same folder of the manage.py file

    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('upload_videos_from_file.py').read())
"""
path = 'videos_london.csv'

with open(path, encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        try:

            location = Location.objects.get(name__exact = row['location'])
            
        except:

            print('\n\n EXCEPTION \n\n')
            
            print(Location.objects.all())

            # print('Exception')

            break

        p = Videos_Location(location = location, link = row['link'])

        p.save()

exit()