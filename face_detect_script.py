import face_recognition
import os
from picamera import PiCamera
from time import sleep

camera = PiCamera()
goAgain = "y"
people_list = ["Amogh", "Laddha", "Prakhar"]
results = [False, False, False]
print("People list retrieved")

# Load the jpg files into numpy arrays
amogh_image = face_recognition.load_image_file("amogh.jpg")
prakhar_image = face_recognition.load_image_file("prakhar.jpg")
laddha_image = face_recognition.load_image_file("laddha.jpg")
print("Images read")

amogh_face_encoding = face_recognition.face_encodings(amogh_image)[0]
laddha_face_encoding = face_recognition.face_encodings(laddha_image)[0]
prakhar_face_encoding = face_recognition.face_encodings(prakhar_image)[0]
print("Encoding done")

known_faces = [
    amogh_face_encoding,
    laddha_face_encoding,
    prakhar_face_encoding
]


while goAgain == "y":
    os.remove("amoghnew.jpg")
    print("Starting camera")
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Documents/FaceDetection/amoghnew.jpg')
    camera.stop_preview()
    sleep(2)

    unknown_image = face_recognition.load_image_file("amoghnew.jpg")
    
    try:
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    except:
        print("Can't find face. Please try again")
        continue


    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    print(results)
    if True in results:
        print("Hi {}. How are you doing?".format(people_list[results.index(True)]))
    else:
        print("Can't recognize you.")
    results = [False, False, False]
    print(results)
    results.clear()
    print(results)

    #print("Is the unknown face a picture of Biden? {}".format(results[0]))
    #print("Is the unknown face a picture of Obama? {}".format(results[1]))

#    print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
    goAgain = input("Want to go again? (y/n)")

