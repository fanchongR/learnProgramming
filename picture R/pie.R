b2p2 <- colorRamp(c("blue", "purple"))
data$col<-b2p2(seq(0, 1, len = nrow(data)))



position<-matrix(c(1,2,7,3,4,7,5,6,7),nrow=3,byrow=TRUE)
layout( position )
for(i in 2:7){
	data.temp<-data[ data[,i]!=0 ,]
	pie(data.temp[,i],labels=NA,col=data.temp$col)
}
plot(0,0,pch="",xlim=c(0,1),ylim=c(0,26),bty="n",axes=F,xlab="",ylab="")
legend('left',legend=data[,1],col=data$col,pch=15)





# http://iccm.cc/colors-and-palettes-in-r-language/
