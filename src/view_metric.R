cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/data/all_needed_content.csv"
content_data <- read.csv(content_file)


topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/with_title_all_corpus_20_topics/_TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)




t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))