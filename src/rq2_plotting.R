cat("\014") 
options(max.print=1000000)
library(vioplot)
t1 <- Sys.time()
rq2_au_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.au.csv"
rq2_sf_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.sf.csv"
rq2_su_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.su.csv"
rq2_ux_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.unix.csv"


rq2_au_data <- read.csv(rq2_au_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
rq2_sf_data <- read.csv(rq2_sf_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
rq2_su_data <- read.csv(rq2_su_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
rq2_ux_data <- read.csv(rq2_ux_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
#print(rq2_au_data)
plotData <- function(auP, sfP, suP, uxP, ylimRangeP, yLabParam)
{
#   mean_au <- tapply(auP, mean)
#   mean_sf <- tapply(sfP, mean)  
#   mean_su <- tapply(suP, mean)
#   mean_ux <- tapply(uxP, mean)    

  boxplot(auP, sfP, suP, uxP, 
          col=c("grey","blue","green", "yellow"), 
          names=c("AU","SF","SU", "UNIX"), xlab="Q&A Websites", ylab=yLabParam, 
          ylim = ylimRangeP
          )

  vioplot(auP, sfP, suP, uxP, names=c("AU","SF","SU", "UNIX"),  ylim=ylimRangeP, col="yellow")
  title(yLabParam)
}



# ### Comparing scores of questions ... started 
rq2_au_score_q <- as.numeric( rq2_au_data[, 1] )
rq2_sf_score_q <- as.numeric( rq2_sf_data[, 1] )
rq2_su_score_q <- as.numeric( rq2_su_data[, 1] )
rq2_ux_score_q <- as.numeric( rq2_ux_data[, 1] )
plotData(rq2_au_score_q, rq2_sf_score_q, rq2_su_score_q, rq2_ux_score_q, ylim = c(-5, 150),  "Score of questions")
# ### Comparing scores of questions ... ended 

### Comparing view count of questions ... started 
rq2_au_vcount_q <- as.numeric( rq2_au_data[, 2] )
rq2_sf_vcount_q <- as.numeric( rq2_sf_data[, 2] )
rq2_su_vcount_q <- as.numeric( rq2_su_data[, 2] )
rq2_ux_vcount_q <- as.numeric( rq2_ux_data[, 2] )
plotData(rq2_au_vcount_q, rq2_sf_vcount_q, rq2_su_vcount_q, rq2_ux_vcount_q, ylim = c(-5, 200000),  "Count of views")
### Comparing view count of questions ... ended 


### Comparing  count of answers per question ... started 
rq2_au_acount_q <- as.numeric( rq2_au_data[, 3] )
rq2_sf_acount_q <- as.numeric( rq2_sf_data[, 3] )
rq2_su_acount_q <- as.numeric( rq2_su_data[, 3] )
rq2_ux_acount_q <- as.numeric( rq2_ux_data[, 3] )
plotData(rq2_au_acount_q, rq2_sf_acount_q, rq2_su_acount_q, rq2_ux_acount_q, ylim = c(-5, 20),  "Count of answers")
### Comparing  count of answers per question ... ended 



### Comparing  comment count per question ... started 
rq2_au_comcount_q <- as.numeric( rq2_au_data[, 4] )
rq2_sf_comcount_q <- as.numeric( rq2_sf_data[, 4] )
rq2_su_comcount_q <- as.numeric( rq2_su_data[, 4] )
rq2_ux_comcount_q <- as.numeric( rq2_ux_data[, 4] )
plotData(rq2_au_comcount_q, rq2_sf_comcount_q, rq2_su_comcount_q, rq2_ux_comcount_q, ylim = c(-5, 25),  "Count of comments")
### Comparing  comment count per question ... ended 



### Comparing  fav count per question ... started 
rq2_au_favcount_q <- as.numeric( rq2_au_data[, 5] )
rq2_sf_favcount_q <- as.numeric( rq2_sf_data[, 5] )
rq2_su_favcount_q <- as.numeric( rq2_su_data[, 5] )
rq2_ux_favcount_q <- as.numeric( rq2_ux_data[, 5] )
plotData(rq2_au_favcount_q, rq2_sf_favcount_q, rq2_su_favcount_q, rq2_ux_favcount_q, ylim = c(-5, 25),  "Count of favorite")
### Comparing  fav count per question ... ended 



### Comparing  score for answer ... started 
rq2_au_score_a <- as.numeric( rq2_au_data[, 6] )
rq2_sf_score_a <- as.numeric( rq2_sf_data[, 6] )
rq2_su_score_a <- as.numeric( rq2_su_data[, 6] )
rq2_ux_score_a <- as.numeric( rq2_ux_data[, 6] )
plotData(rq2_au_favcount_q, rq2_sf_favcount_q, rq2_su_favcount_q, rq2_ux_favcount_q, ylim = c(-5, 30),  "Score of answers")
### Comparing  score for answer ... ended 


t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))

