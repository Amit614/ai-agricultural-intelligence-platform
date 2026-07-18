class VegetationIndexService:
    @staticmethod
    def ndvi(nir:float, red:float)->float:
        d = nir + red
        return 0.0 if d == 0 else round((nir-red)/d,4)
