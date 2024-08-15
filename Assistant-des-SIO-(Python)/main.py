# -*- coding: utf-8 -*-
import sys
from pronotepy.ent import ent_auvergnerhonealpe
from pronotepy import Client
from datetime import date, timedelta

if __name__ == "__main__":
    # Récupère les arguments passés depuis le script JavaScript
    username = sys.argv[1]
    password = sys.argv[2]
    
    client = Client('https://0382780r.index-education.net/pronote/eleve.html',
                    username=username,
                    password=password,
                    ent=ent_auvergnerhonealpe)

    today = date.today()
    end_of_year_next = date(today.year + 1, 6, 30)
    homework = client.homework(date_from=today, date_to=end_of_year_next)
    for hw in homework:
        sys.stdout.buffer.write(f"{hw.subject.name} {hw.description}\n".encode('utf-8'))
