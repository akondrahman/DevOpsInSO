cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(RMySQL)
library(ggplot2)

mydb = dbConnect(MySQL(), user='root', password='SrcML#2016', dbname='DevOpsInSO', host='localhost')
#dbListTables(mydb)
DiffiTrendYearOut <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/Yr_Diff_N_Trend.csv"
allYears          <- c("2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016")
lenyear         <- length(allYears)


###the vector that holds verything 
fullContent    <- c()
### temp vector for holdind indi. stuff 
topIndCont     <- c()
yearContent    <- c()
diffCultCount  <- c()

for(topicCnt in 1:20)
{
  topicMsg <-paste0("This is topic-", topicCnt, sep="")
  print(topicMsg)
  for(index_ in 1:lenyear)
  {
    thisYear <- allYears[index_]
    print(thisYear)    

    dateQuery1 <- paste0(thisYear, "-%", sep="") 
    #print(dateQuery1)    
    
    shortened_year <- substr(thisYear, 3, 4)
    #print(shortened_year)

    dateQuery2 <- paste0("%/", shortened_year, sep="")    
    #print(dateQuery2)
    
    ###Now the dates are extracted in required format, lets build query for all questions per month that belong in a topic
    
    query_part_one   <- paste0("SELECT COUNT(*) FROM diffntrend WHERE (dateContent LIKE '", dateQuery1, sep="")
    query_part_two   <- paste0(query_part_one, "' or dateContent LIKE '", sep="")    
    query_part_three <- paste0(query_part_two, dateQuery2, sep="")
    query_part_four  <- paste0(query_part_three, "') and topIndCont=", sep="")    
    query_part_five  <- paste0(query_part_four, topicCnt, sep="")    
    #print(query_part_five)
    query_q_per_yr   <- query_part_five
    
    rs_q_per_yr      <- dbSendQuery(mydb, query_q_per_yr)
    out_q_per_yr     <- fetch(rs_q_per_yr, n=-1)
    #print((out_q_per_yr))
    #print(":::::Done with all count:::::")
    
    ###now, lets build query for questions with accepted answers per month that belong in a topic   
    query_part_six  <- paste0(query_q_per_yr, " and accAnsCont > 0", sep="")    
    qury_qaa_per_yr <- query_part_six
    #print(qury_qaa_per_yr)
    
    rs_qaa_per_yr   <- dbSendQuery(mydb, qury_qaa_per_yr)
    out_qaa_per_yr  <- fetch(rs_qaa_per_yr, n=-1)
    #print((out_qaa_per_yr))
    #print("=====Done with aa count=====")
    
    ###now, lets build query for questions with no accepted answers per month that belong in a topic   
    query_part_seven  <- paste0(query_q_per_yr, " and accAnsCont=0", sep="")    
    qury_qnaa_per_yr  <- query_part_seven
    ###print(qury_qnaa_per_yr)
    
    rs_qnaa_per_yr   <- dbSendQuery(mydb, qury_qnaa_per_yr)
    out_qnaa_peryr   <- fetch(rs_qnaa_per_yr, n=-1)
    #print((out_qnaa_peryr)) 
    
    difficult_per_yr <- (as.double(out_qnaa_peryr - out_qaa_per_yr)/as.double(out_q_per_yr))*100
    #print(difficult_per_yr)
    
    ##Appending 
    topIndCont        <-c(topIndCont, topicCnt)    
    yearContent       <-c(yearContent, thisYear)
    diffCultCount     <-c(diffCultCount, difficult_per_yr)
    
  }  
  print("========================================")
}

print("----- The final string to dump -----")
fullContent  <- data.frame(topIndCont, yearContent, diffCultCount)
print(head(fullContent))

write.csv(fullContent, file=DiffiTrendYearOut, row.names=FALSE) 

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))