from  pymongo import MongoClient
# import pymongo
from bson import ObjectId

client =  MongoClient("mongodb+srv://lakshmanpy:lakshmanpy@cluster1.sykqu.mongodb.net/softwareEngineer",  tlsAllowInvalidCertificates=True)
# Not a good idea to include id nad password in code files
#  tlsAllowInvalidcertificates = True __ Not a good idea to handle


print(client)
db = client["Lakshman"]
video_collection = db["videos"]

print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
     for video in video_collection.find():
        print(f"ID: {video['_id']}, Name:{video['name']} and Time: {video['time']}")

def update_video(video_id, new_name , new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    result = video_collection.delete_one({"_id": ObjectId(video_id)})
    if result.deleted_count > 0:
        print(f"Successfully deleted video with ID: {video_id}")
    else:
        print(f"No video found with ID: {video_id}") 

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List al videos")
        print("2. Add a new videos")
        print("3. Delete a  videos")
        print("4. Delete a  videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated  video name:")
            time = input("Enter the  updated video time:")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id, name, time)
        elif choice == '5':
            break
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()