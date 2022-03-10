import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyA9iVMh1oY3F8WQ-cUuPLAtrfY2aUMpX2s",
    "authDomain": "heartrate-8fc50.firebaseapp.com",
    "projectId": "heartrate-8fc50",
    "storageBucket": "heartrate-8fc50.appspot.com",
    "databaseURL": "https://heartrate-8fc50-default-rtdb.europe-west1.firebasedatabase.app/",
    "messagingSenderId": "82089823374",
    "appId": "1:82089823374:web:655c54cc68590867590ddf",
    "measurementId": "G-PM2BCMQ4TM"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

last_heart_rate_value_1 = None
db_empty_flag = True

while True:
    heart_rate_values = db.child("heart rate values").get()
    heart_rate_value = heart_rate_values.val()
    if heart_rate_value is not None:
        last_heart_rate_value = list(heart_rate_value.values())[-1]
        if last_heart_rate_value != last_heart_rate_value_1:
            last_heart_rate_value_1 = last_heart_rate_value
            db_empty_flag = True
            print(last_heart_rate_value)
        continue
    elif db_empty_flag:
        db_empty_flag = False
        print("heart rate values is empty")
