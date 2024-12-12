# yt manager

import json 

def load_data():
    try:
        with open("youtube.txt", "r") as file:
           return json.load(file)                              #  it reads data from file loads it and converts it to json format  
    except FileNotFoundError:
        return []


def save_helper_data(videos):
    with open("youtube.txt", "w") as file:                   # direct file load if done then it will be a string in read,writing format here its a list
        json.dump(videos, file , indent =4)                  # json.dump(kya likhna hai , kaha likhna hai)
        
    

def list_all_videos(videos):
    print("\n")
    print("*" * 70 )
    for index , video in enumerate(videos, start =1):                        # we needed to enumerate as we din't had indexing here it was just a list with objects w/o indexing 
        print(f"{index}.{video['name']}, ( Duration: {video['time']}) ")
    print("\n")
    print("*" * 70 )    

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name , "time": time})
    save_helper_data(videos)
    print("Video added successfully!")

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you wanna update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {"name": name , "time": time}
        save_helper_data(videos)
    else:
        print("Invalid index selected ")



def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    
    if 1<= index <= len(videos):
        del videos[index - 1]
        save_helper_data(videos)
    else:
        print("invalid index selected")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager  | choose an option")
        print("1. List all youtube videos")
        print("2. Add a yt video")
        print("3. Update a yt video details")
        print("4. Delete a yt video")
        print("5. Exit the app")


        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_videos(videos)
            case 3:
                update_videos(videos)    
            case 4:
                delete_videos(videos)
            case 5:
                print("exiting application")
                break
            case _:
                print("Invalid Choice. Please try again.")
        
                
                
                
if __name__ == "__main__":
    main()