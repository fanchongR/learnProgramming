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
	--file=pathway     - character, blah blah
	--help             - print this text

	Example:
	Rscript heatmap.R --file=pathway \n\n")
	q(save="no")
}

parseArgs <- function (x) strsplit (sub ("^--", "", x), "=")
argsDF <- as.data.frame (do.call ("rbind", parseArgs(args )))
option <- as.list (as.character (argsDF$V2))
names (option) <- argsDF$V1



library(gplots,lib.loc="/home/fanchong/R/x86_64-unknown-linux-gnu-library/2.10/")
data<-read.table(option$file,header=TRUE,row.names="sample")



#celllable<-as.matrix(data)

# set R -> 0 , MS -> 1 , S -> 2
tranline<-function(x){
	as.numeric( factor(x,levels=c("R","MS","S"),labels=c(0,1,2)) )
}

for(i in 1:ncol(data)){
	data[,i]=tranline(data[,i])
}

data<-as.matrix(data)


svg("heatmap.svg")

heatmap.2(data, col=heat.colors(100), scale="none",key=FALSE, symkey=FALSE, density.info="none", trace="none", cexRow=0.2)

dev.off()

