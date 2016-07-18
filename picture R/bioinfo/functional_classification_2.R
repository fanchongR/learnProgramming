kegg <- scan("/ifswh1/BC_Asia/huangjq/F13FTSECKF2516_STRbqcD/04.Genome_Function/604F/01.General_Gene_Annotation/03.anno.kegg/functional_classification_2.stat",what="character",sep="
")
kegg <- as.character(sapply(kegg,function(x) strsplit(x,"	")[[1]][1:3]))
kegg <- as.data.frame.list(tapply(kegg,rep(1:3,t=(length(kegg)/3)),as.character))
kegg <- kegg[-1,]

kegg.num <- as.numeric(as.matrix(kegg[,3]))
kegg.name <- paste(kegg[,1], "--", kegg[,2], sep="")


pdf(file="/ifswh1/BC_Asia/huangjq/F13FTSECKF2516_STRbqcD/04.Genome_Function/604F/01.General_Gene_Annotation/03.anno.kegg/functional_classification_2.pdf",15,7)

def.par <- par()
par(mar=c(3,31.5,3,1.5)+.1)
locate = barplot(kegg.num,col=rainbow(24),xlim=c(0,max(kegg.num)*1.1),cex.names=0.8,las=1,
axis.lty=0,cex.axis=0.6,xaxt="n",horiz=TRUE,line=-0.8)
box()
kegg_count = length(kegg.num);
for(i in 1:kegg_count)
{
		text(kegg.num[i], locate[i,1], kegg.num[i], pos=4, cex=0.7);
}
mtext("Number of matched genes",side=1,line=1,font=2,cex=1.2)

axis(side=2,at=locate,labels=kegg.name,padj=0.5,tick=FALSE,font=1,las=1, line=-0.5)
axis(side=1,font=1,tck=0.01,mgp=c(0,0,0))

title("KEGG pathway classification")

dev.off()

