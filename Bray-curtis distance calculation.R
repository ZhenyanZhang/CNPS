wd<- "D:/onedrive/Bray_curtis_distance"
setwd(wd)

library(vegan)

#load data
data = read.table('data_for_BC_distance.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE,na.strings="na")

#calculate the Bray-curtis distance
BCdistance <- vegdist(otu, method = 'bray')

write.table(BCdistance, 'muer_geodists.txt', quote=FALSE, sep="\t")
