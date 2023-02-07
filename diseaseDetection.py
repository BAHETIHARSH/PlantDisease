import pickle
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")


ans = {0: 'Tomato___Late_blight',
       1: 'Tomato___healthy',
       2: 'Tomato___Early_blight',
       3: 'Tomato___Septoria_leaf_spot',
       4: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
       5: 'Tomato___Bacterial_spot',
       6: 'Tomato___Target_Spot',
       7: 'Tomato___Tomato_mosaic_virus',
       8: 'Tomato___Leaf_Mold',
       9: 'Tomato___Spider_mites Two-spotted_spider_mite'}


def predictDisease(data):
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    val = pickled_model.predict([data])
    return ans[int(val)]