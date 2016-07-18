p<-function(x)0.3*exp(-0.3*x^2)+0.7*exp(-0.3*(x-10)^2)
sigma<-10
q<-function(x1,x2)dnorm(x1,x2,sigma)
A<-function(x1,x2)min( 1,p(x2)*q(x1,x2)/p(x1)/q(x2,x1) )

N<-10000
x[1]<-0
for(i in 1:N){
	u<-runif(1)
	x.temp<-rnorm(1,x[i],sigma)
	if( u< A(x[i],x.temp) )x[i+1]<-x.temp else x[i+1]<-x[i]
}


#plot(x,type="l")

x.seq<-seq(-5,15,length=1000)
hist(x,breaks=100,freq=F)
lines(x.seq,0.3*p(x.seq))
x<-NULL




 