import haversine as hs
import os
import shutil
import exifread

class ImagePoint:
    def __init__(self,path, point):
        self.path = path
        self.point = point

    def __str__(self):
        return "Path: {}, Location: {}".format(self.path,self.point)

class ImageDistanceCataloger:
    def __init__(self,input='input',output='output', force=False):
        self.images = os.listdir(input)

        isExists = os.path.isdir(output)
        if isExists:
            if force:
                print("# Removing output, Path: {}".format(output))
                shutil.rmtree(output)
            else:
                raise Exception("Output directory already exists (-f to overwrite)")

        self.input = input
        self.output = output


    def get_decimal_from_dms(self,dms, ref):
        degrees = dms.values[0]
        minutes = dms.values[1] / 60.0
        seconds = dms.values[2] / 3600.0

        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds

        return round(degrees + minutes + seconds, 5)

    def get_coordinates(self, geotags):
        lat = self.get_decimal_from_dms(geotags['GPS GPSLatitude'], geotags['GPS GPSLatitudeRef'])
        lon = self.get_decimal_from_dms(geotags['GPS GPSLongitude'], geotags['GPS GPSLongitudeRef'])
        return (lat,lon)

    def groupByDistance(self, points, r):
        groups = []
        for point in points:
            found_group = False
            for group in groups:
                for member in group:
                    if hs.haversine(member.point, point.point,unit=hs.Unit.METERS) <= r:
                        group.append(point)
                        found_group = True
                        break

                    if found_group:
                        break

            if not found_group:
                groups.append([point])
        return groups

    def group_by_distance(self, r):
        imagePoints = []

        for fname in self.images:
            try:
                path = os.path.join(self.input,fname)
                with open(path, 'rb') as f:
                    geotags = exifread.process_file(f)
                    point = self.get_coordinates(geotags)

                    imagePoints.append(ImagePoint(path, point))
            except Exception as e:
                print("### {} skipping, Err: {}".format(path, e))                

        groups = self.groupByDistance(imagePoints, r)
        for idx, g in enumerate(groups):
            groupDir = os.path.join(self.output,str(idx))
            print("\n## Group", groupDir)
            if not os.path.exists(groupDir):
                os.makedirs(groupDir)
            for p in g:
                print(p)
                newFileName = os.path.join(groupDir, os.path.basename(p.path))
                shutil.copy2(p.path, newFileName)