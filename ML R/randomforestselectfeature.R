group<-read.table("individual_2group.txt",header=F)
group<-group[,6]
data<-read.table("try.txt",header=F,na.strings="-")
genename<-paste(data[,1],data[,2],sep="_")

N<-nrow(data)
for(i in 1:N)data[i,][is.na(data[i,])]<-data[i,3]
data<-data[,c(-1,-2,-3)]
data<-t(data)
data<-as.data.frame(data)
data<-cbind(group,data)
names(data)<-c("group",genename)


library(randomForest)
BOO<-list()
data.temp<-data
N.temp<-ncol(data.temp)-1
restname<-list(names(data.temp))
repeat{
	rmN.temp<-round(N.temp*0.2)
	sol.forest<-randomForest(group~.,data.temp,importance=TRUE,proximity=TRUE)
	BOO<-c(BOO,list(1 - sum( diag(sol.forest$confusion) ) / sum((sol.forest$confusion)[,-3]) ))  #二分类，就-3，三分类-4
	VI<-sol.forest$importance   
	
	rmname.temp<-row.names(VI[order(VI[,3]),])[1:rmN.temp]
	name.temp<- names(data.temp)[ !(names(data.temp) %in% rmname.temp) ]
	restname<-c(restname,list(name.temp))
	data.temp<-data.temp[,name.temp]
	N.temp<-ncol(data.temp) -1
	
	
	
	if(N.temp < 6)break
}
