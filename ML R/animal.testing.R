#!/usr/bin/Rscript
library(optparse)
args<-commandArgs(TRUE)
if(length(args)<1){
	        args<-c("--help")
}

if("--help" %in% args ){
        cat("
                The R Script
                Arguments:
                --SNP=filepath  
                --trait=filepath  
                --help            

		Example:
                Rscript animal.testing.R --SNP=filepath --trait=filepath \n\n")
	q(save="no")
}

parseArgs <- function (x) strsplit (sub ("^--", "", x), "=")
argsDF <- as.data.frame (do.call ("rbind", parseArgs(args )))
option <- as.list (as.character (argsDF$V2))
names (option) <- argsDF$V1



group<-read.table(option$trait,header=F)
group<-group[,6]
data<-read.table(option$SNP,header=F,na.strings="-")
output<-data.frame(genename=data[,1],position=data[,2])
data<-data[,c(-1,-2,-3)]


N<-nrow(data)
pvalue<-rep(2,N)
for(i in 1:N){
	temp<-t(data[i,])
	if( length(table(temp))<=1 )next
	pvalue[i]<-fisher.test(as.vector(temp),group)$p.value
}

output$pvalue<-pvalue

write.table(output,file="fisher.pvalue",sep="\t",quote=F,row.names=F,append=TRUE)
output0.05<-output[output$pvalue<0.05,]
write.table(output0.05,file="fisher.pvalue0.05",sep="\t",quote=F,row.names=F,append=TRUE)
output0.01<-output0.05[output0.05$pvalue<0.01,]
write.table(output0.01,file="fisher.pvalue0.01",sep="\t",quote=F,row.names=F,append=TRUE)






