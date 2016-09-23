cat("\014") 
options(max.print=1000000)
library(vioplot)
t1 <- Sys.time()
rq2_au_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.au.csv"
rq2_sf_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.sf.csv"
rq2_so_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.so.csv"
rq2_su_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.su.csv"
rq2_ux_file ="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/final_rq2.unix.csv"



rq2_au_data <- read.csv(rq2_au_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
rq2_sf_data <- read.csv(rq2_sf_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
rq2_so_data <- read.csv(rq2_so_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
rq2_su_data <- read.csv(rq2_su_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
rq2_ux_data <- read.csv(rq2_ux_file, header=FALSE, stringsAsFactors=F)[ -1, 1:6]
#print(rq2_au_data)
plotData <- function(auP, sfP, soP, suP, uxP, ylimRangeP, yLabParam)
{
#   mean_au <- tapply(auP, mean)
#   mean_sf <- tapply(sfP, mean)  
#   mean_su <- tapply(suP, mean)
#   mean_ux <- tapply(uxP, mean) 
  dir2compile="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/src/"
  dir2SavePlots="/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/"
  # make sure the plots are saved in the output directory 
  setwd(dir2SavePlots)
  # set the box plot name file 
  box_plot_file_name <- paste(yLabParam, ".box.png", sep=".")  
  png(box_plot_file_name, width=4, height=4, units="in", res=750)
  boxplot(auP, sfP, soP, suP, uxP, 
          col=c("grey","blue","green", "yellow", "red"), 
          names=c("AU","SF", "SO", "SU", "UNIX"), xlab="Q&A Websites", ylab=yLabParam, 
          ylim = ylimRangeP
          )
  dev.off()
  # saving box plot done 
  # set the violin plot name 
  vio_plot_file_name <- paste(yLabParam, ".vio.png", sep=".")  
  png(vio_plot_file_name, width=4, height=4, units="in", res=750)
  vioplot(auP, sfP, soP, suP, uxP, names=c("AU","SF", "SO", "SU", "UNIX"),  ylim=ylimRangeP, col="yellow")
  title(yLabParam)
  # saving violin plot done   
  dev.off()
  ## go back to src directory 
  setwd(dir2compile)
}

# ### Comparing scores of questions ... started 
rq2_au_score_q <- as.numeric( rq2_au_data[, 1] )
rq2_sf_score_q <- as.numeric( rq2_sf_data[, 1] )
rq2_so_score_q <- as.numeric( rq2_so_data[, 1] )
rq2_su_score_q <- as.numeric( rq2_su_data[, 1] )
rq2_ux_score_q <- as.numeric( rq2_ux_data[, 1] )
plotData(rq2_au_score_q, rq2_sf_score_q, rq2_su_score_q, rq2_so_score_q, rq2_ux_score_q, ylim = c(-5, 750),  "Score of questions")
## high y limit range for stack overflow 
# ### Comparing scores of questions ... ended 

### Comparing view count of questions ... started 
rq2_au_vcount_q <- as.numeric( rq2_au_data[, 2] )
rq2_sf_vcount_q <- as.numeric( rq2_sf_data[, 2] )
rq2_so_vcount_q <- as.numeric( rq2_so_data[, 2] )
rq2_su_vcount_q <- as.numeric( rq2_su_data[, 2] )
rq2_ux_vcount_q <- as.numeric( rq2_ux_data[, 2] )
plotData(rq2_au_vcount_q, rq2_sf_vcount_q, rq2_so_vcount_q, rq2_su_vcount_q, rq2_ux_vcount_q, ylim = c(-5, 200000),  "Count of views")
### Comparing view count of questions ... ended 


### Comparing  count of answers per question ... started 
rq2_au_acount_q <- as.numeric( rq2_au_data[, 3] )
rq2_sf_acount_q <- as.numeric( rq2_sf_data[, 3] )
rq2_so_acount_q <- as.numeric( rq2_so_data[, 3] )
rq2_su_acount_q <- as.numeric( rq2_su_data[, 3] )
rq2_ux_acount_q <- as.numeric( rq2_ux_data[, 3] )
plotData(rq2_au_acount_q, rq2_sf_acount_q, rq2_so_acount_q, rq2_su_acount_q, rq2_ux_acount_q, ylim = c(-5, 20),  "Count of answers")
### Comparing  count of answers per question ... ended 



### Comparing  comment count per question ... started 
rq2_au_comcount_q <- as.numeric( rq2_au_data[, 4] )
rq2_sf_comcount_q <- as.numeric( rq2_sf_data[, 4] )
rq2_so_comcount_q <- as.numeric( rq2_so_data[, 4] )
rq2_su_comcount_q <- as.numeric( rq2_su_data[, 4] )
rq2_ux_comcount_q <- as.numeric( rq2_ux_data[, 4] )
plotData(rq2_au_comcount_q, rq2_sf_comcount_q, rq2_so_comcount_q, rq2_su_comcount_q, rq2_ux_comcount_q, ylim = c(-5, 30),  "Count of comments")
### Comparing  comment count per question ... ended 



### Comparing  fav count per question ... started 
rq2_au_favcount_q <- as.numeric( rq2_au_data[, 5] )
rq2_sf_favcount_q <- as.numeric( rq2_sf_data[, 5] )
rq2_so_favcount_q <- as.numeric( rq2_so_data[, 5] )
rq2_su_favcount_q <- as.numeric( rq2_su_data[, 5] )
rq2_ux_favcount_q <- as.numeric( rq2_ux_data[, 5] )
plotData(rq2_au_favcount_q, rq2_sf_favcount_q, rq2_so_favcount_q, rq2_su_favcount_q, rq2_ux_favcount_q, ylim = c(-5, 500),  "Count of favorite")
## high y limit range for stack overflow 
### Comparing  fav count per question ... ended 



### Comparing  score for answer ... started 
rq2_au_score_a <- as.numeric( rq2_au_data[, 6] )
rq2_sf_score_a <- as.numeric( rq2_sf_data[, 6] )
rq2_so_score_a <- as.numeric( rq2_so_data[, 6] )
rq2_su_score_a <- as.numeric( rq2_su_data[, 6] )
rq2_ux_score_a <- as.numeric( rq2_ux_data[, 6] )
plotData(rq2_au_favcount_q, rq2_sf_favcount_q, rq2_so_score_a, rq2_su_favcount_q, rq2_ux_favcount_q, ylim = c(-5, 750),  "Score of answers")
## high y limit range for stack overflow 
### Comparing  score for answer ... ended 


t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))

