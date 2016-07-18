#!/ifs4/BC_PUB/biosoft/pipeline/Package/R-3.1.1/bin/Rscript
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
	--snp=filepath   
	--trait=filepath 
	--step=123...	   - 1: t test
			   - 2: rank sum test (Wilcoxon)
			   - 3: permutation test

			   - 4: analysis of variance (ANOVA)
			   - 5: rank sum test (Kruskal-Wallis)
			   - 6: permutation test (corresponding to Kruskal-Wallis rank sum test)

			   - 7: chi-square test (pearson test of independence)
			   - 8: fisher test of independence
			   - 9: permutation test (corresponding to chi-square test)
			
	--help             - if haplotypes and trait is continuous variable, could set --step=123
			   - if amphiploid and trait is continuous variable, could set --step=456
			   - if trait is categorical variable, could set --step=789

	Example:
	Rscript hypothesis.testing.R --snp=filepath --trait=filepath --step=123 \n\n")
	q(save="no")
}

parseArgs <- function (x) strsplit (sub ("^--", "", x), "=")
argsDF <- as.data.frame (do.call ("rbind", parseArgs(args )))
option <- as.list (as.character (argsDF$V2))
names (option) <- argsDF$V1


if( any(grep('[123456]',option$step)) ){
	data<-read.table(option$snp,sep='\t',header=FALSE)
	trait<-read.table(option$trait,sep='\t',header=FALSE)
	snpname<-data[-1,1]
	data<-data[,c(-1,-2)]
	data<-data[,order( data[1,] )]
	data<-data[-1,]
	trait<-trait[ order(trait[,1]) ,]
	trait<-trait[,2]

	N<-nrow(data)
}



if( any(grep('1',option$step)) ){
	output<-data.frame(snpname)
	output$pvalue<-NA
	for(i in 1:N){
		snp<-as.vector(unlist(data[i,]))
		temp<-table( snp )
		if(length(temp) == 2 & all(temp>=2))output$pvalue[i]<-t.test(trait~snp)$p.value else next
	}
	output<-output[!is.na(output$pvalue),]
	output$fdr<-p.adjust(output$pvalue,method="fdr")
	write.table(output,"t_test_pvalue",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.05,]
	write.table(output,"t_test_pvalue0.05",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.01,]
	write.table(output,"t_test_pvalue0.01",sep='\t',row.names=FALSE,quote=FALSE)
}



if( any(grep('2',option$step)) ){
	output<-data.frame(snpname)
	output$pvalue<-NA
	for(i in 1:N){
		snp<-as.vector(unlist(data[i,]))
		temp<-table( snp )
		if(length(temp) == 2)output$pvalue[i]<-wilcox.test(trait~snp)$p.value else next
	}
	output<-output[!is.na(output$pvalue),]
	output$fdr<-p.adjust(output$pvalue,method="fdr")
	write.table(output,"ranksum_test_pvalue",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.05,]
	write.table(output,"ranksum_test_pvalue0.05",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.01,]
	write.table(output,"ranksum_test_pvalue0.01",sep='\t',row.names=FALSE,quote=FALSE)
}





if( any(grep('3',option$step)) ){
	library(coin,lib.loc="/home/fanchong/R/x86_64-unknown-linux-gnu-library/2.10/")
	tdata<-t(data)
	data.all<-data.frame(trait)
	data.all<-cbind(data.all,tdata)

	output<-data.frame(snpname)
	output$pvalue<-NA
	for(i in 1:N){
		snp<-as.vector(unlist(data[i,]))
		temp<-table( snp )
		if(length(temp) == 2) output$pvalue[i]<- pvalue( oneway_test(data.all[,1]~data.all[,i+1],data.all,distribution="exact") ) else next
	}
	output<-output[!is.na(output$pvalue),]
	output$fdr<-p.adjust(output$pvalue,method="fdr")
	write.table(output,"permutation_test_pvalue",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.05,]
	write.table(output,"permutation_test_pvalue0.05",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.01,]
	write.table(output,"permutation_test_pvalue0.01",sep='\t',row.names=FALSE,quote=FALSE)
}



##########################################################################################################################################################################


if( any(grep('4',option$step)) ){
	output<-data.frame(snpname)
	output$pvalue<-NA
	for(i in 1:N){
		snp<-as.vector(unlist(data[i,]))
		temp<-table( snp )
		if(length(temp) >  2)output$pvalue[i]<-summary( aov(trait~snp) )[[1]][1,5]
		if(length(temp) == 2 & all(temp>=2))output$pvalue[i]<-t.test(trait~snp)$p.value 
	}
	output<-output[!is.na(output$pvalue),]
	output$fdr<-p.adjust(output$pvalue,method="fdr")
	write.table(output,"aov_pvalue",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.05,]
	write.table(output,"aov_pvalue0.05",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.01,]
	write.table(output,"aov_pvalue0.01",sep='\t',row.names=FALSE,quote=FALSE)
}


if( any(grep('5',option$step)) ){
	output<-data.frame(snpname)
	output$pvalue<-NA
	for(i in 1:N){
		snp<-as.vector(unlist(data[i,]))
		temp<-table( snp )
		if(length(temp) >  2)output$pvalue[i]<- kruskal.test(trait~as.factor(snp))$p.value
		if(length(temp) == 2)output$pvalue[i]<-wilcox.test(trait~snp)$p.value
	}
	output<-output[!is.na(output$pvalue),]
	output$fdr<-p.adjust(output$pvalue,method="fdr")
	write.table(output,"kruskal_test_pvalue",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.05,]
	write.table(output,"kruskal_test_pvalue0.05",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.01,]
	write.table(output,"kruskal_test_pvalue0.01",sep='\t',row.names=FALSE,quote=FALSE)
}





if( any(grep('6',option$step)) ){
	library(coin,lib.loc="/home/fanchong/R/x86_64-unknown-linux-gnu-library/2.10/")
	tdata<-t(data)
	data.all<-data.frame(trait)
	data.all<-cbind(data.all,tdata)

	output<-data.frame(snpname)
	output$pvalue<-NA
	for(i in 1:N){
		snp<-as.vector(unlist(data[i,]))
		temp<-table( snp )
		if(length(temp) >  2) output$pvalue[i]<- pvalue( kruskal_test(data.all[,1]~data.all[,i+1],data.all) )
		if(length(temp) == 2) output$pvalue[i]<- pvalue( oneway_test(data.all[,1]~data.all[,i+1],data.all,distribution="exact") ) 
	}
	output<-output[!is.na(output$pvalue),]
	output$fdr<-p.adjust(output$pvalue,method="fdr")
	write.table(output,"permutation_test_kruskal_pvalue",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.05,]
	write.table(output,"permutation_test_kruskal_pvalue0.05",sep='\t',row.names=FALSE,quote=FALSE)
	output<-output[output$fdr<=0.01,]
	write.table(output,"permutation_test_kruskal_pvalue0.01",sep='\t',row.names=FALSE,quote=FALSE)
}
























##########################################################################################################################################################################

if( any(grep('[789]',option$step)) ){
	data<-read.table(option$snp,sep='\t',header=FALSE)
	trait<-read.table(option$trait,header=TRUE)
	snpname<-data[-1,1]
	data<-data[,c(-1,-2)]
	data<-data[,order( data[1,] )]
	data<-data[-1,]

	trait<-trait[ order(trait[,1]) ,]
	name.trait<-names(trait)[-1]
	trait<-as.data.frame(trait[,-1])
	

	N<-nrow(data)
	num.trait<-ncol(trait)
	
}




if( any(grep('7',option$step)) ){
	filename<-paste(name.trait,"chi-square_test_pvalue",sep="_")
	filename0.05<-paste(filename,"0.05",sep="")
	filename0.01<-paste(filename,"0.01",sep="")

	for(ntrait in 1:num.trait){

		output<-data.frame(snpname)
		output$pvalue<-NA

		type.trait<-table(trait[,ntrait])
		if(length(type.trait) < 2)next

			for(i in 1:N){
				snp<-as.vector(unlist(data[i,]))
				temp<-table( snp )
				if(length(temp) >= 2) output$pvalue[i]<-chisq.test(trait[,ntrait],snp)$p.value
			}
			output<-output[!is.na(output$pvalue),]
			output$fdr<-p.adjust(output$pvalue,method="fdr")
			write.table(output,filename[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
			output<-output[output$fdr<=0.05,]
			write.table(output,filename0.05[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
			output<-output[output$fdr<=0.01,]
			write.table(output,filename0.01[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
	}
}



if( any(grep('9',option$step)) ){
	library(coin,lib.loc="/home/fanchong/R/x86_64-unknown-linux-gnu-library/2.10/")

	filename<-paste(name.trait,"permutation_test_chi-square_pvalue",sep="_")
	filename0.05<-paste(filename,"0.05",sep="")
	filename0.01<-paste(filename,"0.01",sep="")

	for(ntrait in 1:num.trait){
		tdata<-t(data)
		data.all<-data.frame(trait[,ntrait])
		data.all<-cbind(data.all,tdata)

		output<-data.frame(snpname)
		output$pvalue<-NA

		type.trait<-table(trait[,ntrait])
		if(length(type.trait) < 2)next

			for(i in 1:N){
				snp<-as.vector(unlist(data[i,]))
				temp<-table( snp )
				if(length(temp) >= 2) output$pvalue[i]<- pvalue( chisq_test( data.all[,1]~data.all[,i+1],data.all ) )
			}
			output<-output[!is.na(output$pvalue),]
			output$fdr<-p.adjust(output$pvalue,method="fdr")
			write.table(output,filename[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
			output<-output[output$fdr<=0.05,]
			write.table(output,filename0.05[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
			output<-output[output$fdr<=0.01,]
			write.table(output,filename0.01[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
	}
}




if( any(grep('8',option$step)) ){
	filename<-paste(name.trait,"fisher_test_pvalue",sep="_")
	filename0.05<-paste(filename,"0.05",sep="")
	filename0.01<-paste(filename,"0.01",sep="")

	for(ntrait in 1:num.trait){

		output<-data.frame(snpname)
		output$pvalue<-NA

		type.trait<-table(trait[,ntrait])
		if(length(type.trait) < 2)next

			for(i in 1:N){
				snp<-as.vector(unlist(data[i,]))
				temp<-table( snp )
				if(length(temp) >= 2) output$pvalue[i]<-fisher.test(trait[,ntrait],snp)$p.value
			}
			output<-output[!is.na(output$pvalue),]
			output$fdr<-p.adjust(output$pvalue,method="fdr")
			write.table(output,filename[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
			output<-output[output$fdr<=0.05,]
			write.table(output,filename0.05[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
			output<-output[output$fdr<=0.01,]
			write.table(output,filename0.01[ntrait],sep='\t',row.names=FALSE,quote=FALSE)
	}
}

