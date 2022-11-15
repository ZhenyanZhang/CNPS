wd<- "D:/onedrive/boxplot"
setwd(wd)

library(viridis)
library(ggplot2)

# create a dataset
data <- read.delim('data_for_boxplot.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE,na.strings="na")

# Plot
ggplot(data, aes(x=LAYER, y=Denitrification,fill=LAYER)) +
  geom_boxplot(notch=F,notchwidth=0.5,width =0.5,outlier.color="black") +
  geom_jitter(size=0.1, alpha=0.6,width =0.1) +
  scale_fill_viridis(discrete = TRUE, alpha=0.6) +
  stat_summary(fun.y=mean, geom="point", shape=16, size=6, color="red", fill="red") +
    theme(panel.grid = element_blank(), panel.background = element_rect(color = 'black', fill = 'transparent'), legend.key = element_rect(fill = 'transparent'))+
  xlab("")
