cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/ForReproc/FullQAndAContent.csv"
content_data <- read.csv(content_file)

print("------------Head of content------------------")
print(head(content_data))


topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/_TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)

trendInputData <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/_TrendInp.csv"

topic_names <- colnames(topic_prob_data, do.NULL = TRUE, prefix = "col")
doc_names <- rownames(topic_prob_data, do.NULL = TRUE, prefix = "row")

topic_names <- topic_names[!topic_names %in% "X"]

len_doc_names <- length(doc_names)
len_top_names <- length(topic_names)
dic_topics <- vector(mode="list", length=len_doc_names)
names(dic_topics) <- doc_names
###threshold 
topic_prob_cutoff <- 0.10


# print("----- The final string to dump -----")
# fullContent  <- data.frame(idContent, dateContent, topIndCont, origIDCont)
# print(head(fullContent))
# write.csv(fullContent, file=trendInputData, row.names=FALSE, na='0') 
t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))