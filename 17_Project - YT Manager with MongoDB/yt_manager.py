import pymongo
from bson import ObjectId

mongoURL = 'mongodb+srv://710vermaraj:JAuBEflwcUhqXgJ5@cluster0.jdlorrm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = pymongo.MongoClient(mongoURL)

# first create a database i.e. db
db = client['ytmanager']

# created first collection in db
video_collection = db['videos']

# print(video_collection)   # output - connection string

def list_videos():
    videos = video_collection.find()
    for video in videos:
        print(f'ID : {video['_id']} , Name : {video['name']}, Playtime : {video['time']}')

def add_video(name, time):
    video_collection.insert_one({"name":name, "time":time})

def update_video(video_id, name, time):
    list_videos()

    whichToFind = {'_id': video_id}             # ❌ wrong way to find id
    whichToFind = {'_id': ObjectId(video_id)}   # ✅ correct way
    whatToUpdate = {'name':name, 'time':time}
    
    video_collection.update_one(
        whichToFind,
        {'$set': whatToUpdate}
    )

def delete_video(video_id):
    # TODO : this is a keyword to use when something you want to do later in code part
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main():
    while True: 
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        # try to use for match keyword instead of if-elif ladder
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

if __name__ == '__main__':
    main()