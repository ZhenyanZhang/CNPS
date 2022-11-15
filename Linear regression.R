wd<- "D:/onedrive/linear_regression"
setwd(wd)

#load data
data <- read.delim('data_for_LR.txt', row.names = 1, sep = '\t', stringsAsFactors = FALSE, check.names = FALSE)

library(ggplot2)

lmppolyone <- lm(S~poly(richness,1),data = data)
sumone<-summary(lmppolyone)
sumone
ggplot(data, aes(x=richness,y=S))+
  geom_point(size=0.6)+
  geom_smooth(method = lm, formula =y~poly(x,1),  span=0.2)+
  annotate('text', label=paste('R2=',sumone$r.squared,', p=',sumone$coefficients[2,4]), x = 0.1, y = 0.01, size = 5, colour = 'black')+
  theme(panel.grid = element_blank(), panel.background = element_rect(color = 'black', fill = 'transparent'), legend.key = element_rect(fill = 'transparent'))
  

#for multiple LR in one plot
gr <- c("C",
        "N",
        "P",
        "S")

for (i in gr) {
Epipelagic<-subset(data,data$layer=="Epipelagic")
lmpEpipelagic <- summary(lm(Epipelagic[[i]]~poly(depth,1),data = Epipelagic))


Mesopelagic<-subset(data,data$layer=="Mesopelagic")
lmpMesopelagic <- summary(lm(Mesopelagic[[i]]~poly(depth,1),data = Mesopelagic))

Bathypelagic<-subset(data,data$layer=="Bathypelagic")
lmpBathypelagic <- summary(lm(Bathypelagic[[i]]~poly(depth,1),data = Bathypelagic))

Abyssopelagic<-subset(data,data$layer=="Abyssopelagic")
lmpAbyssopelagic <- summary(lm(Abyssopelagic[[i]]~poly(depth,1),data = Abyssopelagic))

p1<-ggplot(data %>% na.omit()) +
  geom_point(aes(depth, data[[i]], colour = layer), 
             size = 1) +
  geom_smooth(aes(depth, data[[i]], colour = layer), method = lm) +
  scale_colour_manual(values = c("Mesopelagic" = "#DD7694",
                                 "Epipelagic"="#1f78b4",
                                 "Bathypelagic"="#00B76D",
                                 "Abyssopelagic"="#FF5900"))+
  scale_x_log10()+
  geom_vline(xintercept = 0, color = 'gray', size = 0.3)+
  geom_vline(xintercept = 200, color = 'gray', size = 0.3)+
  geom_vline(xintercept = 1000, color = 'gray', size = 0.3)+
  geom_vline(xintercept = 4000, color = 'gray', size = 0.3)+
  annotate('text',label=paste(i,'Epipelagic_R2=',lmpEpipelagic$r.squared,', p=',lmpEpipelagic$coefficients[2,4]), x = 1, y = 0.5, size = 5, colour = '#1f78b4')+
  annotate('text',label=paste('Mesopelagic_R2=',lmpMesopelagic$r.squared,', p=',lmpMesopelagic$coefficients[2,4]), x = 1, y = 0.4, size = 5, colour = '#DD7694')+
  annotate('text',label=paste('Bathypelagic_R2=',lmpBathypelagic$r.squared,', p=',lmpBathypelagic$coefficients[2,4]), x = 1, y = 0.3, size = 5, colour = '#00B76D')+
  annotate('text',label=paste('Abyssopelagic_R2=',lmpAbyssopelagic$r.squared,', p=',lmpAbyssopelagic$coefficients[2,4]), x = 1, y = 0.2, size = 5, colour = '#FF5900')+
  theme_bw()
a=paste(i,'_changed_with_depth.pdf')
ggsave(a,device = cairo_pdf,width =6, height =3)
}
