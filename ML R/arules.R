#!/ifs4/BC_PUB/biosoft/pipeline/Package/R-3.1.1/bin/Rscript
library(optparse,lib.loc="/home/fanchong/R/x86_64-unknown-linux-gnu-library/2.10/")
args<-commandArgs(TRUE)
if(length(args)<1){
	        args<-c("--help")
}

if("--help" %in% args ){
	cat("
	The R Script
	Arguments:
	--file=filepath 
	--n=
	--help             - print this text
	\n\n")
	q(save="no")
}

parseArgs <- function (x) strsplit (sub ("^--", "", x), "=")
argsDF <- as.data.frame (do.call ("rbind", parseArgs(args )))
option <- as.list (as.character (argsDF$V2))
names (option) <- argsDF$V1

library(arules,lib.loc="/home/fanchong/R/x86_64-unknown-linux-gnu-library/2.10/")


data<-read.table(option$file,sep="\t",header=TRUE)

snpname<-data[,1]
data<-data[,c(-1,-2)]
data<-as.data.frame(t(data))
names(data)<-snpname

numcol<-ncol(data)
for(i in 1:numcol)data[,i]<-as.factor(data[,i])




data2<-as(data,"transactions")
N<-as.numeric(option$n)
rules<-apriori(data2,parameter=list(confidence=1,maxlen=4))
x<-subset(rules,subset = rhs %pin% "=1" & lhs %pin% "=1")
inspect(sort(x,by="support")[1:N]) 





















q(save="no")

