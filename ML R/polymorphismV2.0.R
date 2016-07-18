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
	if divide into two groups, set:
		--group=11111,21212,12121,21211,12121	(any insert of Comma and Colon is acceptable in case of input error)
	--help
	Example:
	Rscript polymorphismV2.0.R --SNP=filepath --windows=100000 --moving=5000 \n\n")
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

allele.frequency<-function(data){
	F<-rep(NA,N)
	allele.all<-data.frame(A=rep(NA,N),G=rep(NA,N),C=rep(NA,N),T=rep(NA,N) )
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
		name.hybrid2<-hybrid[match(names(frequency),hybrid)]
		name.base2<-base[match(names(frequency),base)]
		name.base2<-name.base2[!is.na(name.base2)]
	
		if( length(frequency)==1 & name.base )next
	
		allele<-c(0,0,0,0)
		names(allele)<-c("A","G","C","T")   #for A G C T
		if( any(name.hybrid) ){
			temp.hybrid<-name.hybrid2[!is.na(name.hybrid2)]
			num.hybrid<-as.numeric(match(temp.hybrid,hybrid))
			name.temp<-filter[[num.hybrid]][c(2,3)]
			allele[name.temp]<-allele[name.temp]+frequency[name.hybrid]
		}
		if( sum(name.base)==2 | sum(name.base)==1)allele[name.base2]<-allele[name.base2]+2*frequency[name.base2]
		allele.all[i,]<-allele

		allele<-allele[allele != 0]
		allele1[i]<-allele[1]
		allele2[i]<-allele[2]
		x1x2<-prod(allele/sum(allele))
		if(any(name.hybrid))X12<-prop.table(frequency)[name.hybrid] else X12<-0
		F[i]<-(2*x1x2-X12)/(2*x1x2)
	}

	list(allele.all=cbind(allele.all,F),allele1=allele1,allele2=allele2)
}


if(is.null(option$group)){
	temp<-allele.frequency(data)
	output1<-output
	output1$allele1<-temp$allele1
	output1$allele2<-temp$allele2
	output<-cbind(output,temp$allele.all)
	write.table(output,file="allele.frequency",sep="\t",row.names=FALSE,quote=FALSE,append=TRUE)
}else{
	temp<-gsub('[,:]','',option$group)
	group<-strsplit(temp,"")[[1]]
	data1<-data[,group == 1]
	data2<-data[,group == 2]
	samplenum<-ncol(data1)
	samplenum2<-ncol(data2)
	return1<-allele.frequency(data1)
	return2<-allele.frequency(data2)
	
	output1<-output
	output1$allele1<-return1$allele1
	output1$allele2<-return1$allele2
	output2<-output
	output2$allele1<-return2$allele1
	output2$allele2<-return2$allele2
	fst<-1 - ( output1$allele1 * output2$allele2 + output1$allele2 * output2$allele1 )/(output1$allele1 + output2$allele1 )/(output1$allele2 + output2$allele2)
	output2$fst<-fst

	output<-cbind(output,return1$allele.all)
	output$line<-"|"
	output<-cbind(output,return2$allele.all)
	write.table(output,file="allele.frequency",sep="\t",row.names=FALSE,quote=FALSE,append=TRUE)
}



###Separation Site, Nucleotide Polymorphism

if( !is.null(option$moving) ){

	stop.position<-output1$position[N]
	output1<-output1[!is.na(output1$allele1),]
	if(!is.null(option$group))output2<-output2[!is.na(output2$allele1),]

	moving<-as.numeric(option$moving)
	windows<-as.numeric(option$windows)

	windows.now<-c(0,windows)
	a1<-sum( 1/(1:(samplenum-1)) )
	if(!is.null(option$group)) a2<-sum( 1/(1:(samplenum2-1)) )
	sita1<-list()
	sita2<-list()
	fst<-list()

	allele.prod1<-output1$allele1 * output1$allele2
	allele.sum1<-output1$allele1 + output1$allele2
	Pi1<-( allele.prod1 * 2 )/( allele.sum1 )/( allele.sum1 -1 )
	if(!is.null(option$group)){
		allele.prod2<-output2$allele1 * output2$allele2
		allele.sum2<-output2$allele1 + output2$allele2
		Pi2<-( allele.prod2 * 2 )/( allele.sum2 )/( allele.sum2 -1 )
	}


	repeat{
		position.now1<-output1$position >= windows.now[1] & output1$position <= windows.now[2]   # logical vector
		S1<-sum(position.now1)
		sita.now1<-S1/windows/a1

		Pi.now1<-sum( Pi1[position.now1] )/windows

		record1<-c(windows.now[1],windows.now[2],sita.now1,Pi.now1)
		sita1<-c(sita1,list(record1))

		if(!is.null(option$group)){
			position.now2<-output2$position >= windows.now[1] & output2$position <= windows.now[2]
			S2<-sum(position.now2)
			sita.now2<-S2/windows/a2
			Pi.now2<-sum( Pi2[position.now2] )/windows
			fst.now<-sum( output2$fst[position.now2],na.rm=TRUE)/windows

			record2<-c(sita.now2,Pi.now2)
			sita2<-c(sita2,list(record2))
			fst<-c(fst,list(fst.now))
		}
		
		if( windows.now[2] > stop.position)break
		windows.now<-windows.now+moving
	}	


	Separation.Site1<-as.data.frame(do.call(rbind,sita1))
	names(Separation.Site1)<-c("Start","End","Sita","Pi")
	if(!is.null(option$group)){
		Separation.Site2<-as.data.frame(do.call(rbind,sita2))
		names(Separation.Site2)<-c("Sita","Pi")
		fst<-as.vector(do.call(rbind,fst))
	}




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

	D.numerator1<-Separation.Site1$Pi-Separation.Site1$Sita/a1c
	D.denominator1<-sqrt( e1c*Separation.Site1$Sita + e2c*Separation.Site1$Sita*(Separation.Site1$Sita-1) )
	Separation.Site1$Tajima.D <- D.numerator1/D.denominator1
	
	if(!is.null(option$group)){
		sequence<-1:(samplenum2-1)
		a1c<-sum(1/sequence)
		a2c<-sum( (1/sequence)^2 )
		b1c<-(samplenum2+1)/(3*(samplenum2-1))
		b2c<-2*(samplenum2*samplenum2+samplenum2+3)/( 9*samplenum2*(samplenum2-1) )
		c1c<-b1c-( 1/a1c )
		c2c<-b2c - (samplenum2+2)/(a1c*samplenum2) + a2c/(a1c*a1c)
		e1c<-c1c/a1c
		e2c<-c2c/( (a1c*a1c)+a2c )


		D.numerator2<-Separation.Site2$Pi-Separation.Site2$Sita/a1c
		D.denominator2<-sqrt( e1c*Separation.Site2$Sita + e2c*Separation.Site2$Sita*(Separation.Site2$Sita-1) )
		Separation.Site2$Tajima.D <- D.numerator2/D.denominator2
		
		Separation.Site1$cutline<-"|"
		Separation.Site1<-cbind(Separation.Site1,Separation.Site2)
		Separation.Site1$fst<-fst
	}

	write.table(Separation.Site1,file="Site.Polymorphism",sep="\t",row.names=FALSE,quote=FALSE,append=TRUE)
}








q(save="no")


	





	

