x1<-rep(1:3,5)
x2<-c("S","M","M",rep("S",3),"M","M",rep("L",3),"M","M","L","L")
y<-rep( c(-1,1,-1,1,-1),c(2,2,3,7,1) )
data<-data.frame(x1,x2,y)


naive.bayes<-function(data,testsample){      #输入是数据框或矩阵，最后一列是类别变量
	if(is.matrix(data))data<-as.data.frame(data)
	dimension<-ncol(data)
	class<-data[,dimension]
	
	P.class<-prop.table(table(class))
	data.group<-split(data,data[,dimension])
	
	cond.prop<-function(X){
		lapply( 1:(dimension-1),function(x)prop.table(table(X[,x])) )	
	}
	probability<-lapply(data.group,cond.prop)  #a list whose name is the classname. And the element is a list,whose element is the variable conditional probability one by one( totally dimension -1 )


	if(is.vector(testsample))testsample<-t(as.matrix(testsample))
	if(is.data.frame(testsample))testsample<-as.matrix(testsample)
	N<-nrow(testsample)
		

	result.group<-function(prob.group,onesample){			
		result<-sapply(1:(dimension-1),function(i)prob.group[[i]][ as.character(onesample[i]) ] )
		prod(result)
	}
	discriminent<-function(probability,onesample){
		result<-sapply(probability,function(x)result.group(x,onesample))
		result<-result*P.class
		names(which.max(result))
	}
	decision<-sapply( 1:N,function(i)discriminent(probability,testsample[i,]) )
	cbind(testsample,decision)
}

	

		

