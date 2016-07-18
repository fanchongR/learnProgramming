#!/usr/bin/Rscript
library(optparse,lib.loc="/home/fanchong/R/x86_64-unknown-linux-gnu-library/2.10/")
args<-commandArgs(TRUE)
if(length(args)<1){
	        args<-c("--help")
}

if("--help" %in% args ){
	cat("
	The R Script
	Author: fanchong@genomics.cn

	Arguments:
	--SNP=filepath
	if run Separation Site, Nucleotide Polymorphism and Tajima's D testing, set:
		--windows=100000 (bp)
		--moving=5000 (bp)
	--help
	Example:
	Rscript polymorphism.R --SNP=filepath --windows=100000 --moving=5000 \n\n")
	q(save="no")
}

parseArgs <- function (x) strsplit (sub ("^--", "", x), "=")
argsDF <- as.data.frame (do.call ("rbind", parseArgs(args )))
option <- as.list (as.character (argsDF$V2))
names (option) <- argsDF$V1



###allele frequency
data<-read.table(option$SNP,header=F,na.strings="-")
output<-data.frame(genename=data[,1],position=data[,2])
data<-data[,c(-1,-2,-3)]

N<-nrow(data)
samplenum<-ncol(data)

F<-rep(NA,N)
allele1<-rep(NA,N)
allele2<-rep(NA,N)


filter<-list( c("M","A","C"),c("R","A","G"),c("W","A","T"),c("S","C","G"),c("Y","C","T"),c("K","G","T") )
hybrid<-c("M","R","W","S","Y","K")
base<-c("A","G","C","T")

for(i in 1:N){	
	temp<-as.vector(unlist(data[i,]))
	temp<-temp[!is.na(temp)]
	if( length(temp) == 0 )next
	combination<-sapply(filter,function(y)all(temp %in% y))
	if(!any(combination))next
	frequency<-table(temp)
	
	name.hybrid<-names(frequency) %in% hybrid
	name.base<-names(frequency) %in% base
	frequency<-as.vector(frequency)
	
	if( length(frequency)==1 & name.base )next
	
	allele<-c(0,0)
	if( any(name.hybrid) )allele<-allele+frequency[name.hybrid]
	if( sum(name.base)==2 )allele<-allele+2*frequency[name.base]
	if( sum(name.base)==1 )allele<-allele+2*c(frequency[name.base],0)
	
	allele1[i]<-allele[1]
	allele2[i]<-allele[2]

	x1x2<-prod(allele/sum(allele))
	if(any(name.hybrid))X12<-prop.table(frequency)[name.hybrid] else X12<-0
	F[i]<-(2*x1x2-X12)/(2*x1x2)
}



output$allele1<-allele1
output$allele2<-allele2
output$F<-F

write.table(output,file="allele.frequency",sep="\t",row.names=FALSE,quote=FALSE,append=TRUE)


###Separation Site, Nucleotide Polymorphism

if( !is.null(option$moving) ){

stop.position<-output$position[N]
output<-output[!is.na(output$allele1),]

moving<-as.numeric(option$moving)
windows<-as.numeric(option$windows)

windows.now<-c(0,windows)
a1<-sum( 1/(1:(samplenum-1)) )
sita<-list()

allele.prod<-output$allele1 * output$allele2
allele.sum<-output$allele1 + output$allele2
Pi<-( allele.prod * 2 )/( allele.sum )/( allele.sum -1 )


repeat{
	position.now<-output$position >= windows.now[1] & output$position <= windows.now[2]
	S<-sum(position.now)
	sita.now<-S/windows/a1

	Pi.now<-sum( Pi[position.now] )/windows

	record<-c(windows.now[1],windows.now[2],sita.now,Pi.now)
	sita<-c(sita,list(record))
	
	if( windows.now[2] > stop.position)break
	windows.now<-windows.now+moving
}


Separation.Site<-as.data.frame(do.call(rbind,sita))
names(Separation.Site)<-c("Start","End","Sita","Pi")



###Tajima's D
sequence<-1:(samplenum-1)
a1c<-sum(1/sequence)
a2c<-sum( (1/sequence)^2 )
b1c<-(samplenum+1)/(3*(samplenum-1))
b2c<-2*(samplenum*samplenum+samplenum+3)/( 9*samplenum*(samplenum-1) )
c1c<-b1c-( 1/a1c )
c2c<-b2c - (samplenum+2)/(a1c*samplenum) + a2c/(a1c*a1c)
e1c<-c1c/a1c
e2c<-c2c/( (a1c*a1c)+a2c )

D.numerator<-Separation.Site$Pi-Separation.Site$Sita/a1c
D.denominator<-sqrt( e1c*Separation.Site$Sita + e2c*Separation.Site$Sita*(Separation.Site$Sita-1) )
Separation.Site$Tajima.D <- D.numerator/D.denominator




write.table(Separation.Site,file="Site.Polymorphism",sep="\t",row.names=FALSE,quote=FALSE,append=TRUE)

}








q(save="no")


	





	

