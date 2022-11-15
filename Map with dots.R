library(ggplot2)
library(ggmap)

wd<- "D:/onedrive/map_withdots"
setwd(wd)

#load data
data =read.table("data_for_map.txt",header = T, row.names = 1)

map<-NULL #define a map without information

mapworld<-borders("world",colour = NA,fill="gray50") #draw the basic map

map<-ggplot()+
  mapworld+
  ylim(-90,90)+
  theme(panel.grid = element_blank(), panel.background = element_rect(color = 'black', fill = 'transparent'), legend.key = element_rect(fill = 'transparent'))+
  geom_point(aes(x=datac$long,y=datac$lat,color=datac$layer,size=data$number),alpha=0.8)
map