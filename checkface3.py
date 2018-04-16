import face_reco


image = face_reco.load_image_file("face7.jpg")
face_locations = face_reco.face_locations(image)

print(face_locations)
