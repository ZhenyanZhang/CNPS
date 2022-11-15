wd<- "D:/onedrive/hierarchical_clustering"
setwd(wd)

library(factoextra)
library(cluster)

#load data
df <- read.delim('matrix_for_ET.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE,na.strings="na")

#remove rows with missing values
df <- na.omit(df)

#scale each variable to have a mean of 0 and sd of 1
df <- scale(df)

#view first six rows of dataset
head(df)

#define linkage methods
m <- c( "average", "single", "complete", "ward")
names(m) <- c( "average", "single", "complete", "ward")

#function to compute agglomerative coefficient
ac <- function(x) {
  agnes(df, method = x)$ac
}

#calculate agglomerative coefficient for each clustering linkage method
sapply(m, ac)
#choose the best method with the highest agglomerative coefficient

#calculate average silhouette width for each number of clusters (up to 20 clusters)
fviz_nbclust(df, hcut, method = "silhouette",k.max=20)
#choose the best number of clusters with the highest average silhouette width

#hierarchical clustering
#calculate the euclidean distance between samples
result <- dist(df, method = "euclidean")

#Cluster with the clustering linkage method chosen above
result_hc <- hclust(d = result, method = "ward.D2")

#Cluster into groups as the number chosen above
groups <- cutree(final_clust, k=7)

# add the clustering information to the original matrix and save
final_data <- cbind(df, cluster = groups)
write.csv(as.matrix(final_data),'Results_HC.csv')

#visualization
fviz_dend(result_hc, k =7, show_labels=F, 
          cex = 0.15, 
          k_colors = c("red", "blue", "orange", "purple", "skyblue", "grey","black"),
          color_labels_by_k = TRUE,
          type = c("circular"),
          #phylo_layout=c("layout.gem"),
          repel =T,
          rect = TRUE          
)





