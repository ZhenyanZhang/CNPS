wd<- "D:/OneDrive/PCA"
setwd(wd)
library(factoextra)
library(FactoMineR)

#load data
data <- read.delim('data_for_pca.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE,na.strings="na")
data <- data.frame(t(data))
group <- read.delim('group.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE,na.strings="na")

#PCA
pca2 <- PCA(data,scale.unit = T,ncp=5,graph = T)
summary(pca2)

genetype<-as.factor(gene$type)
names(genetype)<-row.names(pca2$var$contrib)

#Visualization
fviz_pca_biplot(
  pca2,
  geom = c("line","point"),
    axes = c(1, 2),
  col.var = genetype, palette = c("red", "black", "grey", "purple", "orange")
  )
