import dlib
from skimage import io
from scipy.spatial import distance

img1 = io.imread('Data/Download/Foto1.jpg')
img2 = io.imread('Data/Download/Foto2.jpg')

def descriptor_finding(img):
    sp = dlib.shape_predictor('Saved_models/shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('Saved_models/dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()


    win1 = dlib.image_window()
    win1.clear_overlay()
    win1.set_image(img)

    dets = detector(img, 1)

    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left,(), d.top(), d.right(), d.bottom()))
        shape = sp(img, d)
        win1.clear_overlay()
        win1.add_overlay(d)
        win1.add_overlay(shape)

    face_descriptor_1 = facerec.compute_face_descriptor(img, shape)
    return(face_descriptor_1)



def euclidean_distance(function, img1, img2):
    a = distance.euclidean(function(img1), function(img2))
    return a

