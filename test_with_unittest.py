from unittest import TestCase
import RX as rx
import IA as ia
import Export as export

class TryTesting(TestCase):

    def test_cargue_jpg(self):        
        dcm=rx.JPGPNG()
        rxLoad = rx.RXRead(dcm)
        array, img2show = rxLoad.read_file("/Users/dmg/Documents/postgradoIA/images/virus/person1501_virus_2611.jpeg")        
        assert (array.shape == (640, 1024, 3))


    def test_predict(self):
        dcm=rx.JPGPNG()
        rxLoad = rx.RXRead(dcm)
        array, img2show = rxLoad.read_file("/Users/dmg/Documents/postgradoIA/images/virus/person1501_virus_2611.jpeg")                
        deepIA = ia.IA()
        label, proba, heatmap = deepIA.predict(array)        
        print(proba)
        assert (float(proba) >50)
