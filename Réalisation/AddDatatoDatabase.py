import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognationrealtime-38a12-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "333333": 
        {
            "name": "Ouazzani Chahdi Hamza",
            "major": "Data",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-03-07 23:38:34"
        },
    "222222": 
        {
            "name": "Mya Hayat",
            "major": "7anoutt",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2024-03-07 23:38:34"
        },
        
    "444444": 
        {
            "name": "Moufid Anas",
            "major": "Data",
            "starting_year": 2020,
            "total_attendance": 1,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-03-07 23:38:34"
        },
        
    "111111": 
        {
            "name": "Smihi Aya",
            "major": "Data",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-03-07 23:38:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)