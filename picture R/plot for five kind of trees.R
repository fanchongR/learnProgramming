Orange$Tree<-as.numeric(Orange$Tree)
xrange<-range(Orange$age)
yrange<-range(Orange$circumference)
plot(xrange,yrange,type="n",xlab="Age (days)",ylab="Circumference (mm)")
n<-max(Orange$Tree)

color<-rainbow(n)
linetype<-c(1:n)
plotchar<-18:(18+n)

for(i in 1:n){
	tree<-subset(Orange,Tree==i)
	lines(tree$age,tree$circumference,type="b",lwd=2,
	lty=linetype[i],col=color[i],pch=plotchar[i])
}

title("Tree Growth","example of line plot")

legend(xrange[1],yrange[2],1:n,cex=0.8,
	col=color,pch=plotchar,lty=linetype,title="Tree")