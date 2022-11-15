wd<- "D:/onedrive/Stacked_barplot"
setwd(wd)

library(ggplot2)

#load data
data <- read.delim('data_for_Stacked_barplot.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE,na.strings="na")

# Stacked
ggplot(data, aes(fill=phylum, y=abundance, x=rank)) + 
  geom_bar(position="fill", stat="identity")+
theme(axis.ticks.x = element_blank(),
      axis.text.x = element_blank())

