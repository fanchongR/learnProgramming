hist(algae$mxPH,prob=T,xlab='',main="Histogram of maximum pH value",ylim=c(0,1))
lines(density(algae$mxPH,na.rm=T))
rug(jitter(algae$mxPH))