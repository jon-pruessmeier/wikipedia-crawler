import json
import sys

data = [
    {
        'title': 'Staatstheorie',
        'picture': '',
        'text': "Eine Staatstheorie oder Staatsphilosophie behandelt mögliche Definitionen, Entstehung, Formen, Aufgaben und Ziele des Staates sowie dessen institutionelle, soziale, ethische und juristische Bedingungen und Grenzen. Als Teilgebiet der Politischen Philosophie und Konkretion der Allgemeinen Staatslehre berühren Staatstheorien deshalb oftmals Fragestellungen, die mehrere Einzelwissenschaften gleichzeitig betreffen, darunter: die Philosophie, die Theologie, die Politikwissenschaft, die Rechtswissenschaft, die Soziologie und die Volkswirtschaftslehre."
    },
    {
        'title': 'Staat',
        'picture': 'https://de.wikipedia.org/wiki/Staat#/media/Datei:Leviathan_by_Thomas_Hobbes.jpg',
        'text': 'Staat (ugs. bzw. nicht fachspr. auch Land) ist ein mehrdeutiger Begriff verschiedener Sozial- und Staatswissenschaften. Im weitesten Sinn bezeichnet er eine politische Ordnung, in der einer bestimmten Gruppe, Organisation oder Institution eine privilegierte Stellung zukommt – nach Ansicht einiger bei der Ausübung von (politischer) Macht; nach Ansicht anderer hinsichtlich sowohl der Entfaltung des Einzelnen als auch der Gesellschaft.'
    },

    {
        'title': 'Thomas Hobbes',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Thomas_Hobbes_by_John_Michael_Wright_%282%29.jpg',
        'text': 'Thomas Hobbes [hɔbz] (5. April 1588 in Westport, Wiltshire – 4. Dezember 1679 in Hardwick Hall, Derbyshire) war ein englischer Mathematiker, Staatstheoretiker und Philosoph. Er wurde durch sein Hauptwerk Leviathan bekannt, in dem er eine Theorie des Absolutismus entwickelte. Er gilt als Begründer des „aufgeklärten Absolutismus“.[1] Des Weiteren ist er neben John Locke und Jean-Jacques Rousseau einer der bedeutendsten Theoretiker des sogenannten Gesellschaftsvertrags.'
    },

    {
        'title': '',
        'picture': '',
        'text': '',

    }
]
data_json = json.dumps(data)
print(data_json)

sys.stdout.flush()