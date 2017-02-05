cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

library(RMySQL)
library(ggplot2)

mydb = dbConnect(MySQL(), user='root', password='SrcML#2016', dbname='DevOpsInSO', host='localhost')
#dbListTables(mydb)
DiffiTrendMonthOut <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/Mo_Diff_N_Trend.csv"
allMonths <- c('2008-08', '2008-09', '2008-10', '2008-11', '2008-12', '2009-01', '2009-02', '2009-03', '2009-04', '2009-05', '2009-06', '2009-07', '2009-08', '2009-09', '2009-10', '2009-11', '2009-12', '2010-01', '2010-02', '2010-03', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12', '2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12', '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09', '2012-10', '2012-11', '2012-12', '2013-01', '2013-02', '2013-03', '2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12', '2014-01', '2014-02', '2014-03', '2014-04', '2014-05', '2014-06', '2014-07', '2014-08', '2014-09', '2014-10', '2014-11', '2014-12', '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12', '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', '2016-09')
len_month <- length(allMonths)


###the vector that holds verything 
fullContent    <- c()
### temp vector for holdind indi. stuff 
topIndCont     <- c()
montContent    <- c()
diffCultCount  <- c()

for(topicCnt in 1:20)
{
  topicMsg <-paste0("This is topic-", topicCnt, sep="")
  print(topicMsg)
  for(index_ in 1:len_month)
  {
    thisMonth <- allMonths[index_]
    #print(thisMonth)
    dateQuery1 <- paste0(thisMonth, "-%", sep="")
    #print(dateQuery1)
    
    ## so far so good , lets get the other date format 
    splitted_elems <- strsplit(thisMonth, "-")
    #print(splitted_elems)
    ### getting the year part 
    year_  <- splitted_elems[[1]][1]
    #print(year_)
    shortened_year <- substr(year_, 3, 4)
    #print(shortened_year)
    ### getting the month part 
    month_  <- splitted_elems[[1]][2]
    #print(month_)   
    if(substr(month_, 1, 1)=="0")
    {
      shortened_month <- substr(month_, 2, 2)
    }
    else
    {
      shortened_month <- substr(month_, 1, 2)
    }
    #print(shortened_month)
    tempQuery2 <- paste0(shortened_month, "/%/", sep="")        
    dateQuery2 <- paste0(tempQuery2, shortened_year, sep="")    
    #print(dateQuery2)
    
    ###Now the dates are extracted in required format, lets build query for all questions per month that belong in a topic
    
    query_part_one   <- paste0("SELECT COUNT(*) FROM diffntrend WHERE (dateContent LIKE '", dateQuery1, sep="")
    query_part_two   <- paste0(query_part_one, "' or dateContent LIKE '", sep="")    
    query_part_three <- paste0(query_part_two, dateQuery2, sep="")
    query_part_four  <- paste0(query_part_three, "') and topIndCont=", sep="")    
    query_part_five  <- paste0(query_part_four, topicCnt, sep="")    
    #print(query_part_five)
    query_q_per_mon  <- query_part_five

    rs_q_per_mon     <- dbSendQuery(mydb, query_q_per_mon)
    out_q_per_mon    <- fetch(rs_q_per_mon, n=-1)
    #print((out_q_per_mon))
    #print(":::::Done with all count:::::")
    
    ###now, lets build query for questions with accepted answers per month that belong in a topic   
    query_part_six  <- paste0(query_q_per_mon, " and accAnsCont > 0", sep="")    
    qury_qaa_perMon <- query_part_six
    #print(qury_qaa_perMon)
    
    rs_qaa_permon   <- dbSendQuery(mydb, qury_qaa_perMon)
    out_qaa_permon  <- fetch(rs_qaa_permon, n=-1)
    #print((out_qaa_permon))
    #print("=====Done with aa count=====")
    
    ###now, lets build query for questions with no accepted answers per month that belong in a topic   
    query_part_seven  <- paste0(query_q_per_mon, " and accAnsCont=0", sep="")    
    qury_qnaa_perMon  <- query_part_seven
    #print(qury_qnaa_perMon)
    
    rs_qnaa_permon   <- dbSendQuery(mydb, qury_qnaa_perMon)
    out_qnaa_permon  <- fetch(rs_qnaa_permon, n=-1)
    #print((out_qnaa_permon)) 
    
    difficult_permon <- (as.double(out_qnaa_permon - out_qaa_permon)/as.double(out_q_per_mon))*100
    #print(difficult_permon)
    
    ##Appending 
    topIndCont        <-c(topIndCont, topicCnt)    
    montContent       <-c(montContent, thisMonth)
    diffCultCount     <-c(diffCultCount, difficult_permon)
    
    #print("=====Are we done yet?=====")
  }  
}

print("----- The final string to dump -----")
fullContent  <- data.frame(topIndCont, montContent, diffCultCount)
print(head(fullContent))

write.csv(fullContent, file=DiffiTrendMonthOut, row.names=FALSE) 
t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))