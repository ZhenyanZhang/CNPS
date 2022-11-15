wd<- "D:/onedrive/Geo_distance"
setwd(wd)

library(geosphere)

#load data
lonlat = read.table('data_for_Geo_distance.txt', header=TRUE)

#calculat the geographical distance
muer.lonlat = cbind(lonlat$Longitude, lonlat$Latitude)

muer.dists = distm(muer.lonlat, fun=distVincentyEllipsoid)

rownames(muer.dists) = lonlat$sample
colnames(muer.dists) = lonlat$sample

write.table(muer.dists, 'muer_geodists.txt', quote=FALSE, sep="\t")
