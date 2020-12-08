import pandas as pd
from imutils import paths
import xlsxwriter
from classify import Predictor

pred = Predictor()

ripe = []
color = []
name = []
# loop over the test images
for imagePath in paths.list_images("finaltest"):
    color.append(pred.make_prediction(imagePath)[0])
    ripe.append(pred.make_prediction(imagePath)[1])
    name.append(imagePath.split('/')[-1])

final = { "File Name":name, "Predicted Color" : color, "Predicted Ripeness" : ripe}
dataset = pd.DataFrame(final)
writer = pd.ExcelWriter("hahu.xlsx", engine="xlsxwriter")
dataset.to_excel(writer,sheet_name="shit1")
writer.save()
