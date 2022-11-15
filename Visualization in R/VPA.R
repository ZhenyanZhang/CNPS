wd<- "D:/onedrive/VPA"
setwd(wd)

#load data
data <- read.delim('data_for_VPA.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE,na.strings="na")

library(vegan)


VPA<-varpart(Y = data$C_potential, X = data[,1:27],
             data[,28:32],
             data[,33:34])
#factors can be divided into multiple groups like: data[,x:xx],data[,x2:xxx2]
VPA
plot(VPA,bg=2:4)

