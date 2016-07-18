perceptron<-function(data,h=1){             #输入为矩阵或数据框，最后一列是类别
	data<-as.matrix(data)
	num<-nrow(data)
	dimension<-ncol(data)
	x<-data[,-dimension]
	y<-data[,dimension]
	
	plot(x[,1],x[,2]);text(x[,1],x[,2],y)

	G<-matrix(0,nrow=num,ncol=num)
	for(i in 1:num){
		for(j in 1:num){
			G[i,j]<-x[i,] %*% x[j,]
		}
	}
      
	a<-rep(0,num);b<-0
		
	i<-1
	while(i<=num){
		if( y[i]*(sum(a*y*G[,i])+b) <=0 ){a[i]<-a[i]+h;b<-b+h*y[i];i<-1} else i<-i+1
	}

	w<-rep(0,dimension-1)
	for(i in 1:(dimension-1))w<-w+a[i]*y[i]*x[i,]
	abline(-b/w[2],-w[1]/w[2])
	names(w)<-paste("weight",1:(dimension-1),sep="");names(b)<-"bias"
	model<-list(w=w,b=b)
	model
}

	
	